from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_hello_server() -> str:
    return "Welcome to John's Sever"


@app.get("/greet/{name}")
async def greet_person(name: str) -> str:
    return f"Hello {name}"
