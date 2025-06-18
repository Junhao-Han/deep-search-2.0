import asyncio
from dotenv import load_dotenv

# Test
from agents import Agent, Runner

load_dotenv()

test_agent = Agent(
    name="Test Agent",
    instructions="You answer a question in a few words.",
    model="gpt-4o-mini",
)

async def main():
    answer = await Runner.run(test_agent, "What is the capital of Canada?")
    print(answer.final_output)

if __name__ == "__main__":
    asyncio.run(main())
