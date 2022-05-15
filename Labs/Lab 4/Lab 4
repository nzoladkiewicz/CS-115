# Name: Natalie Zoladkiewicz
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS 115 Lab 4

def knapsack(capacity, itemList):
    '''
        Returns the maximum value and list of items to steal without
        exceeding the capacity of the knapsack.
    '''
    if capacity == 0 or itemList == []:
        return [0,[]]
    elif itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    else:
        itemVal = itemList[0][1]
        checkItem = knapsack(capacity - itemList[0][0], itemList[1:])
        use_it = [itemVal + checkItem[0], [itemList[0]] + checkItem[1]]
        lose_it = knapsack(capacity, itemList[1:])
        return max(use_it, lose_it)
