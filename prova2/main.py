from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/somar/{numero1}/{numero2}")
async def somar(numero1: int, numero2: int):
    return {"resultado": numero1 + numero2}

    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

