from fastapi import FastAPI


from core.db import connect_to_db

app = FastAPI()

connect_to_db(app=app)


@app.get("/", tags=["root"])
async def root():
    return {"msg": "hello, from API"}


# to run the application using uvicorn
# python -m core.main

# import uvicorn

# if __name__ == "__main__":
#     uvicorn.run(app="core.main:app", host="127.0.0.1", port=8000, reload=True)
