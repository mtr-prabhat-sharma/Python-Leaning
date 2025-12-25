bill = int(input("Enter bill amount: "))
number_of_friends = int(input("Enter number of friends: "))

total_bill = 0.2 * bill + bill

print("Your total bill including 20% Tax: ", 'Rs',total_bill)

shared_bill = total_bill / number_of_friends

print("Each person has to pay = ", 'Rs',shared_bill)

