from Models.product import Product

class ProductHelper:

    @staticmethod
    def create_item_from_text(file_path):
        products = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    name, price, quantity = line.strip().split(',')
                    product = Product(name, float(price), int(quantity))
                    products.append(product)
        except FileNotFoundError:
            print(f"The file {file_path} was not found.")
        except ValueError:
            print("There was an error in converting the file data to the appropriate types.")
        return products

    @staticmethod
    def get_total_balance(products):
        total = 0
        for product in products:
            total += product.get_total_price()
        total_with_tax = total * 1.20  # Adding 20% VAT
        return total_with_tax
