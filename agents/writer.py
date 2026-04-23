from groq import Groq
import os

def run_writer(research: str, vulnerabilities: str) -> str:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""You are a Banking Cybersecurity Briefing Writer.
Write a professional threat briefing for a bank's security team.

Research findings:
{research}

Vulnerability analysis:
{vulnerabilities}

Structure the briefing exactly like this:

## Executive Summary
(2-3 sentences on current banking threat landscape)

## Overall Risk Level
(CRITICAL / HIGH / MEDIUM with one line justification)

## Active Threats
For each of 3-4 threats:
- Threat name
- Description (2 sentences, banking specific)
- Severity: [CRITICAL] / [HIGH] / [MEDIUM]
- Recent activity or known threat actor

## Key Vulnerabilities
(from the analysis, keep it concise)

## Mitigation Steps
5 specific actionable steps a bank security team can take immediately.

Be direct, technical, and banking specific."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
