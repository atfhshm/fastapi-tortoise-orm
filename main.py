from fastapi import FastAPI


from db import connect_to_db

app = FastAPI()

connect_to_db(app=app)


@app.get("/", tags=["root"])
async def root():
    return {"msg": "hello, from API"}
