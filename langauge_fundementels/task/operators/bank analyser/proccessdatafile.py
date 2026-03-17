from csv import DictReader
class Analayser:
    def __init__(self):
        fr=open("langauge_fundementels\\task\\operators\\bank analyser\\bank_transactions_500_records.csv")
        self.transaction=list(DictReader(fr))
        print(len(self.transaction))
    def deb_transaction(self):
        for l in self.transaction:
            if l.get("type")=="debit":
                print(l)
    def cr_transaction(self):
        for t in self.transaction:
            if t.get("type")=="credit":
                print(t)
    def high_transactions(self): # amount > 75000
        for a in self.transaction:
            if int(a.get("amount")) > 75000:
                print("high value transation greater tha 75000:",a)
    def high_deb_transactions(self):
        debits = [d for d in self.transaction if d.get("type") == "debit"]
        max_amt = max(int(t.get("amount")) for t in debits)
        for d in debits:
            if int(d.get("amount")) == max_amt:
                print("highest debit transaction:", d)
    def high_credit_transactions(self):
        credits = [c for c in self.transaction if c.get("type") == "credit"]
        max_amt = max(int(t.get("amount")) for t in credits)
        for c in credits:
            if int(c.get("amount")) == max_amt:
                print("highest debit transaction:", c)

analysis=Analayser()
# analysis.deb_transaction()
# analysis.cr_transaction()
analysis.high_transactions()
analysis.deb_transaction()
analysis.high_credit_transactions()