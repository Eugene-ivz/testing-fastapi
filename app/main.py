from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.books.routes import books_router
from app.users.routes import users_router
from app.db.base import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield  # The app is running
    print("Closing database connection ")
    await engine.dispose()



app = FastAPI(lifespan=lifespan)

app.include_router(books_router)
app.include_router(users_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
async def root():
    return {"message": "hello"}


