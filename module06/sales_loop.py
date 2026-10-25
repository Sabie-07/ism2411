"""
SELF-ASSESSMENT REFLECTION QUESTIONS

1.   Step 1: Initialize an accumulator variable (e.g., total = 0) before the loop starts.
    This gives the loop a clean starting baseline.
    Step 2: Update the variable inside the loop as each item is processed (e.g., total += sale).
    This incrementally collects results across each iteration.
   Step 3: Use/output the result after the loop completes.
    Waiting until the loop finishes ensures you use the final aggregated value rather than a partial state.

2.  The while loop requires manual counter initialization (i = 0) and explicit manual incrementing (i += 1),
  making it longer and introducing the risk of infinite loops if forgotten. The for loop is cleaner, more 
  concise, and idiomatic in Python when iterating directly over known sequences.

3.  Dataset: A list of daily transaction receipts or employee work hours.
    List contents: Hourly shift logs (e.g., [8.0, 7.5, 8.5, 6.0, 8.0]).
   Accumulate: Total weekly hours worked and total pay earned.
   Output: Total hours logged, overtime hours, and gross weekly payroll.
"""

# Common sales list used across exercises
sales = [120, 80, 250, 175, 90, 410, 60, 215]

# --- Exercise 1 ---
# Sum a list without sum() using a for loop and accumulator pattern
total_1 = 0
for sale in sales:
    total_1 += sale
print(f"Total: ${total_1}")

# --- Exercise 2 ---
# Track both total and count inside loop to compute average (no sum() or len())
total_2 = 0
count_2 = 0
for sale in sales:
    total_2 += sale
    count_2 += 1
average = total_2 / count_2 if count_2 > 0 else 0
print(f"Total: ${total_2}")
print(f"Count: {count_2}")
print(f"Average: ${average:.2f}")

# --- Exercise 3 ---
# Find max without max()
current_max = 0
for sale in sales:
    if sale > current_max:
        current_max = sale
print(f"Largest sale: ${current_max}")

# --- Exercise 4 ---
# Filtered count and sum: sales over $100
count_over_100 = 0
total_over_100 = 0
for sale in sales:
    if sale > 100:
        count_over_100 += 1
        total_over_100 += sale
print(f"Sales over $100: {count_over_100}")
print(f"Total of those sales: ${total_over_100}")

# --- Exercise 5 ---
# break / continue: print sales > $100, stop when hitting sale > $400
for sale in sales:
    if sale > 400:
        print(f"Alert: outlier found - ${sale}. Stopping.")
        break
    if sale <= 100:
        continue
    print(f"${sale}")

# --- Exercise 6 ---
# While loop sum implementation
# Trade-off note: In production, the for-loop version is preferred because it is 
# more concise, pythonic, and eliminates index boundary/infinite loop errors.
total_6 = 0
i = 0
while i < len(sales):
    total_6 += sales[i]
    i += 1
print(f"Total (while loop): ${total_6}")

# --- Exercise 7 ---
# Tiered discount: >= $200 -> 10%, >= $100 -> 5%, else 0%
for sale in sales:
    if sale >= 200:
        discount_rate = 0.10
        discount_pct = "10%"
    elif sale >= 100:
        discount_rate = 0.05
        discount_pct = "5%"
    else:
        discount_rate = 0.0
        discount_pct = "0%"

    discounted_price = sale * (1 - discount_rate)
    print(f"${sale} -> {discount_pct} discount -> ${discounted_price:.2f}")