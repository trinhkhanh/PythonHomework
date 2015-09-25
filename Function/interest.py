__author__ = 'trinhkhanh'
def calInterest(amount, rate, months ):

    amountInterest = amount
    for i in range(months):
        amountInterest += amountInterest*rate

    return (amountInterest, amountInterest - amount)

print (calInterest(2000000, 0.01, 4))

