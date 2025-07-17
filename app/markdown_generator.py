def generate_markdown(sector: str, ai_response: str) -> str:
    """
    Generate a structured markdown report from AI response.
    """
    markdown = f"# 📈 Trade Opportunities in {sector.title()}\n\n"
    markdown += f"{ai_response}\n\n"
    markdown += "---\n*Report generated using real-time market data and AI analysis.*"
    return markdown
