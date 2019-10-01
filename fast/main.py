from fastapi import FastAPI

app = FastAPI(title="fast_api_speed_test")


@app.post("/test")
def tester(payload: dict):
    if payload:
        print(type(payload))
        return 200
