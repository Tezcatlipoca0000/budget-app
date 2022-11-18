class Category:
    ledger = []
    name = ""

    def __init__(self, n) :
        self.name = n

    def deposit(self, amount, desc = "") :
        self.ledger.append({"amount": amount, "description": desc})
    
    def withdraw(self, amount, desc = "") :
        if (self.check_funds(amount)) :
            self.ledger.append({"amount": -abs(amount), "description": desc})

    def get_balance(self) :
        balance = 0
        for item in self.ledger :
            balance = balance + item['amount']
        return balance

    def transfer(self, amount, cat) :
        if (self.check_funds(amount)) :
            self.withdraw(amount, f"""Transfer to {cat.name}""")
            cat.deposit(amount, f"""Transfer from {self.name}""")
            return True
        else :
            return False

    def check_funds(self, amount) :
        funds = 0
        for item in self.ledger :
            funds = funds + item['amount']
        if amount > funds :
            return False
        else :
            return True

    def __str__(self) :
        res = ''
        len_star = int((30 - len(self.name)) / 2)
        for i in range(len_star) :
            res = res + '*'
        res = res + self.name
        for i in range(len_star) :
            res = res + '*'
        res = res + '\n'
        for item in self.ledger :
            desc_len = len(item['description'])
            amount_len = len(str(item['amount']))
            if desc_len < 23 :
                res = res + item['description']
                for i in range(23 - desc_len) :
                    res = res + ' '
            else :
                for i in range(23) :
                    res = res + item['description'][i]
            if amount_len < 7 :
                for i in range(7 - amount_len) :
                    res = res + ' '
                res = res + str(item['amount'])
            else :
                for i in range(7) :
                    res = res + str(item['amount'])[i]
            res = res + '\n'

            
        return res

def create_spend_chart(categories):
    f = ''