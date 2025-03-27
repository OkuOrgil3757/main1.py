from supabase import create_client, Client
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# https://docs.render.com/deploy-fastapi

url: str = "https://rfhfjcrdxfofgycpirkv.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJmaGZqY3JkeGZvZmd5Y3Bpcmt2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE4MzkzNDIsImV4cCI6MjA1NzQxNTM0Mn0.XNcm1ZEMoDacqKGR-397eoJr_bvmiX6TN_JaJrHmmd8"
supabase: Client = create_client(url, key)

app = FastAPI()

class ChocolateBar(BaseModel):
    company: str
    specific_bean_origin_or_bar_name: str
    ref: int
    review_date: int
    cocoa_percent: int
    company_location: str
    rating: float
    bean_type: str
    broad_bean_origin: str

@app.post("/chocolate_bar/")
def create_chocolate_bar(chocolate_bar: ChocolateBar):
    data = supabase.table("chocolate_bars").insert(chocolate_bar.dict()).execute()
    if data.data:
        return data.data
    else:
        raise HTTPException(status_code=400, detail="Item could not be created")
    

@app.get("/chocolate_bar/")
def read_chocolate_bars():
    data = supabase.table("chocolate_bars").select("*").execute()
    if data.data:
        return data.data
    else:
        raise HTTPException(status_code=404, detail="Items not found")
    

@app.put("/chocolate_bar/{chocolate_bar_id}")
def update_chocolate_bar(chocolate_bar_id: int, chocolate_bar: ChocolateBar):
    data = supabase.table("chocolate_bars").update(chocolate_bar.dict()).eq("id", chocolate_bar_id).execute()
    if data.data:
        return data.data
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/chocolate_bar/{chocolate_bar_id}")
def delete_chocolate_bar(chocolate_bar_id: int):
    data = supabase.table("chocolate_bars").delete().eq("id", chocolate_bar_id).execute()
    if data.data:
        return {"message": "Item deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
