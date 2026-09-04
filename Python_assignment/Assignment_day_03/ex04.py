'''Exercise 4: Nightclub VIP Queue
Scenario: A nightclub bouncer maintains a list of VIP guests who are allowed inside: ["Guido", "Esha", "Rajan", "Kishori"]. As guests arrive at the door, the bouncer prompts the user to enter their name.

If the guest is on the VIP list, move them from their current position in the queue and insert them at the front of the queue (index 0).
If the guest is not on the VIP list, print "Access denied. Not on the VIP list." and do not modify the list. 
Run this program in a loop. The loop should stop when the user types "exit". Print the updated queue state after each guest arrives.
Sample Walkthrough:
Current VIP queue: ['Guido', 'Esha', 'Rajan', 'Kishori']
Enter guest name: Rajan
Rajan moved to the front!
Current VIP queue: ['Rajan', 'Guido', 'Esha', 'Kishori']

Enter guest name: Vinod
Access denied. Not on the VIP list.
Current VIP queue: ['Rajan', 'Guido', 'Esha', 'Kishori']

Enter guest name: exit'''
def night_club():
    list=["Guido", "Esha", "Rajan", "Kishori"]
    list1=list.copy()
    str=input("Enter your guest name:").title()
    while str!='Exit':
        if str in list:
          pop_id=list1.index(str)
          list1.pop(pop_id)
          list1.insert(0,str)
          print(f"{str} moved to the front ")
          print(f"current VIP queue: {list1}")
        else:
           print("Access denied.Not on the VIP list ")
        str=input("Enter your guest name:").title()
      
    print(f"Current VIP queue:{list}")
night_club()

