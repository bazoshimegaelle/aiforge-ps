import os
from datetime import date
from dotenv import load_dotenv
from agents import Agent, Runner, WebSearchTool

load_dotenv()

daily_agent = Agent(
    name="AIFORGE-PS Daily Research Agent",
    instructions="""
You research daily AI cybersecurity threats affecting government and public-sector organizations.

Focus on:
- agentic AI threats
- shadow AI
- prompt injection
- AI data leakage
- AI forensics
- AI governance
- public-sector cyber risk

Produce a concise daily update with sources.
Do not recommend offensive cyber actions.
""",
    tools=[WebSearchTool()],
)

def main():
    topic = "Latest agentic AI cybersecurity threats affecting government agencies"

    prompt = f"""
Create today's daily AI cyber threat update.

Topic: {topic}

Format:
1. Date
2. Executive summary
3. New or emerging threats
4. Public-sector impact
5. Evidence to monitor
6. Defensive recommendations
7. Sources
"""

    result = Runner.run_sync(daily_agent, prompt)

    os.makedirs("daily_updates", exist_ok=True)

    filename = f"daily_updates/{date.today().isoformat()}_daily_update.md"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(result.final_output)

    print(f"Daily update saved to: {filename}")

if __name__ == "__main__":
    main()