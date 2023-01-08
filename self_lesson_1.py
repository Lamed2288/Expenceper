income_per_mounth = int(input('Input your income per mounth:'))
expence_per_mounth = int(input('Input your expence per mounth:'))
bal_mounth = (income_per_mounth - expence_per_mounth)

income_per_week = income_per_mounth / 4
expence_per_week = expence_per_mounth / 4
bal_week = (income_per_week-expence_per_week)

income_per_year = income_per_mounth * 12
expence_per_year = expence_per_mounth * 12
bal_year = (income_per_year - expence_per_year)


income_per_day = income_per_year / 365
expence_per_day = expence_per_year / 365
bal_day = (income_per_day-expence_per_day)

a = income_per_year - expence_per_year
b = income_per_mounth - expence_per_mounth
c = income_per_week - expence_per_week
d = income_per_day - expence_per_day 

print('My balance per year:' + str(a))
print('My balance per mounth:'+ str(b))
print('My balance per week:' + str(c))
print('My balance per day:'+ str (d))
