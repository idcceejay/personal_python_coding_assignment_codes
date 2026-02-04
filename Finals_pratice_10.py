class Stock:
    def __init__(self):
        self.list_prices = []

    def add_price(self, price: int):

        if price > 0:
            self.list_prices.append(price)
        return self.list_prices

    def determine_market_sentiment(self):

        if len(self.list_prices) < 2:
            return "Neutral"

        first = self.list_prices[0]
        last = self.list_prices[-1]

        if last > first:
            return "Positive"
        elif last < first:
            return "Negative"
        else:
            return "Neutral"
    
if __name__ == "__main__":

    stock = Stock()
    
    while True:
        user_input = input("Enter today's price (int) or '-done': ")

        if user_input == "-done":
            break

        
        price = int(user_input)
        stock.add_price(price)

    
    print(f"Valid Prices: {stock.add_price(price)}")

    
    sentiment = stock.determine_market_sentiment()
    print(f"Given the valid prices, the market felt {sentiment} about your stock.")