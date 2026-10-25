"""Exercise 5: Oberservations & Reflection Answers
*type("12") -> <class 'str'> : Text data inside quotation marks.
*type(12) -> <class 'int'> : Whole integer number.
*type(12.0) -> <class 'float'> : Decimal floating-point number.
*type(True)-> <class 'bool'> : Boolean true/false value.
*"5" + "3" vs 5 + 3:
-"5" + "3" outputs"53" because string literals are concatenated (joined together).
- 5 +3 outputs 8 because integer values are added together arithmetically.
Self Assessment Questions:
1. Python raises a TypeError when attempting arithmetic, or repeats the string if multiplied by a integer. This happens because input() stores values as strings (str), which cannot be used for standard numeric multiplication.
2. The '+' operator is polymorphic: it joins strings together and addsnumbers. Since input() always captures data as plain text (type 'str'), any math operations requires explicit conversion using float() or int() first to treat the values as numbers.
3. In business analytics, numeric variables (floats and ints) track operational metrics like unit costs, sales volumes, and taxes without rounding loss. F-trings  then format the final output cleanly into standardized currency ($:.2f) and percentage (:.1%) summaries for executive reports."""


# --- Exercise 1 ---
product = "Notebook"
unit_price = 4.99
quantity = 12
in_stock = True
print(type(product))
print(type(unit_price))
print(type(quantity))
print(type(in_stock))


# --- Exercise 2 ---
print(f"{quantity} units of {product} at ${unit_price} each = ${unit_price * quantity:.2f}")


# --- Exercise 3 ---
user_product = input("Enter product name: ")
user_price = float(input("Enter product price: "))
user_qty = int(input("Enter product quantity: "))
print(f"{user_qty} units of {user_product} at ${user_price} each =${user_price * user_qty:.2f}")


# --- Exercise 4 ---
prod_name ="Notebook"
prod_price = 4.99
prod_qty = 12
unit_cost = 3.29
revenue = prod_price * prod_qty
margin = (prod_price - unit_cost) / prod_price
print(f"Product: {prod_name}")
print(f"Price: ${prod_price:.2f}")
print(f"Qty: {prod_qty}")
print(f"Revenue: ${revenue:.2f}")
print(f"Margin: {margin:.1%}")
