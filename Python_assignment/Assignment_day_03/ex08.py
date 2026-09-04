'''Scenario: An online shopping cart has duplicate items due to double-clicks: ["apple", "banana", "apple", "orange", "banana", "banana"]. Write a program that processes the list and removes all duplicate items, but keeps the first occurrence of each item in its original order. Print the cleaned cart.

Hardcoded Input: cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
Sample Output: ['apple', 'banana', 'orange']'''

def duplicating_cart():
    inp=["apple", "banana", "apple", "orange", "banana", "banana"]
    frq={}
    list=[]
    for i in inp:
        frq[i]=frq.get(i,0)+1
    for i in frq:
        if frq[i]>=1:
            inp.pop(inp.index(i))
            list.append(i)
    print(list,end=" ")
        
duplicating_cart()
