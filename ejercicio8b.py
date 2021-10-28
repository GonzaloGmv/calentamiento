investment_in_bitcoin = 1.2
bitcoin_to_euros = 25000

def bitcoinToEuros(bitcoin_amount, bitcoin_value_euros):
    euros_value = bitcoin_amount * bitcoin_value_euros
    return euros_value
    
investment_in_euros = bitcoinToEuros(investment_in_bitcoin, bitcoin_to_euros)
if investment_in_euros <= 30000:
    print("Investment below 30,000€! SELL!")
else: 
    print("Investment above 30,000€")