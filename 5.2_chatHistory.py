from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import os

os.environ["OPENAI_API_KEY"] = (
    "sk-xxxxxxxxxxxxxxxxxxxxx"  # 🔒 Replace with your key
)

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

chat_history = [SystemMessage(content="You are a helpful AI assistant")]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))

    if user_input.lower() == "exit":
        break

    # Invoke model
    result = model.invoke(chat_history)

    # Append assistant response
    chat_history.append(AIMessage(content=result.content))

    # Print AI response
    print("AI:", result.content)

    # ✅ Print token usage
    usage = result.response_metadata.get("token_usage", {})
    input_tokens = usage.get("prompt_tokens", 0)
    output_tokens = usage.get("completion_tokens", 0)
    total_tokens = usage.get("total_tokens", 0)

    print(
        f"Tokens used -> Input: {input_tokens}, Output: {output_tokens}, Total: {total_tokens}"
    )

print(chat_history)
