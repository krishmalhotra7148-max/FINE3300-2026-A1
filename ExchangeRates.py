import csv 

class ExchangeRates:
    def __init__(self, filename):
        # open the file, find the USDCAD column, grab the last row's value
        with open(filename) as lebron_file:
            reader = csv.DictReader(lebron_file)
            for row in reader:
                self.rate = float(row['FXAUSDCAD'])

    def test(self):
        return self.rate
    
    def convert(self, amount, from_cur, to_cur):
        if from_cur == 'CAD' and to_cur == 'USD':
            return amount / self.rate
        elif from_cur == 'USD' and to_cur == "CAD":
            return amount * self.rate
        else:
            return amount

if __name__ == "__main__":
    lebron = ExchangeRates('BankOfCanadaExchangeRate.2026.csv')

    amount= float(input("Enter the amount: "))
    from_cur = input("From currency (USD or CAD): ")
    to_cur = input("To currency (USD or CAD): ")
   
    result = lebron.convert(amount, from_cur, to_cur)

print(f"{amount:,.2f} {from_cur} = {result:,.2f} {to_cur}")
      