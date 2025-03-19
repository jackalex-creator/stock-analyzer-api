from fastapi import FastAPI
import yfinance as yf

# Create the API
app = FastAPI()

# Test if API is working
@app.get("/")
def home():
    return {"message": "Stock Data API is live!"}

# Get stock data when requested
@app.get("/stock/{ticker}")
def get_stock_data(ticker: str):
    try:
        # Fetch stock info
        stock = yf.Ticker(ticker)
        info = stock.info

        return {
            "ticker": ticker.upper(),
            "company": info.get("shortName", "N/A"),
            "revenueGrowth": info.get("revenueGrowth", "N/A"),
            "peRatio": info.get("trailingPE", "N/A"),
            "pegRatio": info.get("pegRatio", "N/A"),
            "roe": info.get("returnOnEquity", "N/A"),
            "quickRatio": info.get("quickRatio", "N/A"),
        }
    except Exception as e:
        return {"error": str(e)}
