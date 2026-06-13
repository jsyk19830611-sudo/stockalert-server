main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

KIS_APP_KEY = os.environ.get("KIS_APP_KEY", "")
KIS_APP_SECRET = os.environ.get("KIS_APP_SECRET", "")
POLYGON_API_KEY = os.environ.get("POLYGON_API_KEY", "")

@app.get("/")
def root():
    return {"status": "ok", "message": "StockAlert Server Running"}

@app.get("/stock/kr/{symbol}")
async def get_kr_stock(symbol: str):
    return {
        "symbol": symbol,
        "name": "삼성전자",
        "currentPrice": 79400,
        "changePercent": "+1.54%",
        "isUp": True,
        "institution": 324000000000,
        "foreign": -189000000000,
        "individual": -135000000000
    }

@app.get("/stock/us/{symbol}")
async def get_us_stock(symbol: str):
    return {
        "symbol": symbol,
        "name": "NVIDIA",
        "currentPrice": 875.40,
        "changePercent": "+1.42%",
        "isUp": True,
        "institution": -2100000000,
        "hedgefund": 890000000,
        "individual": 1200000000
    }

@app.get("/events")
async def get_events():
    return {
        "events": [
            {
                "title": "FOMC 금리 결정",
                "date": "2025-06-18",
                "time_kr": "03:00",
                "time_us": "14:00",
                "time_nz": "06:00",
                "time_au": "04:00",
                "importance": "high"
            },
            {
                "title": "네 마녀의 날",
                "date": "2025-06-20",
                "importance": "high"
            }
        ]
    }
