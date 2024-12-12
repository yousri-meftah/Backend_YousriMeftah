import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

def test_search_products(test_client):
    response = test_client.get("/product/search", params={"query": "phone"})
    assert response.status_code == 200
    assert "products" in response.json()

def test_get_product_by_id(test_client):
    product_id = 1
    response = test_client.get(f"/product/{product_id}")
    assert response.status_code == 200
    assert response.json()["id"] == product_id

def test_filter_products_by_category(test_client):
    category = "beauty"
    response = test_client.get(f"/product/category/{category}")
    assert response.status_code == 200
    assert "products" in response.json()


