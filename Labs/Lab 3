# Name: Natalie Zoladkiewicz
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS 115 Lab 3

def change(amount, coins):
    '''
        Returns the least number of coins needed to make the given
        amount of money.
    '''
    if amount == 0:
        return 0
    if coins==[]:
        return float("inf")
    amount1 = amount - coins[0]
    if amount1 < 0:
        return change(amount, coins[1:])
    return min(change(amount, coins[1:]), 1 + change(amount1, coins))
