#  William Dos Santos Junqueira
#  Youtube video download using KivyMd and Pytube
'''
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', False)'''

import os
from kivymd.app import MDApp
from pytube import YouTube
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivy.config import Config


# Main app class  
class MainApp(MDApp):
    def build(self):
        self.title = 'Download Youtube Video'
        self.icon = 'icon.png'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.material_style = 'M3'
       
        self.yd = YotubeDownload()
        self.valid = False  #  is the input valid?
         
    #  show a dialog box
    def show_dialog(self, tp=''):
        if tp == 'invalid text':
            self.msg = 'Please insert a valid youtube link.'
            self.title = 'Error invalid url!'

        elif tp == 'downloaded':
            self.title = ''
            print(self.valid)
            if self.valid == False:
                return

            elif self.valid == True:
                self.msg = f'{self.yd.title} video was successfully downloaded'

        md = MDDialog(text=self.msg, title=self.title, radius=[20, 7, 20, 7])
        md.open()
  
    #  show video thumbnail and title on screen
    def show_assents(self):   
        Clock.schedule_once(lambda x: self.yd.get_assents(self.yt)) # sending the youtube object to the get_assents method
        self.root.ids.thumbnail.source = self.yd.thumbnail  
        self.root.ids.title.text = self.yd.title 
        
    #  check if the text input really are a valid youtube link
    def verify(self):
        self.link = self.root.ids.txt_input.text  # get input information   
        try:
            self.yt = YouTube(self.link)  #  youtube obj
            self.show_assents()     
            self.valid = True
                 
        except: self.valid = False
             

#  Youtuve Download Class
class YotubeDownload:
    def __init__(self):
        self.download_complete = False
        self.thumbnail = ''
        self.title = ''
      
    # get the video information (title and thumbnail image)
    def get_assents(self, yt):
        self.yt = yt 
        self.thumbnail = self.yt.thumbnail_url
        self.title = self.yt.title
      
    # download the video 
    def download(self, ):
        self.streams = self.yt.streams.get_highest_resolution()
        self.streams.download('~Downloads/videos')
        self.download_complete = True
        print(f'Successfull! {self.title}')
       
#  Run App
if __name__ == '__main__':
    MainApp().run()
