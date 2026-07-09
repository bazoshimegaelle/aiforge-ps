import os
from datetime import date, datetime
from dotenv import load_dotenv
from agents import Agent, Runner

# ---------------------------------------------------
# Load environment variables
# ---------------------------------------------------
load_dotenv()

# Verify API Key
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError(
        "OPENAI_API_KEY was not found. "
        "Please create a .env file and add your API key like this: "
        "OPENAI_API_KEY=your_api_key_here"
    )

# ---------------------------------------------------
# AIFORGE-PS Weekly Report Agent
# ---------------------------------------------------
weekly_agent = Agent(
    name="AIFORGE-PS Weekly Report Agent",
    instructions="""
You are the AIFORGE-PS Weekly Report Agent.

Mission:
Create weekly executive AI cybersecurity reports from daily AI cyber threat updates.

Audience:
- public-sector cybersecurity leaders
- security analysts
- governance and risk teams
- digital forensics and incident response teams

Reporting rules:

- Be clear, concise, and executive-friendly.
- Identify patterns across the daily updates instead of simply repeating them.
- Highlight the most important AI cybersecurity risks for public-sector organizations.
- Tie important findings to specific sources already included in the daily updates when available.
- Preserve clickable Markdown links from the daily reports.
- Do not list vague sources such as "CISA" or "NIST" without a link if a link is available.

Safety rules:

- Do not recommend offensive cyber actions.
- Do not provide exploit instructions.
- Keep all recommendations defensive, practical, and human-supervised.

Report format:

1. Report Metadata
   - Report date
   - Generated on
   - Source period

2. Executive Summary

3. Top AI Cyber Threats This Week
   - Explain why each threat matters.
   - Mention supporting sources when available.

4. Public-Sector Impact

5. Evidence Trends
   - Identity logs
   - Endpoint logs
   - Network logs
   - Cloud/SaaS logs
   - AI application logs

6. Risk Assessment

7. Defensive Recommendations

8. References
   - Preserve clickable Markdown links from the source daily reports.
   - Use this format when adding or normalizing sources:
     - [Organization – Title](https://example.com) — Publication date if available.
""",
)

# ---------------------------------------------------
# Read Daily Updates
# ---------------------------------------------------
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

# ---------------------------------------------------
# Main Function
# ---------------------------------------------------
def main():
    updates = read_daily_updates()
    report_date = date.today().isoformat()
    generated_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not updates.strip():
        print("No daily updates found.")
        print("Run python daily_research.py first to create at least one daily update.")
        return

    prompt = f"""
Create a weekly AI cybersecurity briefing based on these daily updates.

Report date: {report_date}
Generated on: {generated_on}
Source period: Use the dates from the daily update filenames and report metadata.

Daily updates:

{updates}

Requirements:

- Summarize weekly patterns instead of only repeating each daily update.
- Preserve clickable Markdown links from the daily reports.
- Include source-backed findings whenever possible.
- Do not provide vague source names without URLs if URLs are available.
- Keep recommendations defensive, practical, and human-supervised.
- Do not include offensive cyber instructions.

Weekly report format:

1. Report Metadata
   - Report date
   - Generated on
   - Source period

2. Executive Summary

3. Top AI Cyber Threats This Week

4. Public-Sector Impact

5. Evidence Trends
   - Identity Logs
   - Endpoint Logs
   - Network Logs
   - Cloud/SaaS Logs
   - AI Application Logs

6. Risk Assessment

7. Defensive Recommendations

8. References
   - Preserve clickable Markdown links from the daily reports.
   - Format every source as a clickable Markdown link when possible.
   - Example: [CISA – AI Security Guidance](https://www.cisa.gov/) — Publication date if available.
"""

    try:
        result = Runner.run_sync(weekly_agent, prompt)
    except Exception as error:
        print("\nThe weekly report agent could not complete the request.")
        print(f"Error: {error}")
        return

    os.makedirs("weekly_reports", exist_ok=True)

    filename = f"weekly_reports/{report_date}_weekly_report.md"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(result.final_output)

    print(f"Weekly report saved to: {filename}")

# ---------------------------------------------------
# Entry Point
# ---------------------------------------------------
if __name__ == "__main__":
    main()
