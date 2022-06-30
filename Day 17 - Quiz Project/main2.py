# how to create a class

# class User:  # class name 1st letter must be uppercase.
#     pass
#
#
# user_1 = User()
# user_1.id = '001'  # creating an attribute called id.
# user_1.username = 'angela'  # creating a username called username
#
# print(user_1.id)
# print(user_1.username)
#
# user_2 = User()
# user_2.id = '002'  # creating an attribute called id.
# user_2.username = 'jack'  # creating a username called username
#
# print(user_2.id)
# print(user_2.username)
#
# print('-------------------------------------------------------------------')


# above method is tedious. alternative approach is to create a CONSTRUCTOR and to intialise itself.
# example
class Car:
    def __init__(self):
        pass
        # initialise the attributes


class User:
    def __init__(self):
        print('new user created.')


user_1 = User()
user_1.id = '001'  # creating an attribute called id.
user_1.username = 'angela'  # creating a username called username

print(user_1.id)
print(user_1.username)

user_2 = User()
user_2.id = '002'  # creating an attribute called id.
user_2.username = 'jack'  # creating a username called username

print(user_2.id)
print(user_2.username)

print('-------------------------------------------------------------------')

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user_3 = User('003', 'bauer')
user_4 = User('004', 'vinoth')

#print(user_4.id, user_4.username, user_4.following, user_4.followers)


user_3.follow(user_4) # -> user_3.follow (calling the method aka the function which is already declared in the User class.
print(user_3.followers)
print(user_3.following)

print(user_4.followers)
print(user_4.following)