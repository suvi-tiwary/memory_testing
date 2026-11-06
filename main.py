import kioko

memory = kioko.intelligent("sqlite:///plant-memory.db")      # a file next to your code; nothing else to set up

# After each exchange, hand the turn to Kioko. It decides what is worth keeping, and where.
memory.record_turn("Hi, I'm Asha, a controls engineer at the Pune plant. I prefer short answers.",
                   "Nice to meet you, Asha!", user_id="asha", session_id="mon-shift")
memory.record_turn("My goal is to get line 3 OEE above 85% by December 31.",
                   "Noted - let's track it.", user_id="asha", session_id="mon-shift")
memory.record_turn("To reset the safety relay, switch off the main breaker, then press reset for 5 seconds, "
                   "then switch the breaker back on.", "Thanks, saved.", user_id="asha", session_id="mon-shift")

# Before each answer, ask Kioko what the agent should know.
ctx = memory.recall("what is my name ", user_id="asha", session_id="tue-shift")
print(ctx.text)