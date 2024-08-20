initial_investment = float(input("Enter in initial amount: "))
interest = float(input("Enter in interest in %: ")) / 100 + 1
years = int(input("Enter in years: "))

result = initial_investment * (interest ** years)

print("Your investment in {years} years will be {result}kr".format(years=years, result=result))
