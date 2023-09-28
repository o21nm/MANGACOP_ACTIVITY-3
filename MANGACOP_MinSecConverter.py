# Get input
seconds = int(input("Enter an integer in seconds: "))

# Calculate minutes and remaining seconds
minutes = seconds // 60
remaining_seconds = seconds % 60

# Result
print(f"{seconds} seconds is {minutes} minutes and {remaining_seconds} seconds")