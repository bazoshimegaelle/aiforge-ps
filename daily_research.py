import os
from datetime import date, datetime
from dotenv import load_dotenv
from agents import Agent, Runner, WebSearchTool
from citation_utils import process_report

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
# AIFORGE-PS Daily Research Agent
# ---------------------------------------------------
daily_agent = Agent(
    name="AIFORGE-PS Daily Research Agent",
    instructions="""
You are the AIFORGE-PS Daily Research Agent.

Mission:
Create a concise daily AI cybersecurity threat update for government and public-sector organizations.

Focus on:
- agentic AI threats
- shadow AI
- prompt injection
- AI data leakage
- AI forensics
- AI governance
- public-sector cyber risk

APA citation and source rules:

- Use current and credible sources.
- Prioritize sources such as CISA, NIST, MITRE, Microsoft, Google, OpenAI, FBI IC3, NSA, ENISA, and reputable cybersecurity research organizations.
- In the body of the report, do not hyperlink phrases or sentences.
- In the body of the report, cite sources only with APA-style in-text citations, such as (CISA, 2026) or (Microsoft, 2025).
- Put clickable URLs only in the References section.
- Format the References section in APA-style as much as possible.
- Each reference must include organization/author, year or full date if available, title, publisher if different from author, and URL.
- Do not list vague references such as "CISA" or "NIST" without a full citation and URL.

Reference format examples:

Cybersecurity and Infrastructure Security Agency. (2026). Title of report or webpage. https://www.cisa.gov/example
National Institute of Standards and Technology. (2025). Title of report or webpage. https://www.nist.gov/example
Microsoft. (2025). Title of report or webpage. https://www.microsoft.com/example

Safety rules:

- Do not recommend offensive cyber actions.
- Keep all recommendations defensive, practical, and human-supervised.

Report format:

1. Report Metadata
   - Report date
   - Generated on
   - Topic

2. Executive Summary

3. New or Emerging Threats
   - Each threat should include an APA-style in-text citation.

4. Public-Sector Impact

5. Evidence to Monitor
   - Identity logs
   - Endpoint logs
   - Network logs
   - Cloud/SaaS logs
   - AI application logs

6. Defensive Recommendations

7. References
   - APA-style references with URLs only here.
""",
    tools=[WebSearchTool()],
)

# ---------------------------------------------------
# Main Function
# ---------------------------------------------------
def main():
    topic = "Latest agentic AI cybersecurity threats affecting government agencies"
    report_date = date.today().isoformat()
    generated_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    prompt = f"""
Create today's daily AI cyber threat update.

Report date: {report_date}
Generated on: {generated_on}
Topic: {topic}

Requirements:

- Use current and credible sources.
- Use APA-style in-text citations in the body, such as (CISA, 2026).
- Do not hyperlink phrases or sentences in the body of the report.
- Put URLs only in the References section.
- Format the References section using APA-style citations with URLs.
- Connect important findings to the sources that support them.
- Keep recommendations defensive, practical, and human-supervised.
- Do not include offensive cyber instructions.

Format:

1. Report Metadata
   - Report date
   - Generated on
   - Topic

2. Executive Summary

3. New or Emerging Threats

4. Public-Sector Impact

5. Evidence to Monitor
   - Identity Logs
   - Endpoint Logs
   - Network Logs
   - Cloud/SaaS Logs
   - AI Application Logs

6. Defensive Recommendations

7. References
   - Use APA-style references.
   - Include URLs only in this section.
   - Example: Cybersecurity and Infrastructure Security Agency. (2026). Title of report. https://www.cisa.gov/example
"""

    try:
        result = Runner.run_sync(daily_agent, prompt)
    except Exception as error:
        print("\nThe daily research agent could not complete the request.")
        print(f"Error: {error}")
        return

    processed_report = process_report(result.final_output)

    os.makedirs("daily_updates", exist_ok=True)

    filename = f"daily_updates/{report_date}_daily_update.md"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(processed_report)

    print(f"Daily update saved to: {filename}")

# ---------------------------------------------------
# Entry Point
# ---------------------------------------------------
if __name__ == "__main__":
    main()
