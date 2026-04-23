from tavily import TavilyClient
import os

def run_researcher() -> str:
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    queries = [
        "banking fraud cyberattack 2025",
        "phishing attacks targeting banks 2025",
        "ransomware attack bank financial sector 2025",
        "swift banking system cyber threat 2025",
    ]

    all_results = ""
    for query in queries:
        results = client.search(
            query=query,
            max_results=3,
            search_depth="advanced"
        )
        for r in results.get("results", []):
            all_results += f"- {r['title']}: {r['content'][:300]}\n"

    return all_results
