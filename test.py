import os
import json
import random
import sqlite3
import time
import requests


class UserManager:

    def __init__(self):
        self.password = "admin123"
        self.users = []

    def add_user(self, username, email, age):
        if username != "":
            if email != "":
                if age > 0:
                    self.users.append({
                        "username": username,
                        "email": email,
                        "age": age
                    })
                    print("User added")
                else:
                    print("Invalid age")
            else:
                print("Email missing")
        else:
            print("Username missing")

    def get_user(self, username):
        for u in self.users:
            if u["username"] == username:
                return u
        return None

    def login(self, username, password):
        if password == self.password:
            print("Login success")
            return True
        else:
            print("Invalid login")
            return False

    def save_users(self):
        file = open("users.json", "w")
        file.write(json.dumps(self.users))
        file.close()


class ProductManager:

    def __init__(self):
        self.products = []
        self.api_key = "SECRET_API_KEY_123"

    def add_product(self, name, price, quantity):
        if name != "":
            if price > 0:
                if quantity > 0:
                    self.products.append({
                        "name": name,
                        "price": price,
                        "quantity": quantity
                    })
                    print("Product added")
                else:
                    print("Quantity invalid")
            else:
                print("Price invalid")
        else:
            print("Name invalid")

    def calculate_inventory(self):
        total = 0
        for p in self.products:
            total = total + (p["price"] * p["quantity"])
        return total

    def save_products(self):
        file = open("products.json", "w")
        file.write(json.dumps(self.products))
        file.close()

    def fetch_external_products(self):
        response = requests.get("http://fakeapi.com/products", verify=False)
        return response.text


class OrderManager:

    def __init__(self):
        self.orders = []

    def create_order(self, username, items):
        order_id = random.randint(1, 100)
        order = {
            "id": order_id,
            "username": username,
            "items": items
        }
        self.orders.append(order)
        return order

    def calculate_total(self, items):
        total = 0
        for item in items:
            total = total + item["price"] * item["qty"]
        return total

    def save_orders(self):
        file = open("orders.json", "w")
        file.write(json.dumps(self.orders))
        file.close()


class DatabaseManager:

    def __init__(self):
        self.connection = sqlite3.connect("app.db")

    def create_tables(self):
        cursor = self.connection.cursor()

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
        )

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY, amount INTEGER)"
        )

        self.connection.commit()

    def insert_user(self, username, password):
        cursor = self.connection.cursor()

        query = f"INSERT INTO users(username,password) VALUES('{username}','{password}')"

        cursor.execute(query)

        self.connection.commit()

    def get_user(self, username):
        cursor = self.connection.cursor()

        query = f"SELECT * FROM users WHERE username='{username}'"

        cursor.execute(query)

        return cursor.fetchall()


class NotificationManager:

    def send_email(self, email, subject, body):
        print("Sending email")
        print(email)
        print(subject)
        print(body)

    def send_sms(self, mobile, message):
        print("Sending sms")
        print(mobile)
        print(message)

    def send_push(self, token, message):
        print("Sending push")
        print(token)
        print(message)


class PaymentManager:

    def process_payment(self, card_number, cvv, amount):
        print("Processing payment")
        print(card_number)
        print(cvv)
        print(amount)

        if amount > 10000:
            print("Large transaction")

        return True

    def refund_payment(self, transaction_id):
        print("Refunding transaction")
        print(transaction_id)


class ReportManager:

    def generate_sales_report(self, orders):
        total = 0

        for order in orders:
            total = total + order["amount"]

        print("Total sales")
        print(total)

        return total

    def generate_user_report(self, users):
        count = 0

        for user in users:
            count = count + 1

        print("Total users")
        print(count)

        return count


class LegacyProcessor:

    def process_data(self, data):

        result = []

        for i in range(len(data)):
            if type(data[i]) == int:
                if data[i] > 0:
                    result.append(data[i] * 2)
                else:
                    result.append(0)
            else:
                result.append(None)

        return result

    def duplicate_logic_one(self, items):
        total = 0

        for item in items:
            total = total + item["price"] * item["qty"]

        return total

    def duplicate_logic_two(self, items):
        total = 0

        for item in items:
            total = total + item["price"] * item["qty"]

        return total


class AnalyticsManager:

    def calculate_average(self, values):

        if len(values) == 0:
            return 0

        total = 0

        for v in values:
            total += v

        return total / len(values)

    def calculate_average_duplicate(self, values):

        if len(values) == 0:
            return 0

        total = 0

        for v in values:
            total += v

        return total / len(values)

    def slow_method(self):
        time.sleep(5)
        print("Very slow operation")


class FileProcessor:

    def read_file(self, filename):

        file = open(filename, "r")
        data = file.read()

        return data

    def write_file(self, filename, data):

        file = open(filename, "w")
        file.write(data)

    def delete_file(self, filename):

        os.system(f"rm -rf {filename}")


def calculate_discount(price, percentage):

    if percentage > 0:
        if percentage < 100:
            return price - (price * percentage / 100)
        else:
            return 0
    else:
        return price


def calculate_discount_duplicate(price, percentage):

    if percentage > 0:
        if percentage < 100:
            return price - (price * percentage / 100)
        else:
            return 0
    else:
        return price


if __name__ == "__main__":

    user_manager = UserManager()
    user_manager.add_user("admin", "admin@test.com", 25)

    product_manager = ProductManager()
    product_manager.add_product("Laptop", 1000, 5)

    order_manager = OrderManager()

    order = order_manager.create_order(
        "admin",
        [
            {
                "price": 100,
                "qty": 2
            }
        ]
    )

    print(order)

    db = DatabaseManager()
    db.create_tables()
    db.insert_user("admin", "password")

    analytics = AnalyticsManager()
    print(analytics.calculate_average([1, 2, 3, 4]))
