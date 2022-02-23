import os
from random import choice

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import sp, dp
from kivy.properties import ObjectProperty
from kivy.utils import get_color_from_hex
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

from plyer import filechooser
from base.scripts import *


class MDTab(MDFloatLayout, MDTabsBase):
    pass

class PlayGround(MDTab):
    pass 


class Output(MDTab):
    path = r"kv-files\btn.kv"
    Builder.load_file(path)

class MDTooltipContentClass(MDBoxLayout):
    pass



class KivyDevelopmentEnvironmentApp(MDApp):
    
    # Properties
    width_num = ObjectProperty(255)

    height_num = ObjectProperty(255)

    text = ObjectProperty("Change ME!")

    background_color = ObjectProperty(get_color_from_hex(get_color_from_text("Sienna")))

    pos_x = ObjectProperty(150)

    pos_y = ObjectProperty(150)

    disabled = ObjectProperty(False)

    font_size = ObjectProperty("12sp")

    font = ObjectProperty("Roboto")


    text_color = ObjectProperty(get_color_from_hex(get_color_from_text("White")))

    elevation = ObjectProperty(10)
    
    tooltip_dialog = None
    
    path_to_kv_file = r'kv-files\playground.kv'

    font_style = ObjectProperty('Button')

    # Tooltip related properties
    tooltip_text = ObjectProperty("output-btn")

    tooltip_bg_color = ObjectProperty(get_color_from_hex(get_color_from_text("White")))

    tooltip_font_style = ObjectProperty('Caption')

    tooltip_text_color = ObjectProperty(get_color_from_hex(get_color_from_text("Black")))

    tooltip_radius = ObjectProperty([dp(7)])



    def open_file_manager(self):
        filechooser.open_file(title="Choose Font", filters=['*.ttf', '*.otf', '*.ttc'], on_selection=self.return_path)



    def return_path(self, path):
        try:
            OK_BTN = MDFlatButton(
                text="OK",
                theme_text_color="Custom",
                text_color=self.theme_cls.primary_dark
            )
            
            back_slash = '\\'
            file_name = path[0].split(back_slash)

            
            file_name = file_name[-1]

            self.load_dialog = MDDialog(
                title="Font Loaded Successfully",
                text=f"The font file {file_name} loaded successfully.",
                buttons=[
                    OK_BTN
                ]
            )
            def switch_tab_and_dismiss():
                self.load_dialog.dismiss()
                MDApp.get_running_app().root.ids.tabs.carousel.load_next()

            OK_BTN.bind(on_press=lambda switch: switch_tab_and_dismiss())
            self.load_dialog.open()
            self.font = path[0]
        
        except:
            pass
    

    def change_palette(self):
        palettes = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        accent_palettes = palettes.copy()
        
        palette = choice(palettes)
        accent = choice(accent_palettes)

        self.theme_cls.primary_palette = f"{palette}"
        self.theme_cls.accent_palette = f"{accent}"

        self.dialog.title = f"Using theme: {palette}"
        self.dialog.text = f"The primary palette has been changed to {palette} & the accent palette has been changed to {accent}."
        self.CANCEL_BTN.text = "CANCEL"
        self.CANCEL_BTN.bind(on_press=lambda revert: self.revert())

        self.dialog.open()

    def revert(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.dialog.dismiss()

    def build(self):
        palettes = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        accents = palettes.copy()

        self.rand_palette = choice(palettes)
        self.rand_accent = choice(accents)

        os.environ["KIVY_PROFILE_LANG"] = "1"


        self.theme_cls.primary_palette = f"{self.rand_palette}"
        self.theme_cls.accent_palette = f"{self.rand_accent}"
        

        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = return_theme()
        self.title = "Kivy Development Environment"

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
            text=f"The primary pallette has been changed to {self.theme_cls.primary_palette} & the accent palette has been changed to {self.theme_cls.accent_palette}.",
            buttons=(self.OK_BTN, self.CANCEL_BTN)

        )
        self.OK_BTN.bind(on_press=self.dialog.dismiss)
        
        self.CANCEL_BTN.bind(on_press=lambda revert: self.revert())
    
        self.dialog.open()
        self.funcs = {
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
            "error_color": self.theme_cls.error_color
        }
    
    def launch_tooltip_dialog(self):

        OK_BTN = MDFlatButton(
            text="APPLY",
            theme_text_color="Custom",
            text_color=self.theme_cls.primary_color
        )
        CANCEL_BTN = MDFlatButton(
            text="CANCEL",
            theme_text_color="Custom",
            text_color=self.theme_cls.error_color
        )

        self.tooltip_dialog = MDDialog(
            title="Edit Tooltip Properties",
            content_cls=MDTooltipContentClass(),
            type="custom",
            buttons=[
                OK_BTN,
                CANCEL_BTN,
            ],
        )
        def apply_and_switch():
            self.tooltip_dialog.dismiss()
            MDApp.get_running_app().root.ids.tabs.carousel.load_next()
        
        def reset_and_dismiss():
            self.tooltip_text = "output-btn"

            if self.theme_cls.theme_style == "Dark":
                self.tooltip_bg_color = get_color_from_hex(get_color_from_text("White"))
                self.tooltip_text_color = get_color_from_hex(get_color_from_text("Black"))
            
            else:
                self.tooltip_bg_color = get_color_from_hex(get_color_from_text("Black"))
                self.tooltip_text_color = get_color_from_hex(get_color_from_text("White"))
            

            self.tooltip_font_style = "Caption"
            self.tooltip_radius = [dp(7)]

            self.tooltip_dialog.dismiss()
        
            

            self.tooltip_font_style = "Caption"
            self.tooltip_radius = [dp(7)]



    
        CANCEL_BTN.bind(on_press=lambda reset_and_dismiss_: reset_and_dismiss())

        OK_BTN.bind(on_press=lambda switch_tab: apply_and_switch())


        self.tooltip_dialog.open()

    
    # TOOLTIP TEXTFIELD EVENTS



    def set_tooltip_property(self, instance, type):

        if type == "tooltip_text":
            try:
                text = instance.text
                if text == "":
                    self.tooltip_text = f"output-btn"
                else:
                    self.tooltip_text = f"{text}"
            except Exception as tb:
                self.tooltip_text = f"output-btn"
        
        elif type == "tooltip_bg":
            try:
                bg_text_input = instance.text

                try:
                    color = self.funcs[bg_text_input.lower()]
                    self.tooltip_bg_color = color
                    
                except:
                    if bg_text_input == "":
                        self.tooltip_bg_color = get_color_from_hex(get_color_from_text("White"))
                    else:
                        try:
                            bg_color = get_color_from_text(bg_text_input)
                            self.tooltip_bg_color = get_color_from_hex(bg_color)

                        except:
                            pass
                        
            except:
                self.tooltip_bg_color = get_color_from_hex(get_color_from_text("White"))
                        

        elif type == "tooltip_style":
            try:
                font_style = instance.text

                if font_style == "":
                    self.tooltip_font_style = "Caption"
                
                else:
                    self.tooltip_font_style = f"{font_style}"
            except:
                self.tooltip_font_style = "Caption"
        
        elif type == "tooltip_txt_clr":
            try:
                color_text_input = instance.text
                try:
                    color = self.funcs[color_text_input.lower()]
                    self.tooltip_text_color = color

                except:
                    if color_text_input == "":
                        self.tooltip_text_color = get_color_from_hex(get_color_from_text("Black"))
                    
                    else:
                        try:
                            color = get_color_from_text(color_text_input)
                            self.tooltip_text_color = get_color_from_hex(color)

                        except:
                            pass
                    
            except:
                self.tooltip_text_color = get_color_from_hex(get_color_from_text("Black"))

        elif type == "radius":
            try:
                radius = instance.text
                if radius == "":
                    self.tooltip_radius = [dp(7)]
                
                else:
                    try:
                        
                        self.tooltip_radius = [dp(eval(radius))]
                     
                    except Exception as tb:
                        self.tooltip_radius = [dp(7)]


            except Exception as tb:
                print(tb)
                self.width_num = sp(200)





    # TEXTFIELD  EVENTS
    def set_property(self, instance, type):

        # Set the width of the button.
        if type == "width":
            try:
                width = instance.text
                if width == "":
                    self.width_num = sp(200)
                
                else:
                    try:
                        
                        self.width_num = sp(eval(width))
                     
                    except Exception as tb:
                        self.width_num = sp(200)


            except Exception as tb:
                print(tb)
                self.width_num = sp(200)
        
        # Set the height of the button.
        elif type == "height":
            try:
                height = instance.text
                
                if height == "":
                    self.height_num = sp(200)

                
                else:
                    try:
                        self.height_num = sp(eval(height))
                    except:
                        self.height_num = sp(200)
            except Exception as tb:
                self.height_num = sp(200)



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
        


        # Set the bg_color of the button
        elif type == "bg_color":
            try:
                bg_text_input = instance.text

                try:
                    color = self.funcs[bg_text_input.lower()]
                    self.background_color = color
                    
                except:
                    if bg_text_input == "":
                        self.background_color = self.funcs["primary_color"]
                    else:
                        try:
                            bg_color = get_color_from_text(bg_text_input)
                            self.background_color = get_color_from_hex(bg_color)

                        except:
                            pass
                        
            except:
                self.background_color = self.funcs["primary_color"]        

        # Set the font_size of the button
        elif type == "font_size":
            try:
                font_size = instance.text

                if font_size == "":
                    self.font_size = "24sp"

                else:
                    self.font_size = font_size

            except Exception as tb:
                self.font_size = "24sp"


        # Set the text color of the button
        elif type == "text_color":
            try:
                color_text_input = instance.text
                try:
                    color = self.funcs[color_text_input.lower()]
                    self.text_color = color
                except:
                    if color_text_input == "":
                        self.text_color = get_color_from_hex(get_color_from_text("White"))
                    
                    else:
                        try:
                            color = get_color_from_text(color_text_input)
                            self.text_color = get_color_from_hex(color)

                        except:
                            self.text_color = get_color_from_hex(get_color_from_text("White"))
                    
            except:
                self.text_color = get_color_from_hex(get_color_from_text("White"))
        

        # Set the pos_x of the button
        elif type == "pos_x":
            try:
                pos_x = instance.text

                if pos_x == "":
                    self.pos_x = 0
                
                else:
                    self.pos_x = eval(pos_x)
            

            except Exception as tb:
                self.pos_x = 0


        # Set the pos_y of the button
        elif type == "pos_y":
            try:
                pos_y = instance.text

                if pos_y == "":
                    self.pos_y = 0
                
                else:
                    self.pos_y = eval(pos_y)
            

            except Exception as tb:
                self.pos_y = 0
        
        elif type == "elevation":
            try:
                elevation = instance.text

                if elevation == "":
                    self.elevation = 10
                
                else:
                    self.elevation = eval(elevation)
            
            except:
                self.elevation = 10
        
        elif type == "font_style":
            try:
                font_style = instance.text

                if font_style == "":
                    self.font_style = "Button"
                
                else:
                    self.font_style = font_style
            except:
                self.font_style = "Button"


        
Window.maximize()
KivyDevelopmentEnvironmentApp().run()
