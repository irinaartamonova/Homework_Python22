def is_year_leap(year):
    return "True" if year % 4 == 0 else "False"

year_to_check = 2024
result = is_year_leap(year_to_check)

print(f"Год{year_to_check}: {result}")
