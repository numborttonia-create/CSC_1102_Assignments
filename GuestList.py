# Exercise 3-4: Guest List
guests = ['John', 'Alice', 'Bob']
print("Exercise 3-4: Guest List")
for guest in guests:
    print(f"Dear {guest}, you're invited to dinner!")

# Exercise 3-5: Changing Guest List
print("\nExercise 3-5: Changing Guest List")
print(f"Unfortunately, {guests[1]} can't make it.")
guests[1] = 'Charlie'
for guest in guests:
    print(f"Dear {guest}, you're invited to dinner!")

# Exercise 3-6: More Guests
print("\nExercise 3-6: More Guests")
print("We found a bigger table!")
guests.insert(0, 'Eve')
guests.insert(2, 'Mike')
guests.append('Sarah')
for guest in guests:
    print(f"Dear {guest}, you're invited to dinner!")

# Exercise 3-7: Shrinking Guest List
print("\nExercise 3-7: Shrinking Guest List")
print("Sorry, we can only invite two people.")
while len(guests) > 2:
    guest = guests.pop()
    print(f"Sorry {guest}, you're not invited.")
for guest in guests:
    print(f"Dear {guest}, you're still invited!")
del guests[0]
del guests[0]
print("Final Guest List:", guests)
