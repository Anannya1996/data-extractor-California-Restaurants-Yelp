# Yelp Restaurant Data Fetcher

This Python script fetches restaurant data from the Yelp API based on a specified location and saves it into an Excel file.

## Setup

1. **Obtain Yelp API Key**: Before using this script, you need to obtain an API key from Yelp. Visit the [Yelp Fusion API](https://www.yelp.com/developers/documentation/v3/authentication) page for more information.

2. **Install Required Packages**: Ensure you have the necessary packages installed. You can install them using pip:
    ```bash
    pip install requests pandas
    ```

## Usage

1. **Insert Your Yelp API Key**: Replace `'Replace Your API Key'` in the script with your actual Yelp API key.

2. **Specify Location**: Set the `location` variable in the script to the desired location. The script will fetch restaurant data for this location.

3. **Run the Script**: Execute the script using Python:
    ```bash
    python script_name.py
    ```

4. **Output**: The script will generate an Excel file named `california_restaurants.xlsx` containing information about restaurants in the specified location.

## Notes

- The maximum limit per request for fetching data from Yelp is 50 businesses. If you need more data, you might need to paginate through the results.

- Ensure you use the fetched data responsibly and comply with Yelp's terms of service and API usage guidelines.

