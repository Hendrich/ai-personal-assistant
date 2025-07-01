import os
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool
from langchain_huggingface import HuggingFaceEndpoint
from langchain_openai import OpenAI

# Prompt: Personal Assistant
system_prompt = """
Anda adalah AI Personal Assistant yang membantu user dalam aktivitas sehari-hari, seperti menjawab pertanyaan umum, melakukan perhitungan matematika sederhana, dan memberikan informasi yang bermanfaat. Jika perlu, gunakan tools yang tersedia.
"""

# Memory: Episodic (percakapan)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Tool: Kalkulator Matematika Sederhana
def kalkulator(expr: str) -> str:
    try:
        result = eval(expr, {"__builtins__": {}})
        return f"Hasil perhitungan: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

tools = [
    Tool(
        name="Kalkulator Matematika",
        func=kalkulator,
        description="Lakukan perhitungan matematika sederhana. Input: ekspresi matematika (contoh: 2+2*5)"
    )
]

# Model: OpenAI GPT (chat model, via OpenAI API)
llm = OpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.7,
    max_tokens=512
)

# Agent (conversational)
from langchain.agents import initialize_agent

agent = initialize_agent(
    tools,
    llm,
    agent="conversational-react-description",
    memory=memory,
    verbose=True,
)

def main():
    print("AI Personal Assistant. Ketik 'exit' untuk keluar.")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break
        response = agent.invoke({"input": user_input})
        print(f"AI: {response['output']}")

if __name__ == "__main__":
    main()
