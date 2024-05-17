"""
**************** ฅ՞•ﻌ•՞ฅ *****************
* @author: Bruno Vitte @Tanque40 in github
* @version: 1.0
* @brief: Entry point for server side of the turbo message application
"""
import server.controller.user_controller as user_controller
from concurrent import futures
import grpc
import turbomessage_pb2 as turbomessage_pb2
import turbomessage_pb2_grpc as turbomessage_pb2_grpc
import lib.constants as constants

class TurboMessageAuthenticator(turbomessage_pb2_grpc.AuthenticatorServicer):
	def new_user(self, New_User_Data):
		return Status
	
	def authenticate(self, User_Data):
		return Status

class TurboMessageEmailServer(turbomessage_pb2_grpc.EmailServerServicer):
	def send_email(self, Email_Data):
		return Status

	def recive_emails(self, User_Email):
		return Email_Response

	def mark_as_read(self, Email_Data):
		return Status

if __name__ == "__main__":
	print("Email server started")
	userController = user_controller.UserController()
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))
	turbomessage_pb2_grpc.add_AuthenticatorServicer_to_server(TurboMessageAuthenticator(), server)
	turbomessage_pb2_grpc.add_EmailServerServicer_to_server(TurboMessageEmailServer(), server)
	server.add_insecure_port("[::]:" + constants.PORT)
	server.start()
	server.wait_for_termination()

