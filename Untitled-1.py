'''
FINE 3300
Assignment - Part 1: Exchange Rates

Reads the Bank of Canada exchange rate file and converts an amount
between USD and CAD using the latest USD/CAD rate (last row of data).
'''

import csv


class ExchangeRates:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__usd_cad = self.__read_latest_rate()

    def __read_latest_rate(self):
        # Read every row of the CSV into a list
        with open(self.__file_name, newline='') as f:
            rows = list(csv.reader(f))

        # Find the data header row that contains the USD/CAD column.
        # FXUSDCAD also appears in the SERIES description section (as the
        # first cell), so we only accept a row where it's NOT the first column.
        header_index = None
        usd_col = None
        for i, row in enumerate(rows):
            if 'FXUSDCAD' in row and row.index('FXUSDCAD') > 0:
                header_index = i
                usd_col = row.index('FXUSDCAD')
                break

        if header_index is None:
            raise ValueError("Could not find the FXUSDCAD column in the file.")

        # Walk backwards from the bottom to get the latest (last) rate
        for row in reversed(rows[header_index + 1:]):
            if len(row) > usd_col and row[usd_col].strip() != '':
                return float(row[usd_col])

        raise ValueError("No USD/CAD rate found in the file.")

    def get_rate(self):
        return self.__usd_cad

    def convert(self, amount, from_currency, to_currency):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in ('USD', 'CAD') or to_currency not in ('USD', 'CAD'):
            raise ValueError("Currencies must be USD or CAD.")

        if from_currency == to_currency:
            return amount
        elif from_currency == 'USD':      # USD -> CAD
            return amount * self.__usd_cad
        else:                              # CAD -> USD
            return amount / self.__usd_cad


if __name__ == "__main__":
    rates = ExchangeRates('BankOfCanadaExchangeRates.2026.csv')
    print("Latest USD/CAD rate: {}".format(rates.get_rate()))

    # Prompt for the amount (keep asking until it's a valid number)
    while True:
        try:
            amount = float(input("Enter the amount: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    # Prompt for the currencies (keep asking until it's USD or CAD)
    from_currency = input("Convert FROM (USD or CAD): ").strip().upper()
    while from_currency not in ('USD', 'CAD'):
        from_currency = input("Invalid. Convert FROM (USD or CAD): ").strip().upper()

    to_currency = input("Convert TO (USD or CAD): ").strip().upper()
    while to_currency not in ('USD', 'CAD'):
        to_currency = input("Invalid. Convert TO (USD or CAD): ").strip().upper()

    result = rates.convert(amount, from_currency, to_currency)
    print("{:,.2f} {} = {:,.2f} {}".format(amount, from_currency, result, to_currency))