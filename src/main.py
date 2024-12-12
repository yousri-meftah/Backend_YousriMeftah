from fastapi import FastAPI
import uvicorn
from Product import router
from fastapi.middleware.cors import CORSMiddleware
from fastapi_limiter import FastAPILimiter
from redis.asyncio import Redis
from contextlib import asynccontextmanager
@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = Redis.from_url("redis://localhost:6379", decode_responses=True)
    try:
        await FastAPILimiter.init(redis)
        yield
    finally:
        await redis.close()

app = FastAPI(
    title='Toho_task',
    description='toho task',
    version='1.0.0',
    docs_url='/',
    lifespan=lifespan, 
)



origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/product", tags=["product"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
