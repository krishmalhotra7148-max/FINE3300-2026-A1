import csv 

class ExchangeRates:
    def __init__(self, filename):
        # Open the CSV file containing the exchange rates
        with open(filename) as lebron_file:
            # Read each row as a dictionary using the column names
            reader = csv.DictReader(lebron_file)
            # Go through each row in the CSV file
            for row in reader:
                # Store the exchange rate, updating it each row and the final value is the most recent rate
                self.rate = float(row['FXAUSDCAD'])

    def test(self):
        # Return the most recent exchange rate
        return self.rate
    
    def convert(self, amount, from_cur, to_cur):
        # Convert CAD to USD by dividing by the exchange rate
        if from_cur == 'CAD' and to_cur == 'USD':
            return amount / self.rate
        # Convert USD to CAD by multiplying by the exchange rate
        elif from_cur == 'USD' and to_cur == "CAD":
            return amount * self.rate
        # Return the original amount if neither condition is met
        else:
            return amount

# Run this code only when the file is executed directly
if __name__ == "__main__":
    lebron = ExchangeRates('BankOfCanadaExchangeRate.2026.csv')
    # Ask the user to enter the amount and convert it to a number
    amount= float(input("Enter the amount: "))
    # Ask the user which currencies they want to convert
    from_cur = input("From currency (USD or CAD): ")
    to_cur = input("To currency (USD or CAD): ")
    # Call the convert method to calculate the converted amount
    result = lebron.convert(amount, from_cur, to_cur)
# Display the conversion result with two decimal places
print(f"${amount:,.2f} {from_cur} = ${result:,.2f} {to_cur}")
      