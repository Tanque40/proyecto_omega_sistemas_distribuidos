"""
**************** ฅ՞•ﻌ•՞ฅ *****************
* @author: Bruno Vitte @Tanque40 in github
* @version: 1.0
* @brief: Entry point for client side of the turbo message application
"""

import dearpygui.dearpygui as dpg
import lib.constants as constants
import grpc
import turbomessage_pb2
import turbomessage_pb2_grpc

dpg.create_context()
dpg.create_viewport(title='TurboMessage', width=constants.WIDTH, height=constants.HEIGHT)

dpg_window = dpg.generate_uuid()

def print_me(sender):
	print(f"Menu Item: {sender}")

def test_connection(email):
	print("Aqui si jala")
	print(email)

def change_window(one):
	dpg.delete_item(dpg_window, children_only=True) # clean the window from the past interface
	print(one)
	render_second_window(parent=dpg_window)

def render_second_window(parent=0):
	with dpg.group(horizontal=False, parent=parent) as group:
		email = dpg.add_input_text(label="Correo")
		dpg.add_text("Hello, world", parent=group)
		dpg.add_button(label="Save", callback=test_connection(email), parent=group)
		dpg.add_input_text(label="string", default_value="Quick brown fox", parent=group)
		dpg.add_slider_float(label="float", default_value=0.273, max_value=1, parent=group)

def render_login(parent = 0):
	with dpg.group(horizontal=False, parent=parent) as group:
		email = dpg.add_input_text(label="Correo")

		with dpg.menu(label="Widget Items"):
			dpg.add_checkbox(label="Pick Me", callback=print_me)
			dpg.add_button(label="Press Me", callback=change_window(email))
			dpg.add_color_picker(label="Color Me", callback=print_me)

with dpg.window(
		tag=dpg_window,
		label="TurboMessage",
		width=constants.WIDTH,
		height=constants.HEIGHT,
		no_collapse=True,
		no_close=True
	):
	render_login()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

"""
import dearpygui.dearpygui as dpg

dpg.create_context()

dpg.create_viewport()

# I just feel more comfortable working with variables instead of string/ing tags

dpg_window = dpg.generate_uuid()

def render_main_window(parent=0):

	with dpg.group(horizontal=True, parent=parent) as group:

		dpg.add_text('This is the main window!', parent=group)

		dpg.add_text('Test', parent=group)

def login():

	dpg.delete_item(dpg_window, children_only=True) # clean the window from the past interface

	render_main_window(parent=dpg_window)

def render_login_window(parent=0):

	dpg.add_button(label='Login', callback=login, parent=parent)

	with dpg.group(horizontal=True, parent=parent) as group:

		dpg.add_text('1', parent=group)

		dpg.add_text('2', parent=group)

with dpg.window(tag=dpg_window):
	render_login_window()

dpg.setup_dearpygui()

dpg.show_viewport()

dpg.start_dearpygui()

dpg.destroy_context()

"""