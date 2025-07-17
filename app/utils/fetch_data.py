from duckduckgo_search import DDGS

async def fetch_sector_news(sector: str) -> str:
    """
    Fetches recent market-related news snippets for a given sector using DuckDuckGo.
    """
    query = f"{sector} sector market trends India 2025"
    results = []

    # Use DDGS  context
    with DDGS() as ddgs:
        for r in ddgs.text(query, region='in-en', safesearch='Moderate', max_results=5):
            title = r.get('title', '')
            snippet = r.get('body', '')
            url = r.get('href', '')
            results.append(f"**{title}**\n{snippet}\n[Read more]({url})\n")

    return "\n---\n".join(results)
