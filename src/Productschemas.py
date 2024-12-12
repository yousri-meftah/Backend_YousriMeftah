from pydantic import BaseModel
from typing import List, Optional, Dict

class Review(BaseModel):
    rating: Optional[int]
    comment: Optional[str]
    date: Optional[str]
    reviewerName: Optional[str]
    reviewerEmail: Optional[str]

class Dimensions(BaseModel):
    width: Optional[float]
    height: Optional[float]
    depth: Optional[float]

class MetaData(BaseModel):
    createdAt: Optional[str]
    updatedAt: Optional[str]
    barcode: Optional[str]
    qrCode: Optional[str]

class Product(BaseModel):
    id: Optional[int]
    title: Optional[str]
    description: Optional[str]
    price: Optional[float]
    discountPercentage: Optional[float]
    rating: Optional[float]
    stock: Optional[int]
    brand: Optional[str]
    category: Optional[str]
    thumbnail: Optional[str]
    images: Optional[List[str]]
    tags: Optional[List[str]]
    sku: Optional[str]
    weight: Optional[float]
    dimensions: Optional[Dimensions]
    warrantyInformation: Optional[str]
    shippingInformation: Optional[str]
    availabilityStatus: Optional[str]
    reviews: Optional[List[Review]]
    returnPolicy: Optional[str]
    minimumOrderQuantity: Optional[int]
    meta: Optional[MetaData]

class ProductsList(BaseModel):
    products: Optional[List[Product]]
    total: Optional[int]
    skip: Optional[int]
    limit: Optional[int]
