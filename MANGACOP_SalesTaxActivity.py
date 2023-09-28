# Prompt the user to enter purchase amount
purchase_amount = float(input("Enter the purchase amount: "))

# Calculate sales tax 
sales_tax_rate = 0.06 
sales_tax = purchase_amount * sales_tax_rate

# Display the salestax
print(f"Sales Tax (6%): {sales_tax:.2f}")