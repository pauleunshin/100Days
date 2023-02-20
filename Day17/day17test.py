class User:
    def __init__(self, user_id, username):
        #initialize attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("generating new user...")
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Robin")
print(user_1.id)





