
class Stock():
    def __init__(self, title, price, name):
        self.title = title
        self.price = price
        self.name = name

    def get_description(self):
        return f"{self.title}: {self.name} -- ${self.price}"


msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock("GOOG", 135.0, "Google Inc")
meta= Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("AMZN", 135.0, "Amazon Inc")

print(msft.get_description())
print(goog.get_description())
print(meta.get_description())
print(amzn.get_description())