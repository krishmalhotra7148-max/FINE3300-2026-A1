"""
ExchangeRatesAI.py
Converts an amount between USD and CAD using the latest USD/CAD rate
from the Bank of Canada exchange rate CSV file.
"""

import csv
import os


class ExchangeRates:
    """Loads a Bank of Canada exchange rate file and converts between USD and CAD."""

    RATE_COLUMN = "FXAUSDCAD"  # 1 USD = this many CAD

    def __init__(self, filename):
        self.filename = filename
        self.date, self.usd_cad = self._load_latest_rate()

    def _load_latest_rate(self):
        # utf-8-sig strips the invisible BOM character at the start of the file
        with open(self.filename, newline="", encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))

        if not rows:
            raise ValueError("The exchange rate file has no data rows.")

        latest = rows[-1]  # last row = most recent rate
        rate_text = latest.get(self.RATE_COLUMN, "").strip()
        if not rate_text:
            raise ValueError(f"No {self.RATE_COLUMN} value in the last row.")

        return latest["Date"], float(rate_text)

    def convert(self, amount, from_currency, to_currency):
        """Convert amount from one currency (USD or CAD) to the other."""
        from_currency = from_currency.strip().upper()
        to_currency = to_currency.strip().upper()
        valid = {"USD", "CAD"}

        if from_currency not in valid or to_currency not in valid:
            raise ValueError("Currencies must be USD or CAD.")

        if from_currency == to_currency:
            return amount
        if from_currency == "USD":       # USD -> CAD: multiply
            return amount * self.usd_cad
        return amount / self.usd_cad     # CAD -> USD: divide


def main():
    # Look for the CSV in the same folder as this script
    folder = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(folder, "BankOfCanadaExchangeRate.2026.csv")
    rates = ExchangeRates(csv_path)
    print(f"Latest USD/CAD rate ({rates.date}): 1 USD = {rates.usd_cad} CAD\n")

    while True:
        try:
            amount = float(input("Enter the amount: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        from_cur = input("Convert FROM (USD or CAD): ").strip().upper()
        if from_cur in ("USD", "CAD"):
            break
        print("Please enter USD or CAD.")

    while True:
        to_cur = input("Convert TO (USD or CAD): ").strip().upper()
        if to_cur in ("USD", "CAD"):
            break
        print("Please enter USD or CAD.")

    result = rates.convert(amount, from_cur, to_cur)
    print(f"\n${amount:,.2f} {from_cur} = ${result:,.2f} {to_cur}")


if __name__ == "__main__":
    main()