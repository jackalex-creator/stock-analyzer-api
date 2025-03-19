from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Stock Data API is live!"}

@app.get("/stock/{ticker}")
def get_stock_data(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        # DEBUG: Print full data response (for troubleshooting)
        print("Full stock info:", info)

        if not info or "shortName" not in info:
            return {"error": "No data available for this ticker. Check the symbol."}

        return {
            "ticker": ticker.upper(),
            "company": info.get("shortName", "Not found"),
            "revenueGrowth": info.get("revenueGrowth", "Not found"),
            "peRatio": info.get("trailingPE", "Not found"),
            "pegRatio": info.get("pegRatio", "Not found"),
            "roe": info.get("returnOnEquity", "Not found"),
            "quickRatio": info.get("quickRatio", "Not found"),
        }
    except Exception as e:
        return {"error": str(e)}
