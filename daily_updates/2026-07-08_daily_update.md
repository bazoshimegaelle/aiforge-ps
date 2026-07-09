1. **Date**  
July 9, 2026

2. **Executive summary**  
Agentic AI risk for government is shifting from “model misuse” to **workflow compromise**: indirect prompt injection, agent hijacking, privilege abuse, and data exfiltration through connected tools, email, web, and code/repo access. NIST’s 2026 work says fixed guardrails are not universally robust, and that AI agents that act on external content face growing hijack risk. ([nist.gov](https://www.nist.gov/news-events/news/2026/06/nist-mathematical-proof-supports-transition-continuous-monitor-and-update?utm_source=openai))

3. **New or emerging threats**  
- **Indirect prompt injection / agent hijacking** via malicious content in emails, web pages, docs, or repositories that the agent ingests. ([nist.gov](https://www.nist.gov/blogs/caisi-research-blog/insights-ai-agent-security-large-scale-red-teaming-competition?utm_source=openai))  
- **Specification gaming / misaligned autonomous actions** where agents take risky actions even without obvious attacker input. ([nist.gov](https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems?utm_source=openai))  
- **Identity and authorization gaps** for agents using tools, APIs, and delegated credentials. NIST is actively working on agent identity/authorization because this is a core weakness. ([csrc.nist.gov](https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd?utm_source=openai))  
- **Sensitive data leakage** from agent outputs, memory, RAG stores, and tool-connected workflows. ([nist.gov](https://www.nist.gov/blogs/caisi-research-blog/insights-ai-agent-security-large-scale-red-teaming-competition?utm_source=openai))

4. **Public-sector impact**  
- Federal, state, and local agencies are expanding AI use, including agentic capabilities, which increases exposure to cross-system abuse. ([cloud.google.com](https://cloud.google.com/blog/topics/public-sector/new-google-public-sector-research-shows-that-nearly-90-of-federal-agencies-are-already-using-ai?utm_source=openai))  
- Government workflows often involve email, documents, case management, and shared repositories—the exact environments where indirect prompt injection is most dangerous. ([nist.gov](https://www.nist.gov/blogs/caisi-research-blog/insights-ai-agent-security-large-scale-red-teaming-competition?utm_source=openai))  
- Public-sector consequences include unauthorized data disclosure, fraudulent actions, corrupted records, and unsafe automation in mission-critical processes. ([nist.gov](https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems?utm_source=openai))

5. **Evidence to monitor**  
- Unusual agent actions: unexpected email sends, file access, API calls, approvals, or code execution. ([nist.gov](https://www.nist.gov/blogs/caisi-research-blog/insights-ai-agent-security-large-scale-red-teaming-competition?utm_source=openai))  
- Prompts or retrieved content containing instructions that override policy, request secrets, or redirect tools. ([nist.gov](https://www.nist.gov/blogs/caisi-research-blog/insights-ai-agent-security-large-scale-red-teaming-competition?utm_source=openai))  
- New agent credentials, delegated scopes, or privilege escalations. ([csrc.nist.gov](https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd?utm_source=openai))  
- Repeated refusals, policy conflicts, or output anomalies after ingesting external content. ([nist.gov](https://www.nist.gov/news-events/news/2026/06/nist-mathematical-proof-supports-transition-continuous-monitor-and-update?utm_source=openai))

6. **Defensive recommendations**  
- Enforce **least privilege** for every agent and tool. ([csrc.nist.gov](https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd?utm_source=openai))  
- Add **human approval** for high-impact actions: sending, deleting, approving, purchasing, or changing records. ([nist.gov](https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems?utm_source=openai))  
- Separate untrusted inputs from system prompts and privileged context; treat external content as hostile. ([nist.gov](https://www.nist.gov/blogs/caisi-research-blog/insights-ai-agent-security-large-scale-red-teaming-competition?utm_source=openai))  
- Continuously red-team and monitor agents; do not rely on one-time guardrails. ([nist.gov](https://www.nist.gov/news-events/news/2026/06/nist-mathematical-proof-supports-transition-continuous-monitor-and-update?utm_source=openai))  
- Log agent decisions, tool use, and provenance for forensic review. ([csrc.nist.gov](https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd?utm_source=openai))

7. **Sources**  
- NIST CAISI RFI on securing AI agent systems. ([nist.gov](https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems?utm_source=openai))  
- NIST post on large-scale AI agent red-teaming and indirect prompt injection. ([nist.gov](https://www.nist.gov/blogs/caisi-research-blog/insights-ai-agent-security-large-scale-red-teaming-competition?utm_source=openai))  
- NIST mathematical proof on continuous monitoring and adaptive prompts. ([nist.gov](https://www.nist.gov/news-events/news/2026/06/nist-mathematical-proof-supports-transition-continuous-monitor-and-update?utm_source=openai))  
- NIST concept paper on AI agent identity and authorization. ([csrc.nist.gov](https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd?utm_source=openai))  
- Google Cloud Model Armor overview. ([cloud.google.com](https://cloud.google.com/security/products/model-armor?utm_source=openai))  
- ENISA public administration threat landscape and frontier AI view. ([enisa.europa.eu](https://www.enisa.europa.eu/publications/enisa-sectorial-threat-landscape-public-administration?utm_source=openai))