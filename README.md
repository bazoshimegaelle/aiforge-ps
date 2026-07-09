# aiforge-ps
Agentic AI framework for AI threat intelligence, digital forensics, incident reconstruction, and decision support for public-sector cybersecurity.
# AIFORGE-PS

**AI Forensics, Governance, and Research Engine for Public Sector**

AIFORGE-PS is an **agentic AI framework** under development that assists public-sector cybersecurity teams with AI threat research, digital forensics, incident reconstruction, evidence correlation, risk assessment, and executive decision support.

> **Status:** 🚧 Active Development

---

# Vision

Artificial Intelligence is rapidly transforming how organizations operate, but it also introduces new cybersecurity challenges such as:

- Agentic AI attacks
- Prompt injection
- Shadow AI
- AI supply-chain attacks
- Data leakage
- Model abuse
- Autonomous agent misuse

AIFORGE-PS aims to help cybersecurity professionals investigate these threats using specialized AI agents while maintaining **human oversight**.

---

# Current Features

✅ AI Security Research Agent

- Researches emerging AI cybersecurity threats
- Searches trusted public sources
- Produces executive cybersecurity briefings
- Generates Markdown reports
- Supports public-sector cybersecurity analysis

---

# Planned Architecture

```text
Mission Planner
        │
        ▼
Research Agent
        │
        ▼
Threat Intelligence Agent
        │
        ▼
AI Forensics Agent
        │
        ▼
Shadow AI Detection Agent
        │
        ▼
Risk Assessment Engine
        │
        ▼
FRCS Confidence Engine
        │
        ▼
Compliance Agent
        │
        ▼
Executive Report Generator
```

---

# Project Structure

```text
aiforge-ps/
│
├── agents/
├── scoring/
├── prompts/
├── reports/
├── daily_updates/
├── weekly_reports/
├── tests/
├── docs/
│
├── main.py
├── daily_research.py
├── weekly_report.py
├── requirements.txt
└── .env
```

---

# Current Capabilities

The current version can:

- Research AI cybersecurity threats
- Produce daily intelligence updates
- Generate weekly executive reports
- Search trusted public sources
- Save reports automatically

---

# Planned Features

- Threat Intelligence Agent
- Digital Forensics Agent
- Shadow AI Detection
- AI Governance Agent
- Compliance Mapping
- MITRE ATT&CK Integration
- MITRE ATLAS Integration
- NIST AI RMF Mapping
- FRCS (Forensic Reconstruction Confidence Score)
- Executive Dashboard
- Microsoft Word reports
- PDF reports
- PowerPoint briefings

---

# Technologies

- Python
- OpenAI Agents SDK
- OpenAI Responses API
- Web Search Tool
- Markdown
- Git
- GitHub

---


# Installation

## Clone the repository

```bash
git clone https://github.com/bazoshimegaelle/aiforge-ps.git
cd aiforge-ps
```

## Create a virtual environment

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure your API key

Copy the example environment file.

Windows

```bash
copy .env.example .env
```

Linux/macOS

```bash
cp .env.example .env
```

Open `.env` and replace:

```text
OPENAI_API_KEY=your_openai_api_key_here
```

with your own API key.

## Run the application

Interactive research:

```bash
python main.py
```

Daily intelligence report:

```bash
python daily_research.py
```

Weekly executive report:

```bash
python weekly_report.py
```

# Research Focus

This project investigates:

- AI Security
- Agentic AI
- Digital Forensics
- Incident Reconstruction
- Threat Intelligence
- AI Governance
- Public-Sector Cybersecurity
- Explainable AI
- Human-in-the-Loop Decision Support

---

# Roadmap

## Phase 1

- ✅ Research Agent
- ✅ Daily Updates
- ✅ Weekly Reports

## Phase 2

- Threat Intelligence Agent
- AI Forensics Agent
- Risk Engine

## Phase 3

- FRCS Engine
- Compliance Agent
- Executive Reports

## Phase 4

- Dashboard
- Multi-Agent Collaboration
- Production Deployment

---

# License

This repository is released under the MIT License.

---

# Author

**Gaelle Yeo Shime**

Master of Science in Cybersecurity Operations

University of Maryland Global Campus

GitHub: https://github.com/bazoshimegaelle

---

# Disclaimer

AIFORGE-PS is an active research and development project.

The framework is intended to support cybersecurity research, digital forensics, and public-sector cyber defense.

It does **not** perform offensive cybersecurity activities and is designed to keep human analysts in control of operational decisions.
