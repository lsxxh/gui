from kivy.app import App
from kivy.graphics import Color,Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage

class RootWidget(BoxLayout):
    pass 
class CustomLayout(FloatLayout):
    def __init__(self,**kwargs):
        super(CustomLayout,self).__init__(**kwargs)
        with self.canvas.before:
            Color(0,1,0,1)
            self.rect=Rectangle(size=self.size,pos=self.pos)

        self.bind(size=self._update_rect,pos=self._update_rect)

    def _update_rect(self,instance,value):
        self.rect.pos=instance.pos
        self.rect.size=instance.size

class MainApp(App):
    def build(self):
        root=RootWidget()
        c=CustomLayout()
        root.add_widget(c)
        c.add_widget(
                AsyncImage(
                    source='http://www.rolls-roycemotorcars.com.cn/content/dam/rollsroyce-website/Ghost/ghost-ewb.png',
                    size_hint=(1,.5),
                    pos_hint={'center_x':.5,'center_y':.5}))
        root.add_widget(AsyncImage(source='https://f1.media.brightcove.com/8/1634657725001/1634657725001_6073558126001_6056449777001-vs.jpg',
                size_hint=(1,.5),
                pos_hint={'center_x':.5,'center_y':.5}))
        c=CustomLayout()
        root.add_widget(c)
        return root
if __name__=='__main__':
    MainApp().run()


