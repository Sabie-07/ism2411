"""
SELF-ASSESSMENT QUESTIONS:

1. Python would not crash; it would produce a wrong answer silently (a logical error).
   Multiplying by 10 instead of 0.10 would calculate a 1,000% discount instead of a 10%
   discount, resulting in heavily negative discounted revenue and negative profit.

2.Managing shifts or staffing in a call center or retail store: if staff are scheduled
   in teams of 5, integer division (//) calculates how many complete 5-person teams can
   be formed, while modulo (%) identifies how many unassigned workers remain to cover
   floating roles or partial shifts. Another example is manufacturing assembly, where
   components are bundled into multi-packs (e.g., 6-packs of soda), and the remainder
   represents loose items held for the next production run.

3. Formatting specifications inside f-strings (like combining commas for thousands
   separators, decimal precision, and percentage formats) can still require double-checking
   the exact syntax. Practicing small standalone snippets with varied financial formatting
   cases will help solidify the rules.
"""
# --- Exercise 1 ---
price_1 = 50
quantity_1 = 12
revenue_1 = price_1 * quantity_1
print(f"Revenue: ${revenue_1:,.2f}")

# --- Exercise 2 ---
cost_2 = 32
price_2 = 50
margin_2 = (price_2 - cost_2) / price_2
print(f"Margin: {margin_2:.1%}")

# --- Exercise 3 ---
# Product A

price_a, cost_a = 60, 30
margin_a = (price_a - cost_a) / price_a
# Product B

price_b, cost_b = 80, 48
margin_b = (price_b - cost_b) / price_b
product_a_wins = margin_a > margin_b
print(f"Product A Margin: {margin_a:.1%}")
print(f"Product B Margin: {margin_b:.1%}")
print(f"Product A has a higher margin: {product_a_wins}")

# --- Exercise 4 ---
price_4 = 120
margin_4 = 0.35
is_premium = (price_4 > 100) and (margin_4 > 0.3)
print(f"is_premium = {is_premium}")

# --- Exercise 5 ---
div_result = 17 / 5
floor_result = 17 // 5
mod_result = 17 % 5
print(f"17 / 5 = {div_result}")
print("Explanation: Standard division returns a floating-point number. Used for finding exact financial rates or average unit costs.")
print(f"17 // 5 = {floor_result}")
print("Explanation: Floor (integer) division returns the largest whole integer. Used for determining full batches, crates, or complete packages.")
print(f"17 % 5 = {mod_result}")
print("Explanation: Modulo returns the remainder after integer division. Used for counting leftover inventory or cycle schedules.")

# --- Exercise 6 ---
product_name = input("Enter product name: ")
retail_price = float(input("Enter retail price: "))
unit_cost = float(input("Enter unit cost: "))
quantity_sold = int(input("Enter quantity sold: "))
discount_pct_input = float(input("Enter discount percentage (e.g., 10 for 10%): "))
discount_rate = discount_pct_input / 100
revenue_before_discount = retail_price * quantity_sold
discounted_revenue = revenue_before_discount * (1 - discount_rate)
total_cost = unit_cost * quantity_sold
net_profit = discounted_revenue - total_cost
gross_margin = (net_profit / discounted_revenue) if discounted_revenue > 0 else 0.0
print("\n--- Pricing Summary ---")
print(f"Product: {product_name}")
print(f"Revenue (before discount): ${revenue_before_discount:,.2f}")
print(f"Discounted Revenue: ${discounted_revenue:,.2f}")
print(f"Gross Margin: {gross_margin:.1%}")
print(f"Net Profit: ${net_profit:,.2f}")

# --- Exercise 7 ---
items_ordered = int(input("Enter number of items ordered: "))
full_boxes = items_ordered // 24
loose_items = items_ordered % 24
exact_fit = loose_items == 0
print(f"Full boxes: {full_boxes}, Loose items: {loose_items}, Exact fit: {exact_fit}")