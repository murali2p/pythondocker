import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def testing():
    return "Welcome to docker! Keep Up :)"


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=80, reload= True)