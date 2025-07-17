from fastapi import Header, HTTPException

# Dummy set of allowed API keys
API_KEYS = {"guest123", "admin456"}

def verify_api_key(x_api_key: str = Header(...)):
    """
    Verifies that the provided API key is in the allowed list.
    """
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=403, detail="Invalid API Key")
