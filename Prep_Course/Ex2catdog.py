human_years = input("Enter human years:")
humanYears = int(human_years)

if humanYears == 1:
    catYears = 15*(1)
    dogYears = 15*(1)
elif humanYears == 2:
    catYears = 15*(1) + 9*(1)
    dogYears = 15*(1) + 9*(1)
elif humanYears > 2:
    catYears = 15*(1) + 9*(1) + 4*(humanYears-2)
    dogYears = 15*(1) + 9*(1) + 5*(humanYears-2)

print(f"[{humanYears}, {catYears}, {dogYears}]")


