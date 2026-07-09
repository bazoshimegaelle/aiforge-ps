import os
from datetime import date
from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()

weekly_agent = Agent(
    name="AIFORGE-PS Weekly Report Agent",
    instructions="""
You create weekly executive cybersecurity reports from daily AI cyber threat updates.

Your report should be clear for public-sector leaders and useful for cybersecurity analysts.

Do not recommend offensive cyber actions.
""",
)

def read_daily_updates():
    folder = "daily_updates"

    if not os.path.exists(folder):
        return ""

    updates = []

    for filename in sorted(os.listdir(folder)):
        if filename.endswith(".md"):
            path = os.path.join(folder, filename)
            with open(path, "r", encoding="utf-8") as file:
                updates.append(f"\n\n--- {filename} ---\n")
                updates.append(file.read())

    return "\n".join(updates)

def main():
    updates = read_daily_updates()

    if not updates.strip():
        print("No daily updates found.")
        return

    prompt = f"""
Create a weekly AI cybersecurity briefing based on these daily updates:

{updates}

Weekly report format:
1. Executive summary
2. Top AI cyber threats this week
3. Public-sector impact
4. Evidence trends
5. Risk assessment
6. Defensive recommendations
7. Sources
"""

    result = Runner.run_sync(weekly_agent, prompt)

    os.makedirs("weekly_reports", exist_ok=True)

    filename = f"weekly_reports/{date.today().isoformat()}_weekly_report.md"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(result.final_output)

    print(f"Weekly report saved to: {filename}")

if __name__ == "__main__":
    main()