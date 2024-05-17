from ..model import seed as db_seed
from ..model import user as user_model

class UserController:
	def __init__(self):
		db_seed.execute_seed()
		self.user = user_model.User()
		print([row for row in self.user.get_all()])

	def new_user(self, id = 0, name="", last_name = "", email="", password=""):
		self.user = user_model.User(id = id, name = name, last_name = last_name, email = email, password=password)