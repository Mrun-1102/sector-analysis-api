from pydantic import BaseModel

class AnalysisResponse(BaseModel):
    sector: str
    markdown_report: str
