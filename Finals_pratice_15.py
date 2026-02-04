class Spending_tracker():
    def __init__(self):
        self.amounts = []

    def add_amount(self, amount: int):
        if amount > 0:
            self.amounts.append(amount)
        

    def total_spent(self):
        
        return sum(self.amounts)
        
    def spending_level(self):

        if len(self.amounts) < 2:
            return "Insufficient Data"
        
        total = self.total_spent()

        if total < 20:
            return "Very Frugal"
        
        elif 20 <= total <= 49:
            return "Frugal"
        
        elif 50 <= total <= 99:
            return "Average Spender"
        
        else:
            return "Big Spender"
        
    def __str__(self):
        
        return f"""Valid Spending entries: {self.amounts}\n
        Total spent: {self.add_amount}"""

if __name__ == "__main__":

    sp = Spending_tracker()


    while True:
        amount = input("Amount(-done): ")

        if amount == "-done":
            break

        amount_int = int(amount)
        sp.add_amount(amount_int)
        
        word = sp.spending_level()
        print(sp) 
        print(f"Your spending level is: {word}")
    




        