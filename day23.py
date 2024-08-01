# https://codingbat.com/python/Warmup-1

class InstagramProfile:
    def __init__(self,user_name,password,mail_id):
        self.user_name = user_name
        self.password = password
        self.mail_id = mail_id
        self.following = 0
        self.followers = 0
    def follow(self,other_user):
        if self==other_user:
            print("Same user will not able to follow")
        else:
            if self.user_name == other_user.user_name:
                print("Username should be different ")
            else:
                self.following+=1
                other_user.followers+=1
    def unfollow(self,other_user):
        if self==other_user:
            print("Same user will not able to follow")
        else:
            if self.user_name == other_user.user_name:
                print("Username should be different ")
            else:
                if self.following>0 and other_user.followers>0:
                    self.following-=1
                    other_user.followers-=1
                else:
                    print("Unable to unfollow")
    def displayinfo(self):
        print(f'Username : {self.user_name}\nPassword : {self.password}\nMail id : {self.mail_id}\nFollowers {self.followers}\nFollowing : {self.following}')
user1 = InstagramProfile("User1","User_123","user1@gmail.com")
user2 = InstagramProfile("User2","1234","user2@gmail.com")
user3 = InstagramProfile("User3","1234","user3@gmail.com")
print("Follow")
user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user3.follow(user1)
print("start..")
user1.displayinfo()
print("---------------------------------------")
user2.displayinfo()
print("---------------------------------------")
user3.displayinfo()
# print("\nUnFollow")
# user1.unfollow(user2)
# user2.unfollow(user1)
# user1.displayinfo()
# print("---------------------------------------")
# user2.displayinfo()
#after completing codingbat questions
#try these two
#1. leetcode
#2. hackerrank
