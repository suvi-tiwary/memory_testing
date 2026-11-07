import kioko

memory = kioko.intelligent("sqlite:///test-memory.db")

ctx = memory.recall(
    "What have I learned about AI?",
    user_id="test_user",
    session_id="session_3"
)

print(ctx.text)