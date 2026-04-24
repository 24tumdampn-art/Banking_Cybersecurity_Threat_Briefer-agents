<img width="1919" height="973" alt="Screenshot 2026-04-24 190555" src="https://github.com/user-attachments/assets/05e16b8a-bbb3-42b4-af5b-fa93c74c73a1" /># 🏦 Banking Cybersecurity Threat Briefer

A multi-agent AI system that automatically generates real-time
cybersecurity threat briefings for banks and financial institutions.
Click one button — 5 AI agents run automatically and produce a
full professional threat report in under 60 seconds.

---

## 🚀 Live Demo

App runs locally using Streamlit.
To run it yourself follow the steps in the Run Locally section below.

---

## 🎯 Problem Statement

Banks face constant cyber threats including fraud, phishing,
ransomware, SWIFT attacks, and ATM skimming. Security analysts
currently spend hours manually researching threats and writing
compliance reports.

This system reduces that to under 60 seconds using Agentic AI.

**Users:** Bank security officers, IT teams, compliance managers

---

## 🤖 How It Works

5 AI agents run in sequence automatically:

1. 🔍 **Threat Researcher** — searches live banking threats via Tavily
2. 🛡️ **Vulnerability Analyst** — identifies CVEs and attack vectors
3. 📋 **Briefing Writer** — writes a professional structured threat report
4. ⚖️ **LLM-as-Judge** — scores the report quality out of 10
5. ✅ **Compliance Checker** — checks RBI and PCI-DSS compliance gaps

Each agent passes its output to the next automatically.
No human involvement needed between steps.

---

## 📊 What The Output Includes

- Executive Summary with risk level — CRITICAL / HIGH / MEDIUM
- Active threats with CVE numbers and severity ratings
- 5 actionable mitigation steps for the security team
- LLM Judge score out of 10 — Accuracy, Completeness, Actionability
- RBI compliance score out of 100
- PCI-DSS compliance score out of 100
- Interactive charts — radar, bar, gauge, donut

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web UI framework |
| Groq API — Llama 3.3 70B | AI brain for Agents 2, 3, 4, 5 |
| Tavily Search API | Live internet search for Agent 1 |
| Plotly | Interactive graphs and charts |
| python-dotenv | Secure API key management |

---

## ⚙️ Run Locally

**Step 1 — Clone the repo**


## 🏗️ Architecture Diagram

![Architecture](<img width="1919" height="973" alt="Screenshot 2026-04-24 190555" src="https://github.com/user-attachments/assets/f8478634-b617-4d7d-a6e5-3d29f4b9e0d8" />
)

**Flow:**
User → Streamlit UI → Agent 1 (Tavily Search) → Agent 2 (Groq Analyst)
→ Agent 3 (Groq Writer) → Agent 4 (LLM Judge) → Agent 5 (Compliance) → Output
