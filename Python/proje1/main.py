from Helpers.product_helper import ProductHelper
import os

# Check if Products.txt file exists
file_path = 'C:\\Users\\btk02\\OneDrive\\Desktop\\UygulamlarlaNesneYönelimliProgramlamaPython\\Python\\proje1\\Products.txt'
if not os.path.exists(file_path):
    print(f"The file {file_path} was not found.")
else:
    # Create products from text file
    products = ProductHelper.create_item_from_text(file_path)

    # Print each product
    for product in products:
        print(product)

    # Calculate and print the total balance
    total_balance = ProductHelper.get_total_balance(products)
    print(f"Total balance including 20% VAT: {total_balance}")


