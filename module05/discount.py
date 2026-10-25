"""
Self-Assessment Questions

1. When order_total = 350, it checks if 350 >= 500 (False). 
It then moves to the next condition, 350 >= 200 (True). 
It assigns a 10% discount and skips the rest of the branch. 
The final price becomes 350 * 0.90 = $315.00.

2. A single condition with 'and' requires both conditions to 
be true at the exact same time to execute the block. Two 
separate 'if' statements check independently; if both 
evaluate to true, both separate code blocks run, producing
 different behavior.

3. Systems like income tax brackets, tiered shipping fees,
 and credit card rewards use tiered conditionals.
   Understanding Python conditionals shows how crucial order 
   and mutually exclusive ranges are to prevent applying 
     the wrong rate.
   
"""

# --- Exercise 1 ---
total = 250.0
if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0.0
final = total * (1 - discount)
print(f"Discount: {discount * 100:.0f}%")
print(f"Final price: ${final:.2f}")

# --- Exercise 2 ---
final = 637.50
if final > 1000:
    status = "manager_approval_required"
else:
    status = "auto_approved"
print(f"Status: {status}")

# --- Exercise 3 ---
region = "South"
total = 250.0
if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0.0
if region == "South" and total >= 100:
    print("Region bonus applied: additional 2% off")
    discount += 0.02
final = total * (1 - discount)
print(f"Final discount: {discount * 100:.0f}%")
print(f"Final price: ${final:.2f}")

# --- Exercise 4 ---
region = "South"
total = 150.0
customer_type = "wholesale"
# The flat version avoids deep indentation and makes the rule easier to test on one line.
if region == "South" and total > 100 and customer_type == "Wholesale":
    extra_discount = 0.03

# --- Exercise 5 ---
amount = 15000
if amount <= 0:
    print("SUSPICIOUS")
elif 1 <= amount <= 9999:
    print("NORMAL")
else:
    print("LARGE - REVIEW REQUIRED")

# --- Exercise 6 ---
total_spent = 2500
orders = 12
has_balance = False
is_vip = (total_spent > 2000 or orders > 10) and not has_balance
