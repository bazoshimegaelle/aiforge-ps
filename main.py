import os
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
        "Please add it to your .env file."
    )

# ---------------------------------------------------
# AIFORGE-PS Research Agent
# ---------------------------------------------------
research_agent = Agent(
    name="AIFORGE-PS Research Agent",

    instructions="""
You are the AIFORGE-PS AI Security Research Agent.

Mission:
Research emerging AI cybersecurity threats affecting
public-sector organizations.

Responsibilities:

• Search for current information.
• Summarize findings.
• Compare multiple trusted sources.
• Explain why each threat matters.
• Recommend defensive actions.
• Never recommend offensive cyber activities.
• Never modify systems.
• Never execute external actions.
• Keep the human analyst in control.

Always structure reports using:

1. Executive Summary

2. Threat Overview

3. Key Findings

4. Evidence to Collect

5. Risk Assessment

6. Defensive Recommendations

7. References
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

    topic = input("\nResearch Topic: ")

    prompt = f"""
Research the following cybersecurity topic.

Topic:
{topic}

Generate an executive cybersecurity briefing.

Include:

• Executive Summary

• Threat Overview

• Key Findings

• Evidence to Collect
    - Identity Logs
    - Endpoint Logs
    - Network Logs
    - Cloud/SaaS Logs
    - AI Application Logs

• Risk Assessment

• Defensive Recommendations

• References
"""

    result = Runner.run_sync(
        research_agent,
        prompt
    )

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