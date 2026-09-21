from fastapi import FastAPI 

app = FastAPI(title="Recipe Recommender API")

@app.get("/health")
def health_check():
  return {"status": "ok"}