import kioko

memory = kioko.intelligent("sqlite:///test-memory.db")

user = "test_user"
session = "session_1"

memory.record_turn(
    "I am a Python developer.",
    "Nice!",
    user_id=user,
    session_id=session
)

memory.record_turn(
    "My goal is to build an AI SaaS product.",
    "Let's work towards it.",
    user_id=user,
    session_id=session
)

memory.record_turn(
    "To make the AI agent - intilize LLM ,chunking,embedding , system prompt , output  .",
    "Let's work towards it.",
    user_id=user,
    session_id=session
)

memory.record_turn(
    "I had complete all the AI basic to medium things like - RAG ,ai agents ,grapg retrieval etc ",
    "Let's work towards it.",
    user_id=user,
    session_id="session_3"
)



queries = [
    "What is my profession?",
    "What is my AI SaaS goal?",
    "What AI technologies have I completed?"
]

for q in queries:
    print("\nQUESTION:", q)

    ctx = memory.recall(
        q,
        user_id=user,
        session_id="session_2"
    )

    print(ctx.text)

