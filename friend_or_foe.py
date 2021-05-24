def friend(x):
    return [friend for friend in x if len(friend) == 4  and not friend.isdigit()]

real_friends = friend(["Ryan", "Kieran", "Mark",])
print(real_friends)
