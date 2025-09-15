def test_create_user(test_client):
    response = test_client.post("/users/", json={"name": "Alice", "email": "alice@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"
    assert "id" in data

def test_get_users(test_client):
    # Create user first
    test_client.post("/users/", json={"name": "Bob", "email": "bob@example.com"})
    # Now fetch users
    response = test_client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1



def test_update_user(test_user,test_client):
    user_id = test_user["id"]
    updated = {"name": "Updated John", "email": "updated@example.com"}
    response = test_client.put(f"/users/{user_id}", json=updated)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated John"
    assert data["email"] == "updated@example.com"


def test_delete_user(test_user,test_client):
    user_id = test_user["id"]
    response = test_client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
