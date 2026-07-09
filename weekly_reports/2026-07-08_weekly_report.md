## 1. Executive summary
This week’s AI security updates show a shift from simple model misuse to **workflow compromise** in agentic AI. The main risks for government are indirect prompt injection, agent hijacking, privilege abuse, and data leakage through connected tools such as email, web, documents, code repositories, and APIs. NIST’s current work reinforces that fixed guardrails are not enough for all environments and that AI agents handling external content face increasing hijack risk.

## 2. Top AI cyber threats this week
- **Indirect prompt injection** through malicious instructions hidden in emails, web pages, documents, or repositories.
- **Agent hijacking** where external content causes an agent to take attacker-influenced actions.
- **Specification gaming / misaligned behavior** where autonomous agents take risky actions without direct attacker input.
- **Identity and authorization weaknesses** in agent-to-tool access, delegated credentials, and API permissions.
- **Sensitive data leakage** through outputs, memory, retrieval stores, logs, and connected workflows.

## 3. Public-sector impact
- Federal, state, and local agencies are rapidly adopting AI, including agentic functions, increasing exposure across systems.
- Government workflows heavily depend on email, shared documents, case management, and repositories—the exact channels most vulnerable to indirect prompt injection.
- Likely consequences include unauthorized disclosure, fraudulent actions, corrupted records, and unsafe automation in mission-critical processes.

## 4. Evidence trends
Watch for:
- Unexpected agent actions: email sends, file access, API calls, approvals, or code execution.
- Content that tries to override policy, request secrets, or redirect tools.
- New agent credentials, broader delegated scopes, or privilege changes.
- Repeated refusals, conflicting policy behavior, or unusual output after ingesting external content.

## 5. Risk assessment
**Overall risk: High** for public-sector environments using connected or agentic AI.

Why:
- Attack paths are now aimed at the **surrounding workflow**, not just the model.
- Government systems combine high-value data with many externally supplied inputs.
- Weak identity, authorization, and monitoring controls can let a compromised agent act with real authority.

## 6. Defensive recommendations
- Enforce **least privilege** for all agents and connected tools.
- Require **human approval** for high-impact actions such as sending, deleting, approving, purchasing, or changing records.
- Treat all external content as hostile; separate it from system prompts and privileged context.
- Continuously red-team and monitor agent behavior; do not rely on one-time guardrails.
- Log agent decisions, tool use, and provenance for later review and investigation.

## 7. Sources
- NIST CAISI RFI on securing AI agent systems
- NIST research on large-scale AI agent red-teaming and indirect prompt injection
- NIST mathematical proof on continuous monitoring and adaptive prompts
- NIST concept paper on AI agent identity and authorization
- Google Cloud Model Armor overview
- ENISA public administration threat landscape and frontier AI view