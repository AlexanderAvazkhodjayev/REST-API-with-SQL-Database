from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

#from security.py file which contains two functions authenticate and identity
from security import authenticate, identity
from user import UserRegister 
from item import Item, ItemList


app = Flask(__name__)
app.secret_key = 'Kyle'
api = Api(app)


#allows for the authenication and identity of users
#creates endpoint /auth
jwt = JWT(app, authenticate, identity) 




api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
	app.run(debug=True)