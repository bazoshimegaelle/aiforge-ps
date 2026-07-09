import os
from datetime import datetime
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

Source and citation rules:

• Use credible sources such as CISA, NIST, MITRE, Microsoft, Google, OpenAI, FBI IC3, NSA, ENISA, and reputable cybersecurity research organizations.
• Include clickable Markdown links for every source.
• Include the organization name, article/report title, publication date when available, and URL.
• Tie important findings to specific sources.
• Do not list vague sources such as "CISA" or "NIST" without a link.

Always structure reports using:

1. Report Metadata
   - Topic
   - Generated on
   - Analyst note

2. Executive Summary

3. Threat Overview

4. Key Findings
   - Each major finding should mention the supporting source.

5. Evidence to Collect
   - Identity logs
   - Endpoint logs
   - Network logs
   - Cloud/SaaS logs
   - AI application logs

6. Risk Assessment

7. Defensive Recommendations

8. References
   - Use this format:
     - [Organization – Title](https://example.com) — Publication date if available.
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
• Include clickable Markdown links in the References section.
• Do not provide vague source names without URLs.
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
   - Format every source as a clickable Markdown link.
   - Example: [CISA – AI Security Guidance](https://www.cisa.gov/) — Publication date if available.
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

        file.write(result.final_output)

    print("\n")
    print("=" * 65)
    print(result.final_output)
    print("=" * 65)

    print(f"\nReport saved to: {report_path}")

# ---------------------------------------------------
# Entry Point
# ---------------------------------------------------
if __name__ == "__main__":
    main()
