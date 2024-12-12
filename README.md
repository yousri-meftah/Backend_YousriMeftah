# FastAPI Project with Redis Caching and Rate Limiting

This repository contains a FastAPI-based project integrated with Redis for caching and rate limiting. The API interacts with the DummyJSON API to provide endpoints for searching products, retrieving product details, and filtering products by category.

## Features
- **Caching**: Uses Redis to cache responses for frequently requested endpoints.
- **Rate Limiting**: Implements rate limiting to prevent excessive requests from individual clients and ensure compliance with external API rate limits.
- **API Endpoints**: Comprehensive set of endpoints to interact with product data from the DummyJSON API.
- **Dockerized Setup**: Includes a Docker Compose configuration for running Redis.

---

## Prerequisites
- Docker and Docker Compose installed on your machine.
- Python 3.8 or later.

---

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/yousri-meftah/Backend_YousriMeftah.git
cd Backend_YousriMeftah
```

### Install Python Dependencies
1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Run Redis with Docker Compose
1. Start Redis:
   ```bash
   docker-compose up -d
   ```

2. Verify Redis is running:
   ```bash
   docker ps
   ```
   Redis should be listed as a running container.

### Start the API
1. Run the FastAPI application:
   ```bash
   python src/main.py
   ```

2. Access the API documentation:
   - Swagger UI: [http://127.0.0.1:8000/](http://127.0.0.1:8000/docs)
   

---

## Endpoints Documentation

### 1. Search Products
**Endpoint**: `/search`
- **Method**: `GET`
- **Description**: Search for products by a query string.
- **Parameters**:
  - `query` (str): The search query.
- **Responses**:
  - **200 OK**: Returns a list of matching products.
  - **500 Internal Server Error**: An error occurred while processing the request.

**Example**:
```bash
curl -X GET "http://127.0.0.1:8000/product/search?query=phone"
```

---

### 2. Get Product by ID
**Endpoint**: `/{product_id}`
- **Method**: `GET`
- **Description**: Retrieve details of a product by its ID.
- **Parameters**:
  - `product_id` (int): The ID of the product.
- **Responses**:
  - **200 OK**: Returns the product details.
  - **404 Not Found**: Product not found.
  - **500 Internal Server Error**: An error occurred while processing the request.

**Example**:
```bash
curl -X GET "http://127.0.0.1:8000/product/1"
```

---

### 3. Filter Products by Category
**Endpoint**: `/category/{category}`
- **Method**: `GET`
- **Description**: Filter products by category.
- **Parameters**:
  - `category` (str): The category name.
- **Responses**:
  - **200 OK**: Returns a list of products in the specified category.
  - **404 Not Found**: Category not found.
  - **500 Internal Server Error**: An error occurred while processing the request.

**Example**:
```bash
curl -X GET "http://127.0.0.1:8000/product/category/beauty"
```

---
# Running Tests

To ensure the API is working as expected, the project includes test cases written with `pytest`. Follow these steps to run the tests:



## Running the Tests
1. Navigate to the project directory where the tests are located.
2. Run the tests using `pytest`:
   ```bash
   pytest src/test.py
   ```

## Expected Output
If all tests pass, you should see output similar to this:
```plaintext
============================= test session starts =============================
platform linux -- Python 3.x, pytest-8.x
collected 3 items

src/test.py ......                                                   [100%]

============================== 3 passed in 1.23s ==============================
```

---

## Notes
- Ensure Redis is running before starting the FastAPI application.
---

