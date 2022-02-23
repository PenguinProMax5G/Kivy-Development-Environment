import json
import webbrowser
from copy import deepcopy
from random import choice
from typing import Any
from kivy.metrics import cm, dp, inch, mm, pt, sp
from kivy.utils import get_color_from_hex
import darkdetect

def open_link(link):
    webbrowser.open(link)


def get_color_from_text(color_name:str):

    with open(r"base\json\colors.json", "r") as colors:
        json_colors = json.load(colors)
        
        for color in json_colors:
            if color["name"] == color_name.upper():
                return color["hex"]
        
        return color_name



def change_theme(app_instance):

    path = r"base\json\config.json"

    with open(path, "r+") as json_cache:

        data = json.load(json_cache)

        if app_instance.theme_cls.theme_style == "Dark":

            data["THEME_STYLE"] = "Light"
            json_cache.seek(0)
            json.dump(data, json_cache)
            json_cache.truncate()

            app_instance.theme_cls.theme_style = "Light"
            app_instance.tooltip_bg_color = get_color_from_hex(get_color_from_text("Black"))
            app_instance.tooltip_text_color = get_color_from_hex(get_color_from_text("White"))

        else:

            data["THEME_STYLE"] = "Dark"
            json_cache.seek(0)
            json.dump(data, json_cache)
            json_cache.truncate()


            app_instance.theme_cls.theme_style = 'Dark'
            app_instance.tooltip_bg_color = get_color_from_hex(get_color_from_text("White"))
            app_instance.tooltip_text_color = get_color_from_hex(get_color_from_text("Black"))



def return_theme():

    with open(r"base\json\config.json") as cache:
        json_cache = json.load(cache)

        return json_cache["THEME_STYLE"]
