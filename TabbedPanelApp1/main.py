from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
 
class TabbedPanelApp(App):
      def build(self):
          tb_panel= TabbedPanel()
 
          #Create text tab          
          th_text_head = TabbedPanelHeader(text='Text tab')
          th_text_head.content= Label(text='Ainene')
 
          #Create image tab
          th_img_head= TabbedPanelHeader(text='Image tab')
          th_img_head.content= Image(source='sample.jpg',pos=(400, 100), size=(400, 400))
 
          #Create button tab
          th_btn_head = TabbedPanelHeader(text='Button tab')
          th_btn_head.content= Button(text='Click me',font_size=20)
 
          tb_panel.add_widget(th_text_head)
          tb_panel.add_widget(th_img_head)
          tb_panel.add_widget(th_btn_head)     

 
          return tb_panel

 
if __name__ == '__main__':
    TabbedPanelApp().run()