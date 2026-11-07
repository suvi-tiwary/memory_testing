import sqlite3
import json

conn = sqlite3.connect("test-memory.db")
cursor = conn.cursor()

user = "test_user"

# 1. Count memories by type
print("\n========== MEMORY COUNTS ==========")

cursor.execute("""
    SELECT memory_type, COUNT(*)
    FROM kioko_memories
    WHERE user_id = ?
    GROUP BY memory_type
""", (user,))

for row in cursor.fetchall():
    print(row)

# 2. Inspect actual memories
print("\n========== STORED MEMORIES ==========")

cursor.execute("""
    SELECT id, content, memory_type, session_id,
           importance, source, created_at
    FROM kioko_memories
    WHERE user_id = ?
    ORDER BY created_at
""", (user,))

for row in cursor.fetchall():
    print("\nID:", row[0])
    print("CONTENT:", row[1])
    print("TYPE:", row[2])
    print("SESSION:", row[3])
    print("IMPORTANCE:", row[4])
    print("SOURCE:", row[5])
    print("CREATED:", row[6])

# 3. Inspect original messages
print("\n========== ORIGINAL MESSAGES ==========")

cursor.execute("""
    SELECT session_id, role, content
    FROM kioko_messages
    WHERE user_id = ?
    ORDER BY created_at
""", (user,))

for row in cursor.fetchall():
    print(row)

# 4. Inspect event records
print("\n========== EVENT LOG ==========")

cursor.execute("""
    SELECT seq, type, session_id, data
    FROM kioko_events
    WHERE user_id = ?
    ORDER BY seq
""", (user,))

for row in cursor.fetchall():
    print("\nSEQ:", row[0])
    print("TYPE:", row[1])
    print("SESSION:", row[2])
    print("DATA:", row[3])

conn.close()