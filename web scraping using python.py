import requests
from bs4 import BeautifulSoup

# Step 1: Send an HTTP request to the website
url = "https://webscraper.io/test-sites/e-commerce/allinone"
response = requests.get(url)

# Step 2: Check if the request was successful
if response.status_code == 200:
    # Step 3: Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Step 4: Find all the product elements on the page
    products = soup.find_all('div', class_='col-sm-4 col-lg-4 col-md-4')  # Product card divs
    
    # Step 5: Extract relevant data from each product
    for product in products:
        # Extract product name
        product_name = product.find('h4', class_='title').text.strip()
        
        # Extract product price
        product_price = product.find('h4', class_='price').text.strip()
        
        # Extract product description (if available)
        product_description = product.find('p', class_='description').text.strip() if product.find('p', class_='description') else 'No description available'
        
        # Print the extracted data
        print(f"Product: {product_name}")
        print(f"Price: {product_price}")
        print(f"Description: {product_description}")
        print("-" * 40)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
