class User:
    def __init__(self, user_id, username): #everytime we create a User(), we need to put in parameters
        self.id = user_id
        self.username = username
        self.followers = 0 #example like IG, all accounts created will start will default value of 0 followers
        self.following = 0 #so we do not need to put in the parameters, just set it to 0 and all creation
                           #will be 0 by default when created
    def follow(self, user):
        self.following+=1
        user.followers+=1


user_1 = User("001", "angela")
# print(user_1.id)
# print(user_1.username)

user_2 = User("002", "Micheal")
# print(user_2.id)
# print(user_2.username)

print(user_1.following) #following starts at 0
user_1.follow(user_2) #user 1 follows user 2
print(user_1.following) #after user 1 follows user 2, user 1 following +1
print(user_2.followers) #user 2 followers +1