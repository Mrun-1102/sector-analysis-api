from fastapi import FastAPI, Depends, HTTPException, Request  # ✅ Add Request
from app.schemas import AnalysisResponse
from app.auth import verify_api_key
from app.rate_limit import limiter
from slowapi.middleware import SlowAPIMiddleware

from app.utils.fetch_data import fetch_sector_news
from app.utils.ai_analysis import analyze_with_gemini
from app.markdown_generator import generate_markdown

app = FastAPI(title="Trade Opportunities API")

# Add rate limiting
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.get("/analyze/{sector}", response_model=AnalysisResponse, tags=["Analyze"])
@limiter.limit("5/minute")
async def analyze_sector(
    request: Request,  # ✅ Must be here for rate limiting to work
    sector: str,
    api_key: str = Depends(verify_api_key)
):
    """
    Analyze a given sector and return a markdown trade report.
    """
    try:
        # Step 1: Fetch market data
        raw_data = await fetch_sector_news(sector)

        # Step 2: Analyze with Gemini
        prompt = f"Based on the following data, write a detailed markdown report on trade opportunities in India's {sector} sector:\n\n{raw_data}"
        ai_analysis = await analyze_with_gemini(prompt)

        # Step 3: Format markdown
        markdown_report = generate_markdown(sector, ai_analysis)

        return {"sector": sector, "markdown_report": markdown_report}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during analysis: {str(e)}")
    

