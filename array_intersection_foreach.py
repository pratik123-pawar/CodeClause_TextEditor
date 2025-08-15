#!/usr/bin/env python3

# Define the arrays
a = [1, 3, 4, 6, 7, 9, 11, 12]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Find intersection using only for loops
output = []

# For each element in array a
for element_a in a:
    # Check if it exists in array b using nested for loop
    found = False
    for element_b in b:
        if element_a == element_b:
            found = True
            break  # Found match, no need to continue checking
    
    # If found in b, check if it's already in output to avoid duplicates
    if found:
        already_exists = False
        for existing in output:
            if existing == element_a:
                already_exists = True
                break
        
        # Add to output only if not already there
        if not already_exists:
            output.append(element_a)

print(f"Array a: {a}")
print(f"Array b: {b}")
print(f"Intersection using only for loops: {output}")

# Alternative approach - check each element of b against a
print("\n--- Alternative approach ---")
output2 = []

for element_b in b:
    # Check if it exists in array a
    found = False
    for element_a in a:
        if element_b == element_a:
            found = True
            break
    
    # If found, add to output (avoiding duplicates)
    if found:
        already_exists = False
        for existing in output2:
            if existing == element_b:
                already_exists = True
                break
        
        if not already_exists:
            output2.append(element_b)

print(f"Alternative result: {output2}")