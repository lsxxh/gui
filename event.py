from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

Builder.load_string('''
<CustomLayout>
    canvas.before:
        Color:
            rgba:0,1,0,1
        Rectangle:
            pos:self.pos
            size:self.size

<RootWidget>
    CustomLayout:
        AsyncImage:
            source:'http://www.rolls-roycemotorcars.com.cn/content/dam/rollsroyce-website/Ghost/ghost-ewb.png'
            size_hint:1,.5
            pos_hint:{'center_x':.5,'center_y':.5}
    AsyncImage:
        source:"https://f1.media.brightcove.com/8/1634657725001/1634657725001_6073558126001_6056449777001-vs.jpg"
        size_hint:1,.5
        pos_hint:{'center_x':.5,'center_y':.5}
    CustomLayout:
        AsyncImage:
            source:'http://www.rolls-roycemotorcars.com.cn/content/dam/rollsroyce-website/Ghost/ghost-ewb.png'           
            size_hint:1,.5
            pos_hint:{'center_x':.5,'center_y':.5}
    Button:
        text:"search1"
        text_size:self.width-20,self.height-20
        size_hint:.2,.2
        on_press:root.search()
            ''')

class RootWidget(BoxLayout):
    def search(self):
        print('smile')
class CustomLayout(FloatLayout):
    pass
class MainApp(App):
    def build(self):
        return RootWidget()

if __name__=='__main__':
    MainApp().run()
