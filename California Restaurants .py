import requests
import pandas as pd


# Function to fetch data from Yelp API
def fetch_yelp_data(api_key, location):
    headers = {
        'Authorization': 'Bearer ' + api_key,
    }
    params = {
        'location': location,
        'categories': 'restaurants',
        'limit': 50  # Maximum limit per request is 50
    }
    response = requests.get('https://api.yelp.com/v3/businesses/search', headers=headers, params=params)
    data = response.json()
    return data.get('businesses', [])


# Function to extract required information
def extract_info(business):
    name = business['name']
    phone = business['phone']
    location = ', '.join(business['location']['display_address'])
    return {
        'Name': name,
        'Phone': phone,
        'Location': location
    }


# Main function
def main():
    api_key = 'Replace Your API Key'
    location = 'California'

    data = fetch_yelp_data(api_key, location)
    if not data:
        print("No data found.")
        return

    extracted_data = [extract_info(business) for business in data]

    # Create DataFrame
    df = pd.DataFrame(extracted_data)

    # Save to Excel
    df.to_excel('california_restaurants.xlsx', index=False)


if __name__ == "__main__":
    main()
