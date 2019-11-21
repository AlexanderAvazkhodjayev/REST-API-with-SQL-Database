from user import User # Importing class User from user.py file
from werkzeug.security import safe_str_cmp # Used for python 2.0 versions to make sure string comparsion doesn't break


#Important notes about sets 
#Sets do not have duplicate values(important for unique usernames and ids)
#Elements in sets are not ordered
#You cannot access items in a set by index 
#	username_mapping = { u.username: u for u in users} #set comprehension - used to assign username(u.username) from user list(users).
#	userid_mapping = {u.id: u for u in users} #set comprehension - used to assign userid(u.uid) from user list(users).




#Retreive users using Username or UserId instead of iterating over list
def authenticate(username, password):
	user = User.find_by_username(username)
	if user and safe_str_cmp(user.password, password):
		return user

def identity(payload):
	user_id = payload['identity']
	return User.find_by_id(user_id)
