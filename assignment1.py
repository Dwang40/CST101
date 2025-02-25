name = input("Enter your name: ")
hours_worked = int(input("Enter the total number of hours you work weekly: "))
pay_rate = int(input("Enter your hourly pay rate: "))
week = hours_worked * pay_rate
print(name, ", you make", week, "dollars every week.")
