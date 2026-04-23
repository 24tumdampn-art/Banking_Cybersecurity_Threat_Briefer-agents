from groq import Groq
import os

def run_analyst(research_context: str) -> str:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""You are a Banking Vulnerability Analyst.
Based on the threat research below, identify the top 4 vulnerabilities 
specifically targeting banks and financial institutions.

Research:
{research_context}

For each vulnerability provide:
- Vulnerability name
- CVE number (if known)
- Severity: Critical / High / Medium
- Attack vector (e.g. phishing email, API exploit, insider threat)
- Which banking system is at risk (e.g. core banking, mobile app, ATM, SWIFT)

Format as a numbered list."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
