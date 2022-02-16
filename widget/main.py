from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.metrics import sp
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
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
    pos_x = ObjectProperty(0)
    pos_y = ObjectProperty(0)
    disabled = ObjectProperty(False)
    font_size = ObjectProperty("12sp")
    font = ObjectProperty("Roboto")
    path = ObjectProperty("")
    text_color = ObjectProperty(get_color_from_hex(get_color_from_text("White")))
    
    
    path_to_kv_file = r'kv-files\playground.kv'


    def open_file_manager(self):
        filechooser.open_file(title="Choose Font", filters=['*.ttf', '*.otf', '*.ttc'], on_selection=self.return_path)

    def return_path(self, path):
        self.path = path[0]

        self.font = self.path


    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        self.title = "Widget Playground"

        return Builder.load_file(self.path_to_kv_file)
    

    def on_start(self):
        self.root.ids.tabs.add_widget(PlayGround(title="Playground"))
        self.root.ids.tabs.add_widget(Output(title="Output"))


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