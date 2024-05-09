# import requests

# def fetch_random_user_freeapi():
#     url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
#     response = requests.get(url)
#     data = response.json()

#     if response["success"] and "data" in data:
#         user_data = data["data"]
#         username = user_data["login"]["useraname"]
#         country = user_data["location"]["country"]
#         return username, country
#     else:
#         raise Exception("Failed to fetch user data")
    
# def main():
#     try:
#         username, country = fetch_random_user_freeapi()
#         print(f"Username: {username}")
#         print(f"Country: {country}")
#     except Exception as e:
#         print(str(e))

# if __name__ == "__main__":
#     main()

import requests


def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)

    # Check response status code for success (optional)
    if response.status_code == 200:
        data = response.json()  # Access the JSON data
    else:
        raise Exception(f"Error: Failed to fetch user data. Status code: {response.status_code}")

    print(response.status_code)
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]  # Corrected typo (username)
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch valid user data")


def main():
    try:
        username, country = fetch_random_user_freeapi()
        print(f"Username: {username}")
        print(f"Country: {country}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
