"""
**************** ฅ՞•ﻌ•՞ฅ *****************
* @author: Bruno Vitte @Tanque40 in github
* @version: 1.0
* @brief: Entry point for server side of the turbo message application
"""
import server.model.seed as db_seed
import server.model.user as user_model

if __name__ == "__main__":
	db_seed.execute_seed()
	user = user_model.User()
	print([row for row in user.get_all()])

