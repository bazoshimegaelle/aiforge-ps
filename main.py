import os
from datetime import datetime
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
# AIFORGE-PS Research Agent
# ---------------------------------------------------
research_agent = Agent(
    name="AIFORGE-PS Research Agent",

    instructions="""
You are the AIFORGE-PS AI Security Research Agent.

Mission:
Research emerging AI cybersecurity threats affecting public-sector organizations.

Responsibilities:

• Search for current, reliable information.
• Summarize findings clearly.
• Compare multiple trusted sources.
• Explain why each threat matters.
• Recommend defensive actions.
• Never recommend offensive cyber activities.
• Never modify systems.
• Never execute external actions.
• Keep the human analyst in control.

APA citation and source rules:

• Use credible sources such as CISA, NIST, MITRE, Microsoft, Google, OpenAI, FBI IC3, NSA, ENISA, and reputable cybersecurity research organizations.
• In the body of the report, do not hyperlink phrases or sentences.
• In the body of the report, cite sources only with APA-style in-text citations, such as (CISA, 2026) or (Microsoft, 2025).
• Put clickable URLs only in the References section.
• Format the References section in APA-style as much as possible.
• Each reference must include organization/author, year or full date if available, title, publisher if different from author, and URL.
• Do not list vague references such as "CISA" or "NIST" without a full citation and URL.

Reference format examples:

Cybersecurity and Infrastructure Security Agency. (2026). Title of report or webpage. https://www.cisa.gov/example
National Institute of Standards and Technology. (2025). Title of report or webpage. https://www.nist.gov/example
Microsoft. (2025). Title of report or webpage. https://www.microsoft.com/example

Always structure reports using:

1. Report Metadata
   - Topic
   - Generated on
   - Analyst note

2. Executive Summary

3. Threat Overview

4. Key Findings
   - Each major finding should include an APA-style in-text citation.

5. Evidence to Collect
   - Identity logs
   - Endpoint logs
   - Network logs
   - Cloud/SaaS logs
   - AI application logs

6. Risk Assessment

7. Defensive Recommendations

8. References
   - APA-style references with URLs only here.
""",

    tools=[
        WebSearchTool()
    ]
)

# ---------------------------------------------------
# Main Function
# ---------------------------------------------------
def main():

    print("=" * 65)
    print("AIFORGE-PS AI Security Research Agent")
    print("=" * 65)

    topic = input("\nResearch Topic: ").strip()

    if not topic:
        print("No research topic entered. Please run the program again and enter a topic.")
        return

    generated_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    prompt = f"""
Research the following cybersecurity topic.

Topic:
{topic}

Generated on:
{generated_on}

Generate an executive cybersecurity briefing for public-sector cybersecurity leaders and analysts.

Requirements:

• Use current and credible sources.
• Use APA-style in-text citations in the body, such as (CISA, 2026).
• Do not hyperlink phrases or sentences in the body of the report.
• Put URLs only in the References section.
• Format the References section using APA-style citations with URLs.
• Connect important findings to the sources that support them.
• Keep recommendations defensive, practical, and human-supervised.
• Do not include offensive cyber instructions.

Report format:

1. Report Metadata
   - Topic
   - Generated on
   - Analyst note

2. Executive Summary

3. Threat Overview

4. Key Findings

5. Evidence to Collect
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
        result = Runner.run_sync(
            research_agent,
            prompt
        )
    except Exception as error:
        print("\nThe research agent could not complete the request.")
        print(f"Error: {error}")
        return

    processed_report = process_report(result.final_output)

    os.makedirs("reports", exist_ok=True)

    report_path = os.path.join(
        "reports",
        "briefing.md"
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(processed_report)

    print("\n")
    print("=" * 65)
    print(processed_report)
    print("=" * 65)

    print(f"\nReport saved to: {report_path}")

# ---------------------------------------------------
# Entry Point
# ---------------------------------------------------
if __name__ == "__main__":
    main()
