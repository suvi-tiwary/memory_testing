
import os
import kioko
from groq import Groq

# -------------------------------
# 1. Connect the LLM
# -------------------------------

client = Groq(api_key=os.environ["GROQ_API_KEY"])

MODEL = os.environ["GROQ_MODEL"]

# -------------------------------
# 2. Connect Kioko memory
# -------------------------------

memory = kioko.intelligent("sqlite:///plant-agent.db")

user = "asha"
session = "plant-support-session"


# -------------------------------
# 3. Create the agent
# -------------------------------

def answer(message):

    # STEP 1: Retrieve relevant memories
    ctx = memory.recall(
        message,
        user_id=user,
        session_id=session
    )

    # STEP 2: Give memories to the LLM
    system_prompt = f"""
    You are a helpful Plant Support AI Agent.

    Use the following memories to understand the user
    and previous plant incidents.

    If information is missing, do not make it up.

    Relevant memories:
    {str(ctx)}
    """

    # STEP 3: Generate an answer using Groq
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        temperature=0.3
    )

    reply = response.choices[0].message.content

    # STEP 4: Save the conversation in Kioko
    memory.record_turn(
        message,
        reply,
        user_id=user,
        session_id=session
    )

    return reply


# -------------------------------
# 4. Chat with the agent
# -------------------------------

print("Plant Support Agent is ready!")
print("Type 'exit' to stop.\n")

while True:

    message = input("You: ")

    if message.lower() == "exit":
        break

    reply = answer(message)

    print("\nAgent:", reply)
    print("-" * 50)
