import requests

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol]['quantity'] += quantity
        else:
            self.stocks[symbol] = {'quantity': quantity, 'price': self.get_stock_price(symbol)}

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            confirm = input(f"Are you sure you want to remove {quantity} shares of {symbol}? (yes/no): ").lower()
            if confirm == 'yes':
                if quantity >= self.stocks[symbol]['quantity']:
                    del self.stocks[symbol]
                else:
                    self.stocks[symbol]['quantity'] -= quantity
                print(f"{quantity} shares of {symbol} removed from portfolio.")
            else:
                print("Operation canceled.")
        else:
            print("Stock not found in portfolio")

    def get_stock_price(self, symbol):
        # You can replace this with any other financial API
        api_key = 'YOUR_ALPHA_VANTAGE_API_KEY'
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
        response = requests.get(url)
        data = response.json()
        if 'Global Quote' in data:
            return float(data['Global Quote']['05. price'])
        else:
            return None

    def portfolio_value(self):
        total_value = 0
        for symbol, data in self.stocks.items():
            total_value += data['quantity'] * data['price']
        return total_value

# Example usage
if __name__ == "__main__":
    portfolio = Portfolio()
    portfolio.add_stock('AAPL', 10)
    portfolio.add_stock('MSFT', 5)
    print("Portfolio Value:", portfolio.portfolio_value())
    portfolio.remove_stock('AAPL', 5)
    print("Portfolio Value after removing AAPL:", portfolio.portfolio_value())
