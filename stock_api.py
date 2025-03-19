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
        
        # Debugging: Print available data in logs
        print(info) 
        
        return {
            "ticker": ticker.upper(),
            "company": info.get("shortName", "Data not available"),
            "revenueGrowth": info.get("revenueGrowth", "Data not available"),
            "peRatio": info.get("trailingPE", "Data not available"),
            "pegRatio": info.get("pegRatio", "Data not available"),
            "roe": info.get("returnOnEquity", "Data not available"),
            "quickRatio": info.get("quickRatio", "Data not available"),
        }
    except Exception as e:
        return {"error": str(e)}
