class Account:
    def __init__(self, name, revenue):
        self.name = name
        self.revenue = revenue
    def display(self):
        print(self.name, self.revenue)

###Input for one object
# name_input = input("Name of client:")
# revenue_input = int(input("Amount of revenue:"))
# acc = Account(name_input,revenue_input)
# acc.display()

acc1 = Account("Google", 10000)
acc2 = Account("Apple", 45000)
acc3 = Account("Tesla", 27600)
accounts = [acc1,acc2,acc3]

for acc in accounts:
    acc.display()




# Account('revenue', revenue_input)

# print(acc.name)
# print(acc.revenue)


