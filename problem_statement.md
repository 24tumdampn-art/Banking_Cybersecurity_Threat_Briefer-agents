# Problem Statement

## Project Name
Banking Cybersecurity Threat Briefer

## The Problem
Banks face constant cyber threats including fraud, phishing, 
ransomware, SWIFT attacks, and ATM skimming. Security analysts 
currently spend hours manually researching threats, identifying 
vulnerabilities, and writing compliance reports.

## User
Bank security officers, IT teams, and compliance managers at 
financial institutions.

## Need
An automated system that instantly generates a real-time structured 
cybersecurity threat briefing for the banking sector — including 
active threats, CVEs, mitigation steps, and compliance gaps 
against RBI and PCI-DSS standards.

## Why Agentic
This problem requires multiple sequential reasoning steps:
- Searching live internet data (Tavily)
- Analysing vulnerabilities (Gemini/Groq)
- Writing a professional report (Gemini/Groq)
- Evaluating output quality (LLM-as-Judge)
- Checking compliance rules (RBI + PCI-DSS)

No single AI call can perform all these steps. Each step depends 
on the output of the previous one. Only an agentic architecture 
where agents act autonomously and sequentially can solve this 
problem end-to-end.
