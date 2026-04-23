from groq import Groq
import os
import json
import re

RUBRIC = """
You are an expert cybersecurity evaluator assessing a banking threat briefing.
Score on these 4 criteria (0-10 each):

1. Accuracy: Are the threats real, current, and relevant to banking?
2. Completeness: Does it cover threats, vulnerabilities, and mitigations fully?
3. Actionability: Are mitigation steps specific enough for a bank security team?
4. Banking Relevance: Does it address banking systems like SWIFT, UPI, ATMs, mobile banking?

Return ONLY valid JSON, no extra text, no markdown:
{
  "accuracy": <score>,
  "completeness": <score>,
  "actionability": <score>,
  "banking_relevance": <score>,
  "overall": <average of the 4 scores>,
  "feedback": "<one sentence summary>",
  "grade": "<A/B/C/D based on overall score>"
}
"""

def run_judge(briefing: str) -> dict:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"{RUBRIC}\n\nBriefing to evaluate:\n{briefing}"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        return json.loads(match.group())

    return {
        "accuracy": 0,
        "completeness": 0,
        "actionability": 0,
        "banking_relevance": 0,
        "overall": 0,
        "feedback": "Could not parse judge response",
        "grade": "F"
    }
