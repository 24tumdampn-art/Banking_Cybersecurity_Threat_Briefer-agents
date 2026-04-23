# Task Decomposition & Specifications

## Agent 1 — Threat Researcher
- Input: Nothing (starts automatically)
- Action: Calls Tavily Search API with 4 banking queries
- Output: Raw text of live threat news articles
- Tool Used: Tavily Search API

## Agent 2 — Vulnerability Analyst
- Input: Raw research text from Agent 1
- Action: Sends to Groq LLM, asks for top 4 CVEs
- Output: Numbered list of vulnerabilities with severity
- Decision Point: If research is empty, returns error message

## Agent 3 — Briefing Writer
- Input: Research from Agent 1 + Vulnerabilities from Agent 2
- Action: Sends both to Groq LLM to write structured report
- Output: Full professional threat briefing document
- Format: Executive Summary, Risk Level, Threats, Mitigations

## Agent 4 — LLM-as-Judge
- Input: Full briefing from Agent 3
- Action: Groq LLM scores on 4 criteria using rubric
- Output: JSON with scores 0-10 + grade A/B/C/D + feedback
- Rubric: Accuracy, Completeness, Actionability, Banking Relevance

## Agent 5 — Compliance Checker
- Input: Full briefing from Agent 3
- Action: Maps threats against hardcoded RBI and PCI-DSS controls
- Output: JSON with at-risk controls, compliant controls, scores
- Decision Point: Flags which regulatory controls need attention
