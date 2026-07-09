## 1. Executive Summary

Agentic AI is becoming a real security concern for government agencies because these systems can **take actions**, not just generate text. That expands the attack surface from prompt abuse to **identity abuse, tool misuse, memory poisoning, supply-chain compromise, and unintended code execution**. NIST’s 2026 work on AI agents explicitly highlights the need for secure identity/authorization, while OWASP’s 2025–2026 agentic guidance shows the most likely failure modes in production agent systems. ([nist.gov](https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure?utm_source=openai))

For public-sector environments, the main risk is not “AI answers a question wrong,” but “AI agent is tricked into doing the wrong thing with valid credentials.” That can lead to unauthorized email actions, data exposure, fraudulent approvals, cloud misconfiguration, or lateral movement through trusted integrations. ([nist.gov](https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems?utm_source=openai))

## 2. Threat Overview

Key current threat classes include:

- **Prompt injection / indirect prompt injection** against agents that consume untrusted content. ([owasp.org](https://owasp.org/www-community/attacks/PromptInjection?utm_source=openai))
- **Excessive agency / over-privileged tools** where an agent has more access than needed. ([owasp.org](https://owasp.org/www-project-agentic-skills-top-10/top10?utm_source=openai))
- **Identity and authority abuse** when agent credentials, tokens, or delegated permissions are stolen or over-scoped. ([nist.gov](https://www.nist.gov/news-events/news/2026/02/new-concept-paper-identity-and-authority-software-agents?utm_source=openai))
- **Tool and MCP abuse** where an attacker leverages agent-connected tools, plugins, or protocols to issue commands or actions. ([owasp.org](https://owasp.org/www-project-mcp-top-10/?utm_source=openai))
- **Memory/context poisoning** where malicious content is stored and later reused by the agent. ([genai.owasp.org](https://genai.owasp.org/download/52117/?tmstv=1765059207&utm_source=openai))
- **Supply-chain compromise** of agent skills, connectors, or dependencies. ([owasp.org](https://owasp.org/www-project-agentic-skills-top-10/?utm_source=openai))

## 3. Key Findings

1. **Government agencies should treat AI agents as privileged software identities.** NIST is now focused on agent identity and authorization because agents can act on behalf of users across systems. ([nist.gov](https://www.nist.gov/news-events/news/2026/02/new-concept-paper-identity-and-authority-software-agents?utm_source=openai))

2. **Agentic attacks are materially different from classic LLM abuse.** The danger is not only bad output, but unsafe actions taken through APIs, email, calendars, ticketing systems, or cloud consoles. ([nist.gov](https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems?utm_source=openai))

3. **Prompt injection remains a top entry point.** OWASP continues to emphasize injection as a practical path to override agent instructions and misuse tools. ([owasp.org](https://owasp.org/www-community/attacks/PromptInjection?utm_source=openai))

4. **Over-privilege is a major blast-radius multiplier.** If an agent can approve, send, delete, provision, or exfiltrate, one successful compromise can become an enterprise incident. ([owasp.org](https://owasp.org/www-project-agentic-skills-top-10/top10?utm_source=openai))

5. **Security monitoring must extend into AI application logs.** Traditional SIEM visibility is necessary but insufficient; agent traces, tool calls, memory writes, and policy decisions matter. This is consistent with NIST’s focus on continuous monitoring and update for AI security. ([nist.gov](https://www.nist.gov/news-events/news/2026/06/nist-mathematical-proof-supports-transition-continuous-monitor-and-update?utm_source=openai))

## 4. Evidence to Collect

### Identity Logs
- Agent service accounts, OAuth app logs, SSO/MFA events
- Token issuance, refresh, revocation
- Delegated consent and admin grants
- Privilege changes and role assignments
- Unusual cross-tenant or impossible-travel sign-ins ([nist.gov](https://www.nist.gov/news-events/news/2026/02/new-concept-paper-identity-and-authority-software-agents?utm_source=openai))

### Endpoint Logs
- EDR detections on admin workstations used to operate agents
- Browser/session activity for AI consoles and connectors
- Script execution, credential theft indicators
- Local agent runtime or desktop automation artifacts ([cisa.gov](https://www.cisa.gov/topics/cybersecurity-best-practices/executive-order-improving-nations-cybersecurity?utm_source=openai))

### Network Logs
- Egress to unfamiliar model/API endpoints
- Suspicious DNS, proxy, or TLS patterns
- Lateral movement from agent hosts
- Repeated tool-calling bursts or exfiltration-sized transfers ([nist.gov](https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems?utm_source=openai))

### Cloud/SaaS Logs
- Cloud audit logs for mailbox, file, ticketing, and IAM actions
- API calls made by agent identities
- Data access spikes, sharing changes, mailbox rules, forwarding
- New connectors, integrations, or app registrations ([nist.gov](https://www.nist.gov/news-events/news/2026/02/new-concept-paper-identity-and-authority-software-agents?utm_source=openai))

### AI Application Logs
- Prompts, system instructions, retrieved context, and agent traces
- Tool selections, arguments, approvals, and refusals
- Memory writes/reads and context window events
- Policy-violation events, jailbreak attempts, and retrieval-source provenance ([nist.gov](https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems?utm_source=openai))

## 5. Risk Assessment

**Overall risk: High.**  
For government agencies, agentic AI increases the likelihood of **authorized misuse** and **silent automation-driven compromise**. The most likely impacts are unauthorized data access, fraud, workflow manipulation, and misconfiguration. The highest-impact scenarios involve privileged agents connected to email, identity, cloud administration, procurement, or case-management systems. ([nist.gov](https://www.nist.gov/news-events/news/2026/02/new-concept-paper-identity-and-authority-software-agents?utm_source=openai))

**Most exposed environments**
- Agencies using AI agents for document handling, email, scheduling, or help desk automation
- Environments with broad SaaS/API permissions
- Shared or loosely governed agent skill catalogs and connectors ([owasp.org](https://owasp.org/www-project-agentic-skills-top-10/?utm_source=openai))

## 6. Defensive Recommendations

- **Minimize agent privileges**; use least privilege and short-lived tokens. ([nist.gov](https://www.nist.gov/news-events/news/2026/02/new-concept-paper-identity-and-authority-software-agents?utm_source=openai))
- **Require approval gates for high-risk actions** such as sending, deleting, purchasing, provisioning, or sharing data. ([owasp.org](https://owasp.org/www-project-agentic-skills-top-10/top10?utm_source=openai))
- **Separate identity for the agent from the user.** Do not let the agent inherit broad human privileges by default. ([nist.gov](https://www.nist.gov/news-events/news/2026/02/new-concept-paper-identity-and-authority-software-agents?utm_source=openai))
- **Harden against prompt injection** by isolating untrusted content, constraining tool use, and validating outputs before execution. ([owasp.org](https://owasp.org/www-community/attacks/PromptInjection?utm_source=openai))
- **Inventory all agents, tools, skills, and connectors** with owners, scopes, and revocation paths. ([owasp.org](https://owasp.org/www-project-agentic-skills-top-10/?utm_source=openai))
- **Log agent decisions and tool calls** centrally and make them searchable in SIEM. ([nist.gov](https://www.nist.gov/itl/applied-cybersecurity/cybersecurity-privacy-and-ai?utm_source=openai))
- **Continuously test with red-team style defensive exercises** focused on injection, memory poisoning, and privilege misuse. ([nist.gov](https://www.nist.gov/news-events/news/2024/01/nist-identifies-types-cyberattacks-manipulate-behavior-ai-systems?utm_source=openai))
- **Adopt NIST AI RMF / AI-agent guidance** and align with CISA collaboration and zero-trust practices. ([nist.gov](https://www.nist.gov/itl/ai-risk-management-framework?utm_source=openai))

## 7. References

- NIST: AI Agent Standards Initiative. ([nist.gov](https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure?utm_source=openai))
- NIST: Concept paper on identity and authority of software agents. ([nist.gov](https://www.nist.gov/news-events/news/2026/02/new-concept-paper-identity-and-authority-software-agents?utm_source=openai))
- NIST: RFI on securing AI agent systems. ([nist.gov](https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems?utm_source=openai))
- NIST: AI security and resilience research. ([nist.gov](https://www.nist.gov/artificial-intelligence/ai-research-security-and-resilience?utm_source=openai))
- NIST: AI Risk Management Framework. ([nist.gov](https://www.nist.gov/itl/ai-risk-management-framework?utm_source=openai))
- NIST: Adversarial Machine Learning taxonomy. ([nist.gov](https://www.nist.gov/news-events/news/2024/01/nist-identifies-types-cyberattacks-manipulate-behavior-ai-systems?utm_source=openai))
- OWASP: Agentic Applications Top 10 / Agentic Skills Top 10 / LLM Top 10. ([owasp.org](https://owasp.org/www-project-agentic-skills-top-10/top10?utm_source=openai))
- OWASP: Prompt Injection. ([owasp.org](https://owasp.org/www-community/attacks/PromptInjection?utm_source=openai))
- CISA: AI cybersecurity collaboration playbook and EO-related guidance. ([cisa.gov](https://www.cisa.gov/news-events/alerts/2025/01/14/cisa-releases-jcdc-ai-cybersecurity-collaboration-playbook-and-fact-sheet?utm_source=openai))

If you want, I can turn this into a **1-page PDF-style briefing** or a **slide-ready executive summary**.