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

        # Extract data, ensuring defaults for missing values
        pe_ratio = info.get("trailingPE")
        revenue_growth = info.get("revenueGrowth")

        # Calculate PEG Ratio manually if missing
        if info.get("pegRatio") is not None:
            peg_ratio = info["pegRatio"]
        elif pe_ratio and revenue_growth and revenue_growth > 0:
            peg_ratio = round(pe_ratio / (revenue_growth * 100), 2)  # Convert growth % for correct calculation
        else:
            peg_ratio = "Not available"

        return {
            "ticker": ticker.upper(),
            "company": info.get("shortName", "Not found"),
            "revenueGrowth": revenue_growth,
            "peRatio": pe_ratio,
            "pegRatio": peg_ratio,
            "roe": info.get("returnOnEquity", "Not found"),
            "quickRatio": info.get("quickRatio", "Not found"),
        }
    except Exception as e:
        return {"error": str(e)}
