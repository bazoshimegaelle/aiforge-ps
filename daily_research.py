import os
from datetime import date, datetime
from dotenv import load_dotenv
from agents import Agent, Runner, WebSearchTool

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

Source and citation rules:

- Use current and credible sources.
- Prioritize sources such as CISA, NIST, MITRE, Microsoft, Google, OpenAI, FBI IC3, NSA, ENISA, and reputable cybersecurity research organizations.
- Include clickable Markdown links for every source.
- Include the organization name, article/report title, publication date when available, and URL.
- Tie important findings to specific sources.
- Do not list vague sources such as "CISA" or "NIST" without a link.

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
   - Each threat should mention the supporting source.

4. Public-Sector Impact

5. Evidence to Monitor
   - Identity logs
   - Endpoint logs
   - Network logs
   - Cloud/SaaS logs
   - AI application logs

6. Defensive Recommendations

7. References
   - Use this format:
     - [Organization – Title](https://example.com) — Publication date if available.
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
- Include clickable Markdown links in the References section.
- Do not provide vague source names without URLs.
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
   - Format every source as a clickable Markdown link.
   - Example: [CISA – AI Security Guidance](https://www.cisa.gov/) — Publication date if available.
"""

    try:
        result = Runner.run_sync(daily_agent, prompt)
    except Exception as error:
        print("\nThe daily research agent could not complete the request.")
        print(f"Error: {error}")
        return

    os.makedirs("daily_updates", exist_ok=True)

    filename = f"daily_updates/{report_date}_daily_update.md"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(result.final_output)

    print(f"Daily update saved to: {filename}")

# ---------------------------------------------------
# Entry Point
# ---------------------------------------------------
if __name__ == "__main__":
    main()
