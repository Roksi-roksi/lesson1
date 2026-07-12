def is_year_leap(year):
    return year % 4 == 0


year1 = 2024
result = is_year_leap(year1)

print(f"год {year1}: {result}")
