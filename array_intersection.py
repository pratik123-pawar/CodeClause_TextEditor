#!/usr/bin/env python3

# Define the arrays
a = [1, 3, 4, 6, 7, 9, 11, 12]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Find intersection (elements that appear in both arrays)
output = list(set(a) & set(b))
output.sort()  # Sort to match expected output order

print(f"Array a: {a}")
print(f"Array b: {b}")
print(f"Intersection: {output}")

# Alternative method using list comprehension
output_alt = [x for x in a if x in b]
print(f"Alternative method: {output_alt}")