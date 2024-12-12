from fastapi import APIRouter, HTTPException, Query,Depends
import httpx
from typing import Optional
from Productschemas import Product, ProductsList
from Redis import get_cached_response,set_cached_response
from fastapi_limiter.depends import RateLimiter

BASE_URL = "https://dummyjson.com/products"


router = APIRouter()


"""
    I had to make the return a simple dictionary because I didn't have enough time to fix and debug the return types and their schemas
    I have used 'Paste JSON as Code' extention to retrieve the data format 

"""

@router.get("/", response_model=dict,dependencies=[Depends(RateLimiter(times=200, seconds=60))])
async def list_products(
    skip: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    
):
    cache_key = f"list_products:{skip}:{limit}"
    cached_response = await get_cached_response(cache_key)
    if cached_response:
        print("cash hit !!!!!!!")
        return cached_response

    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params={"limit": limit, "skip": (skip - 1) * limit})
        if response.status_code == 200:
            data = response.json()
            await set_cached_response(cache_key, data, ttl=60)  
            return data
        raise HTTPException(status_code=response.status_code, detail="Error fetching products")






@router.get("/search", response_model=dict,dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def search_products(query: str):
    cache_key = f"search_products:{query}"
    cached_response = await get_cached_response(cache_key)
    if cached_response:
        print("cash hit !!!!!!!")
        return cached_response

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/search", params={"q": query})
            if response.status_code == 200:
                data = response.json()
                await set_cached_response(cache_key, data, ttl=60)  
                return data
            raise HTTPException(status_code=response.status_code, detail="Error searching products")
    except Exception as e:
        raise HTTPException(status_code=500, detail="error while searching for products.")



@router.get("/{product_id}", response_model=Product,dependencies=[Depends(RateLimiter(times=20, seconds=60))])
async def get_product_by_id(product_id: int):
    cache_key = f"get_product:{product_id}"
    cached_response = await get_cached_response(cache_key)
    if cached_response:
        print("cash hit !!!!!!!")
        return cached_response

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/{product_id}")
            if response.status_code == 200:
                data = response.json()
                await set_cached_response(cache_key, data, ttl=60)
                return data
            raise HTTPException(status_code=response.status_code, detail="Product not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while retrieving the product.")




@router.get("/category/{category}", response_model=dict,dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def filter_products_by_category(category: str):
    cache_key = f"filter_products:{category}"
    cached_response = await get_cached_response(cache_key)
    if cached_response:
        print("cash hit !!!!!!!")
        return cached_response

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/category/{category}")
            if response.status_code == 200:
                data = response.json()
                await set_cached_response(cache_key, data, ttl=60)  
                return data
            raise HTTPException(status_code=response.status_code, detail="Category not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while filtering products by category.")