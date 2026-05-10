# Project 1 — Temperature Converter
# Author: your name here
# Date:   session date here
#
# Instructions:
#   1. Read the README.md in this folder first.
#   2. Fill in the missing lines below.
#   3. Test with: 0°C → 32°F | 100°C → 212°F | -40°C → -40°F

# ── Your solution goes here ───────────────────────────────────────────────────

celsius = float(input("Enter temperature in Celsius: "))

# TODO: calculate fahrenheit using the formula F = (C × 9/5) + 32
# fahrenheit = ...

# TODO: print the result using an f-string
# print(f"...")

# ── Bonus (optional) ─────────────────────────────────────────────────────────
# Add a direction menu (C→F or F→C)

# Project 1 - Temperature Converter
# Author: Seid Mamuti
# Get input from the user and convert it to float
celsius = float(input("Enter temperature in Celsius: "))
# Apply the formula: F = (C x 9/5) + 32
fahrenheit = (celsius * 9 / 5) + 32
# Print the result using an f-string
print(f"{celsius:.1f}\u00b0C = {fahrenheit:.1f}\u00b0F")

