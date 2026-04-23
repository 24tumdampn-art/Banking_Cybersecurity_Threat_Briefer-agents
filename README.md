# 🏦 Banking Cybersecurity Threat Briefer

A multi-agent AI system that automatically generates real-time 
cybersecurity threat briefings for banks and financial institutions.

## 🚀 Live Demo
[Click here to open the app]
Local URL: http://localhost:8501
Network URL: http://192.168.43.154:8501

## 🤖 How It Works
5 AI agents run in sequence automatically:
1. 🔍 Threat Researcher — searches live banking threats via Tavily
2. 🛡️ Vulnerability Analyst — identifies CVEs and attack vectors
3. 📋 Briefing Writer — writes a professional threat report
4. ⚖️ LLM-as-Judge — scores the report quality out of 10
5. ✅ Compliance Checker — checks RBI and PCI-DSS compliance gaps

## 🛠️ Tech Stack
- Python
- Streamlit
- Groq API (Llama 3.3 70B)
- Tavily Search API
- Plotly

## ⚙️ Run Locally

1. Clone the repo
   git clone https://github.com/YOUR_USERNAME/banking-threat-briefer

2. Install dependencies
   pip install -r requirements.txt

3. Create .env file
   GROQ_API_KEY=your_key_here
   TAVILY_API_KEY=your_key_here

4. Run the app
   streamlit run app.py

## 📁 Project Structure
banking-threat-briefer/
├── app.py                  # Main UI and agent orchestration
├── agents/
│   ├── researcher.py       # Agent 1 — Tavily live search
│   ├── analyst.py          # Agent 2 — CVE identification
│   ├── writer.py           # Agent 3 — Report generation
│   ├── judge.py            # Agent 4 — LLM-as-Judge scoring
│   └── compliance.py       # Agent 5 — RBI + PCI-DSS checker
├── requirements.txt
└── Procfile

## 👥 Team
- Role A (Architect) — Problem definition, architecture, API integrations
- Role B (Builder) — Implementation, UI, deployment

## 📚 Course
Semester IV · B.E. Electronics & Communication
Introduction to Agentic AI Systems
