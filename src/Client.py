"""
**************** ฅ՞•ﻌ•՞ฅ *****************
* @author: Bruno Vitte @Tanque40 in github
* @version: 1.0
* @brief: Entry point for client side of the turbo message application
"""

import dearpygui.dearpygui as dpg
import lib.constants as constants

dpg.create_context()

dpg.create_viewport(title='Custom Title', width=constants.WIDTH, height=constants.HEIGHT)

def print_me(sender):
    print(f"Menu Item: {sender}")

with dpg.window(label="Tutorial", width=constants.WIDTH, height=constants.HEIGHT):
    with dpg.menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Save", callback=print_me)
            dpg.add_menu_item(label="Save As", callback=print_me)

            with dpg.menu(label="Settings"):
                dpg.add_menu_item(label="Setting 1", callback=print_me, check=True)
                dpg.add_menu_item(label="Setting 2", callback=print_me)

        dpg.add_menu_item(label="Help", callback=print_me)

        with dpg.menu(label="Widget Items"):
            dpg.add_checkbox(label="Pick Me", callback=print_me)
            dpg.add_button(label="Press Me", callback=print_me)
            dpg.add_color_picker(label="Color Me", callback=print_me)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()