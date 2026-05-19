from langchain_anthropic import ChatAnthropic
from dotenv  import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-2", temperature=0.9, max_completion_tokens=10)
results = model.invoke("what is the capital of china?")
print(results.content)