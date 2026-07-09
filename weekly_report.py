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

APA citation and source rules:

- Be clear, concise, and executive-friendly.
- Identify patterns across the daily updates instead of simply repeating them.
- Highlight the most important AI cybersecurity risks for public-sector organizations.
- In the body of the report, do not hyperlink phrases or sentences.
- In the body of the report, cite sources only with APA-style in-text citations, such as (CISA, 2026) or (Microsoft, 2025).
- Put clickable URLs only in the References section.
- Format the References section in APA-style as much as possible.
- Each reference must include organization/author, year or full date if available, title, publisher if different from author, and URL.
- Do not list vague references such as "CISA" or "NIST" without a full citation and URL.
- When daily reports already contain references, preserve their URLs but normalize the references into APA style.
- Remove duplicate references when possible.

Reference format examples:

Cybersecurity and Infrastructure Security Agency. (2026). Title of report or webpage. https://www.cisa.gov/example
National Institute of Standards and Technology. (2025). Title of report or webpage. https://www.nist.gov/example
Microsoft. (2025). Title of report or webpage. https://www.microsoft.com/example

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
   - Include APA-style in-text citations.

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
   - APA-style references with URLs only here.
   - Sort references alphabetically when possible.
   - Remove duplicates when possible.
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
- Use APA-style in-text citations in the body, such as (CISA, 2026).
- Do not hyperlink phrases or sentences in the body of the report.
- Put URLs only in the References section.
- Format the References section using APA-style citations with URLs.
- Preserve source URLs from the daily reports when available.
- Remove duplicate references when possible.
- Sort references alphabetically when possible.
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
   - Use APA-style references.
   - Include URLs only in this section.
   - Example: Cybersecurity and Infrastructure Security Agency. (2026). Title of report. https://www.cisa.gov/example
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
