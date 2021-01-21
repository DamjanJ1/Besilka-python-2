import requests


class CurrencyConverter():
    def __init__(self,url):
        self.data= requests.get(url).json()
        self.currencies = self.data['rates']

    
    def convert(self, from_currency, to_currency, amount): 
        
        if from_currency != 'USD' : 
            amount = amount / self.currencies[from_currency] 
  
     
        amount = round(amount * self.currencies[to_currency], 4) 
        return amount

url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = CurrencyConverter(url)
print(converter.convert('EUR','USD',50))