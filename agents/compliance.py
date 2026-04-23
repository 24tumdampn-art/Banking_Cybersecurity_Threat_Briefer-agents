from groq import Groq
import os
import json
import re

RBI_CONTROLS = [
    "Multi-factor authentication for all banking transactions",
    "End-to-end encryption for customer data at rest and in transit",
    "Real-time fraud detection and transaction monitoring system",
    "Regular vulnerability assessment and penetration testing (VAPT)",
    "Incident response plan tested within last 6 months",
    "Segregation of duties for critical banking operations",
    "Third-party vendor risk assessment program",
    "Customer awareness program for phishing and social engineering",
]

PCI_DSS_CONTROLS = [
    "Cardholder data environment (CDE) properly segmented",
    "Strong access control with least privilege principle enforced",
    "All cardholder data encrypted using AES-256 or equivalent",
    "Firewall and IDS/IPS protecting cardholder data",
    "Regular log monitoring and SIEM in place",
    "Patch management with critical patches applied within 30 days",
]

def run_compliance_check(briefing: str) -> dict:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""You are a banking compliance expert.
Based on this threat briefing, assess which RBI and PCI-DSS
controls are AT RISK or need immediate attention.

Threat Briefing:
{briefing}

RBI Controls to check:
{chr(10).join(f'- {c}' for c in RBI_CONTROLS)}

PCI-DSS Controls to check:
{chr(10).join(f'- {c}' for c in PCI_DSS_CONTROLS)}

Return ONLY valid JSON, no extra text, no markdown:
{{
  "rbi": {{
    "at_risk": ["list of RBI controls threatened by identified threats"],
    "compliant": ["list of RBI controls not directly threatened"],
    "score": <0-100 overall RBI compliance score>
  }},
  "pci_dss": {{
    "at_risk": ["list of PCI-DSS controls at risk"],
    "compliant": ["list of PCI-DSS controls not threatened"],
    "score": <0-100 overall PCI-DSS compliance score>
  }},
  "priority_action": "<single most urgent compliance action to take right now>"
}}"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        return json.loads(match.group())

    return {
        "rbi": {"at_risk": [], "compliant": [], "score": 0},
        "pci_dss": {"at_risk": [], "compliant": [], "score": 0},
        "priority_action": "Could not parse compliance response"
    }
