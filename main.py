import uvicorn
from fastapi import FastAPI

from routes.checkWord import router as check_word_router


app = FastAPI(title="NSC Game API", version="1.0.0")

app.include_router(check_word_router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello world"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/hello/{name}")
def say_hello(name: str) -> dict[str, str]:
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
