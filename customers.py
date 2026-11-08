#Self Assessment questions:
# 1.) I use brackets, like data["name"], when the key should always be
#    there. If it's missing, I want an error so I know something broke.
#    I use .get(), like data.get("name", "none"), when the key might not
#    be there. It gives a backup answer instead of crashing.
# 2.)  It reminds me of a pivot table in Excel, where you add up numbers
#    for each group. Python is better for big data because it handles
#    lots of rows fast and I can rerun it anytime without redoing work.


# ("---Exercise 1 ---")
print("---Exercise 1 ---")
customer = {
    "name": "Alice",
    "email": "alice@example.com", 
    "tier": "gold", 
    "ytd_spend": 12400
}

print(customer["name"]) # Accessing value using bracket notation
print(customer["email"]) # Accessing value using bracket notation
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# ("---Exercise 2 ---")
print("---Exercise 2 ---")
customer["phone"] = "813-555-0142"

print(customer)
customer["tier"] = "platinum"

print(customer)
del customer["email"]

print(customer)

print(customer.get("email", "Email not found")) # Using get() method to access a value with a default message

print("---Exercise 3 ---")
#New
print(customer.get("email", "Email not found"))
#Old
# try:
#     print(customer.get("email", "Email not found")) # Using get() method to access a value with a default message
# except KeyError as error:
#     print(f"KeyError caught: {error}")

print("---Exercise 4 ---")
for key, value in customer.items():
    print(f"{key} :  {value}")

for item in customer:
    print(item)

print("---Exercise 5 ---")
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}") # Platinum
print(f"Discount: {discount_rate * 100:.0f}%") # 15%
print(f"Final price: ${final_price:.2f}") # $170.00

print("---Exercise 6 ---")
customers = {
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
}

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate 
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on $300 purchase")

print("---Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
    }

for product, details in catalog.items():
   if details["stock"] < 20:
       print(f"LOW STOCK: {product} - Only {details['stock']} left in stock!")

print("---Exercise 8 ---")
transactions = {
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
}

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + sale["amount"]
print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")



