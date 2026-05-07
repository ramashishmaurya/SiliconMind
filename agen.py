from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool
import requests

model = ChatOllama(model="qwen2.5")


@tool
def call_api():
    """Call local GET API and return response."""

    url = "http://127.0.0.1:8000/api"

    response = requests.get(url)

    return response.text


# 3. Tool for POST API
@tool
def send_data(name: str, age: int) -> list[int ,str]:
    """Send user data to API."""

    url = "http://127.0.0.1:8000/api"

    payload = {
        "name": name,
        "age": age
    }

    response = requests.post(
        url,
        json=payload
    )

    return response.json()


# 4. Create agent
agent =create_agent(
    model=model,
    tools=[call_api, send_data]
)


# 5. Invoke agent
result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Send Rahul age 22 to the API"
        }
    ]
})


# 6. Print final response
print(result["messages"][-1].content)