class Category:

    #
    ledger = []
    name = ""

    #  
    def __init__(self, n) :
        self.name = n
        self.ledger = []

    # 
    def deposit(self, amount, desc = "") :
        self.ledger.append({"amount": float(amount), "description": desc})
    
    #
    def withdraw(self, amount, desc = "") :
        if (self.check_funds(amount)) :
            self.ledger.append({"amount": float(-abs(amount)), "description": desc})
            return True
        else :
            return False

    #
    def get_balance(self) :
        balance = 0
        for item in self.ledger :
            balance = balance + float(item['amount'])
        return float(balance)

    #
    def transfer(self, amount, cat) :
        if (self.check_funds(amount)) :
            self.withdraw(amount, f"""Transfer to {cat.name}""")
            cat.deposit(amount, f"""Transfer from {self.name}""")
            return True
        else :
            return False

    #
    def check_funds(self, amount) :
        funds = 0
        for item in self.ledger :
            funds = funds + float(item['amount'])
        if amount > funds :
            return False
        else :
            return True

    #
    def __str__(self) :

        #
        res = ''
        len_star = int((30 - len(self.name)) / 2)
        total = 0

        #
        for item in self.ledger :
            total = total + item['amount']
        for i in range(len_star) :
            res = res + '*'
        res = res + self.name
        for i in range(len_star) :
            res = res + '*'
        res = res + '\n'

        #
        for item in self.ledger :
            desc_len = len(item['description'])
            amount_len = len(f'{item["amount"]:.2f}')
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
                res = res + f'{item["amount"]:.2f}'
            else :
                for i in range(7) :
                    res = res + f'{item["amount"]:.2f}'[i]
            res = res + '\n'

        #    
        res = res + f'Total: {total}'
   
        return res

def create_spend_chart(categories):

    #
    total_spent = 0
    spent_by_cat = {}
    percentages = []

    # get info to calculate percentage 
    for item in categories :
        for obj in item.ledger :
            if obj['amount'] < 0 :
                total_spent = total_spent + abs(obj['amount'])
                spent_by_cat[item.name] = abs(obj['amount'])
    
    # calculate percentages
    for k,v in spent_by_cat.items() :
        percentages.append(((v * 100 / total_spent), k))
    
    # Begin chart (first 12 lines)
    count = 100
    res = 'Percentage spent by category\n'
    for i in range(11) :
        if len(str(count)) == 3 :
            res = res + str(count) + '| '
        elif len(str(count)) == 2 :
            res = res + f' {count}| '
        elif len(str(count)) == 1 :
            res = res + f'  {count}| '
        for item in percentages :
            if item[0] >= count :
                res = res + 'o'
            else :
                res = res + ' '
            res = res +'  '
        res = res + '\n'
        count = count - 10
    
    # Horizontal line
    res = res + '    '
    for i in range(((len(percentages) * 2) + len(percentages) + 1)) :
        res = res + '-'
    res = res + '\n'
    
    # calculate final num of lines
    max_len = ''
    for i in percentages :
        if len(i[1]) > len(max_len) :
            max_len = i[1]

    # category displayed vertically
    for i in range(len(max_len)) :
        res = res + '     '
        for item in percentages :
            try :
                res = res + item[1][i]
            except :
                res = res + ' '
            res = res + '  '
        if i + 1 < len(max_len) :
            res = res + '\n'
        
    return res