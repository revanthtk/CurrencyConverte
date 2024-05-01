#----------------------------------------CurrencyConverte----------------------------------------------------------------------------------
class CurrencyConverter:
    def __init__(self):
        
        self.exchange_rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.73,
            'JPY': 113.16,
            'INR': 74.25,
            'AUD': 1.32,
            
        }

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            return "Invalid currency"

        amount_in_usd = amount / self.exchange_rates[from_currency]
        converted_amount = amount_in_usd * self.exchange_rates[to_currency]
        return converted_amount

if __name__ == "__main__":
    converter = CurrencyConverter()

    while True:
        try:
            amount = float(input("Enter the amount: "))
            from_currency = input("Enter the source currency (e.g., USD, EUR, GBP,JPY,INR): ").upper()
            to_currency = input("Enter the target currency (e.g., USD, EUR, GBP,JPY,INR): ").upper()

            result = converter.convert(amount, from_currency, to_currency)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{amount} {from_currency} is equivalent to {result} {to_currency}")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        #----------------------------------------Thankyou-------------------------------------------
