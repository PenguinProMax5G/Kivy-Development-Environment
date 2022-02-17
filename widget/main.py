from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.metrics import sp
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from random import choice
import os
from plyer import filechooser
from scripts.script import *


class MDTab(MDFloatLayout, MDTabsBase):
    pass

class PlayGround(MDTab):
    pass 



class Output(MDTab):
    path = r"kv-files\btn.kv"
    Builder.load_file(path)




class KDEWidgetPlayGroundApp(MDApp):
    
    # Vars

    width_num = ObjectProperty(255)
    height_num = ObjectProperty(255)
    text = ObjectProperty("Change ME!")
    background_color = ObjectProperty(get_color_from_hex(get_color_from_text("Sienna")))
    pos_x = ObjectProperty(150)
    pos_y = ObjectProperty(150)
    disabled = ObjectProperty(False)
    font_size = ObjectProperty("12sp")
    font = ObjectProperty("Roboto")
    path = ObjectProperty("")
    text_color = ObjectProperty(get_color_from_hex(get_color_from_text("White")))
    
    
    path_to_kv_file = r'kv-files\playground.kv'


    def open_file_manager(self):
        filechooser.open_file(title="Choose Font", filters=['*.ttf', '*.otf', '*.ttc'], on_selection=self.return_path)

    def return_path(self, path):
        OK_BTN = MDFlatButton(
            text="OK",
            theme_text_color="Custom",
            text_color=self.theme_cls.primary_dark
        )

        self.load_dialog = MDDialog(
            title="Font Loaded Successfully",
            text=f"The location of the font file is {path[0]}",
            buttons=[
                OK_BTN
            ]
        )
        OK_BTN.bind(on_press=self.load_dialog.dismiss)
        self.load_dialog.open()
        self.font = path[0]

    def change_palette(self):
        palettes = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        accent_palettes = ["Blue", "Red", "Yellow"]
        
        palette = choice(palettes)
        accent = choice(accent_palettes)

        self.theme_cls.primary_palette = f"{palette}"
        self.theme_cls.accent_palette = f"{accent}"

        self.dialog.title = f"Using theme: {palette}"
        self.dialog.text = f"The primary pallette has been changed to {palette} & the accent palette has been changed {accent}."
        self.CANCEL_BTN.text = "CANCEL"
        self.CANCEL_BTN.bind(on_press=lambda revert: self.revert())

        self.dialog.open()

    def revert(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.dialog.dismiss()

    def build(self):
        palettes = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        accent_palettes = ["Blue", "Red", "Yellow"]

        self.rand_accent = choice(accent_palettes)
        self.rand_palette = choice(palettes)

        os.environ["KIVY_PROFILE_LANG"] = "1"

        self.theme_cls.primary_palette = f"{self.rand_palette}"
        self.theme_cls.accent_palette = f"{self.rand_accent}"

        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        self.title = "Widget Playground"

        return Builder.load_file(self.path_to_kv_file)
    

    def on_start(self):
        self.root.ids.tabs.add_widget(PlayGround(title="Playground"))
        self.root.ids.tabs.add_widget(Output(title="Output"))

        print(f"Using theme: {self.theme_cls.primary_palette}")

        self.OK_BTN = MDFlatButton(
            text="OK",
            theme_text_color="Custom",
            text_color=self.theme_cls.primary_dark
        )
        self.CANCEL_BTN = MDFlatButton(
            text="REVERT",
            theme_text_color="Custom",
            text_color=self.theme_cls.error_color
        )

        self.dialog = MDDialog(
            title=f"Using theme: {self.theme_cls.primary_palette}",
            text=f"The primary pallette has been changed to {self.theme_cls.primary_palette} & the accent palette has been change to {self.theme_cls.accent_palette}.",
            buttons=(self.OK_BTN, self.CANCEL_BTN)

        )
        self.OK_BTN.bind(on_press=self.dialog.dismiss)

        def cancel():
            self.theme_cls.primary_palette = "BlueGray"
            self.dialog.dismiss()
        
        self.CANCEL_BTN.bind(on_press=lambda revert: cancel())
    
        self.dialog.open()

    # TEXTFIELD  EVENTS
    def set_property(self, instance, type):

        # Set the width of the button.
        if type == "width":
            try:
                width = instance.text
                if width == "":
                    self.width_num = sp(200)
                
                else:
                    self.width_num = sp(eval(width))


            except Exception as tb:
                self.width_num = sp(eval(width))
        
        # Set the height of the button.
        elif type == "height":
            try:
                height = instance.text
                if height == "":
                    self.height_num = sp(eval(height))
                
                else:
                    self.height_num = sp(eval(height))
            except Exception as tb:
                self.height_num = sp(eval(height))

        # Set the text of the button
        
        elif type == "text":
            try:
                text = instance.text
                if text == "":
                    self.text = "Change ME!"

                else:
                    self.text = f"{text}"
            except Exception as tb:
                self.text = "Change ME!"
        
        elif type == "bg_color":
            try:
                bg_text_input = instance.text
                keywords = [
                    "primary_light",
                    "primary_dark",
                    "primary_color",
                    "accent_color",
                    "accent_light",
                    "accent_dark",
                    "bg_darkest",
                    "opposite_bg_darkest",
                    "bg_dark",
                    "opposite_bg_dark",
                    "bg_normal",
                    "opposite_bg_normal",
                    "bg_light",
                    "opposite_bg_light",

                ]
                funcs = {
                    "primary_light": self.theme_cls.primary_light,
                    "primary_dark": self.theme_cls.primary_dark,
                    "primary_color": self.theme_cls.primary_color,
                    "accent_color": self.theme_cls.accent_color,
                    "accent_light": self.theme_cls.accent_light,
                    "accent_dark": self.theme_cls.accent_dark,
                    "bg_darkest": self.theme_cls.bg_darkest,
                    "opposite_bg_darkest": self.theme_cls.opposite_bg_darkest,
                    "bg_dark": self.theme_cls.bg_dark,
                    "opposite_bg_dark": self.theme_cls.opposite_bg_dark,
                    "bg_normal": self.theme_cls.bg_normal,
                    "opposite_bg_normal": self.theme_cls.opposite_bg_normal,
                    "bg_light": self.theme_cls.bg_light,
                    "opposite_bg_light": self.theme_cls.opposite_bg_light,
                }

                try:
                    color = funcs[bg_text_input.lower()]
                    self.background_color = color
                    
                except:
                    if bg_text_input == "":
                        self.background_color = get_color_from_hex(get_color_from_text("Sienna"))

                    else:
                        try:
                            bg_color = get_color_from_text(bg_text_input)
                            self.background_color = get_color_from_hex(bg_color)

                        except:
                            pass
                        
            except:
                self.background_color = get_color_from_hex(get_color_from_text("Sienna"))
        

        elif type == "font_size":
            try:
                font_size = instance.text

                if font_size == "":
                    self.font_size = "24sp"

                else:
                    self.font_size = font_size

            except Exception as tb:
                self.font_size = "24sp"

        elif type == "text_color":
            try:
                color_text_input = instance.text
                if color_text_input == "":
                    self.text_color = get_color_from_hex(get_color_from_text("White"))
                
                else:
                    try:
                        color = get_color_from_text(color_text_input)
                        self.text_color = get_color_from_hex(color)

                    except:
                        pass
                    
            except:
                self.text_color = get_color_from_hex(get_color_from_text("White"))
        
        elif type == "pos_x":
            try:
                pos_x = instance.text

                if pos_x == "":
                    self.pos_x = 0
                
                else:
                    self.pos_x = float(pos_x)
            

            except Exception as tb:
                self.pos_x = 0
                self.center_x = 0.5

        elif type == "pos_y":
            try:
                pos_y = instance.text

                if pos_y == "":
                    self.pos_y = 0
                
                else:
                    self.pos_y = float(pos_y)
            

            except Exception as tb:
                self.pos_y = 0

        
Window.maximize()
KDEWidgetPlayGroundApp().run()