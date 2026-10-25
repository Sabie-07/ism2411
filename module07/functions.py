"""
Self-Assessment Questions:

1.   The first bug spotted was the missing colon on line 10 (`for sale in sales`).
     I identified it directly from Python's SyntaxError traceback and editor red 
     squigglies before asking any tools. This shows that my instincts are solid for 
     catching structural syntax errors early, though I still benefit from tracing 
     variable states step-by-step for logic bugs.

2.   `apply_discount(price, tier)` takes a base numerical price and a customer's 
     membership tier ("gold", "silver", "bronze", or any other string). It determines the 
     appropriate discount percentage (15%, 10%, 5%, or 0%) and returns the discounted total 
     dollar amount. A colleague can call it successfully without looking at the internal 
     `if/elif` statements because the parameter names, expected types, and returned value 
     are self-explanatory.

3.   I used Gemini purely as an assistive debugging and conceptual tutor 
     for Exercise 5. Following the lab protocol, I pasted only the terminal error messages 
     (e.g., "IndexError: list index out of range") rather than having AI write the code. 
     The AI explained the concept of 0-based indexing and boundary limits, which helped 
     me understand why `i <= len(sales)` overshoots the last valid index. Using AI as an 
     explainer built my conceptual understanding of index boundaries rather than shortcutting 
     the implementation.
"""

# --- Exercise 1 ---
def apply_discount(price, tier):
    """Calculates discounted price based on membership tier."""
    if tier == "gold":
        return price * (1 - 0.15)
    elif tier == "silver":
        return price * (1 - 0.10)
    elif tier == "bronze":
        return price * (1 - 0.05)
    else:
        return price * 1.0

# Test all four tiers with price = $200
print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")
print()


# --- Exercise 2 ---
def calculate_tax(price, rate):
    """Calculates tax amount on a given price and tax rate."""
    return price * rate

# Test calls
tax1 = calculate_tax(100, 0.07)
print(f"Tax on $100 at 7%: ${tax1:.2f}")

tax2 = calculate_tax(250, 0.08)
print(f"Tax on $250 at 8%: ${tax2:.2f}")
print()


# --- Exercise 3 ---
def final_price(price, tier, tax_rate):
    """Applies tier discount and adds calculated sales tax."""
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

# Test Exercise 3 steps
test_price = 200
disc_price = apply_discount(test_price, "gold")
tax_val = calculate_tax(disc_price, 0.07)
total_val = disc_price + tax_val

print(f"After gold discount: ${disc_price:.2f}")
print(f"After tax: ${total_val:.2f}")
print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')
print()


# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")
print()


# --- Exercise 5 ---
# Fixes applied to broken_sales.py:
# Bug 1: total = sale was overwriting instead of accumulating; changed to total += sale.
# Bug 2: for sale in sales was missing a closing colon (:).
# Bug 3: while i <= len(sales) caused an IndexError (off-by-one); changed to i < len(sales).

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1
print()


# --- Exercise 6 ---
# Scope experiment explanation:
# `x = 100` defines a variable in the global scope. Inside `double_it()`, `x = 999`
# creates a distinct local variable that exists only inside the function namespace.
# Reassigning `x` inside does not modify the global `x`. Therefore, `print(x)` before
# and after the function call still refers to the global variable with value 100,
# while `double_it()` executes using the local variable and returns 999 * 2 = 1998.

x = 100  # global variable

def double_it():
    x = 999  # local variable - different from global x!
    return x * 2

print(x)             # prints 100
print(double_it())   # prints 1998
print(x)             # prints 100 (global x has not changed)
