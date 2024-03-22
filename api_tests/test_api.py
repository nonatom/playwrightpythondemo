from playwright.sync_api import *


def test_users_search(api_context: APIRequestContext):
    query = "John"
    response = api_context.get(f"/users/search?q={query}")

    user_data = response.json()

    print("Users found: ", user_data["total"])

    for user in user_data["users"]:
        print("Checking user: ", user["firstName"])
        assert query in user["firstName"]


def test_create_user(api_context: APIRequestContext):
    response = api_context.post(
        "/users/add",
        data={
            "firstName": "Damien",
            "lastName": "Smith",
            "age": 27
        })

    created_user = response.json()
    print(f"\nCreated user: {created_user}")
    assert created_user["id"] == 101
    assert created_user["firstName"] == "Damien"
    assert created_user["lastName"] == "Smith"
    assert created_user["age"] == 27


def test_update_user(api_context: APIRequestContext):
    print(api_context.get("users/1").json()["lastName"])
    response = api_context.put(
        "users/1",
        data={
            "lastName": "Smith",
            "age": 20
        }
    )

    user_data = response.json()
    print(f"\nUpdated user: {user_data}")
    assert user_data["lastName"] == "Smith"
    assert user_data["age"] == 20
