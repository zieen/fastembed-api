import requests
import json
import time

BASE_URL = "http://localhost:8000"

def test_health():
    print(f"Testing Health Check at {BASE_URL}/health...")
    try:
        resp = requests.get(f"{BASE_URL}/health")
        resp.raise_for_status()
        print("✅ Health Check Passed")
    except Exception as e:
        print(f"❌ Health Check Failed: {e}")
        exit(1)

def test_dense():
    print("\nTesting Dense Embeddings...")
    payload = {
        "documents": ["Hello world", "FastAPI is great"]
    }
    try:
        resp = requests.post(f"{BASE_URL}/embed/text", json=payload)
        resp.raise_for_status()
        data = resp.json()
        embeddings = data["embeddings"]
        print(f"Received {len(embeddings)} embeddings")
        if len(embeddings) == 2 and len(embeddings[0]) > 0:
            print(f"Dimension: {len(embeddings[0])}")
            print("✅ Dense Embeddings Passed")
        else:
            print("❌ Dense Embeddings Failed: Invalid response format")
    except Exception as e:
        print(f"❌ Dense Embeddings Failed: {e}")

def test_sparse():
    print("\nTesting Sparse Embeddings...")
    payload = {
        "documents": ["Hello world", "SPLADE is interesting"]
    }
    try:
        resp = requests.post(f"{BASE_URL}/embed/sparse", json=payload)
        resp.raise_for_status()
        data = resp.json()
        embeddings = data["embeddings"]
        print(f"Received {len(embeddings)} embeddings")
        if len(embeddings) == 2 and "indices" in embeddings[0] and "values" in embeddings[0]:
            print(f"First vector indices: {embeddings[0]['indices']}")
            print("✅ Sparse Embeddings Passed")
        else:
            print("❌ Sparse Embeddings Failed: Invalid response format")
    except Exception as e:
        print(f"❌ Sparse Embeddings Failed: {e}")

if __name__ == "__main__":
    # Wait for service to be ready
    for _ in range(10):
        try:
            requests.get(f"{BASE_URL}/health")
            break
        except:
            time.sleep(1)
            
    test_health()
    test_dense()
    test_sparse()
