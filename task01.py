# Step 1: Get input from the user
steps_input = input("Enter the number of steps taken each day, separated by spaces: ")

# Step 2: Convert the input string into a list of integers
daily_steps = [int(step) for step in steps_input.split()]

# Step 3: Calculate the highest and lowest step counts
highest_steps = max(daily_steps)
lowest_steps = min(daily_steps)

# Step 4: Calculate the average daily step count
total_steps = sum(daily_steps)
average_steps = total_steps / len(daily_steps)

# Step 5: Sort the step counts in descending order
sorted_steps = sorted(daily_steps, reverse=True)

# Step 6: Print the results
print("Highest step count:", highest_steps)
print("Lowest step count:", lowest_steps)
print("Average daily step count:", average_steps)
print("Sorted step counts:", sorted_steps)