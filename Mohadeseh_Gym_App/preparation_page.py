from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import LabelBase

import arabic_reshaper
from bidi.algorithm import get_display


LabelBase.register(
    name="Persian",
    fn_regular="assets/fonts/Vazirmatn-Bold.ttf"
)



def persian(text):
    return get_display(
        arabic_reshaper.reshape(str(text))
    )





class PreparationPage(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


        self.tasks = [
            "آب کافی همراه داشتن 💧",
            "۵ دقیقه گرم کردن بدن 🔥",
            "آماده کردن وسایل تمرین 🎒",
            "تنظیم موزیک تمرین 🎧",
            "تمرکز کامل روی تمرین امروز 💪"
        ]


        self.checked = []


        self.layout = FloatLayout()


        self.add_widget(
            self.layout
        )



    def on_enter(self):

        self.build_page()



    def build_page(self):

        self.layout.clear_widgets()


        title = Label(

            text=persian(
                "آماده‌ای محدثه؟ 💜"
            ),

            font_name="Persian",

            font_size=32,

            size_hint=(1,0.15),

            pos_hint={"top":1}

        )


        self.layout.add_widget(title)




        box = BoxLayout(

            orientation="vertical",

            spacing=10,

            size_hint=(0.8,0.5),

            pos_hint={
                "center_x":0.5,
                "center_y":0.55
            }

        )




        for task in self.tasks:


            btn = Button(

                text=persian(
                    "☐ " + task
                ),

                font_name="Persian",

                font_size=18

            )


            btn.bind(
                on_press=lambda x,t=task,b=btn:
                self.check_task(t,b)
            )


            box.add_widget(btn)




        self.layout.add_widget(box)




        self.message = Label(

            text="",

            font_name="Persian",

            font_size=22,

            size_hint=(1,0.1),

            pos_hint={
                "center_y":0.25
            }

        )


        self.layout.add_widget(
            self.message
        )




        back = Button(

            text=persian(
                "بازگشت"
            ),

            font_name="Persian",

            size_hint=(0.3,0.08),

            pos_hint={
                "center_x":0.5,
                "y":0.03
            }

        )


        back.bind(

            on_press=lambda x:
            setattr(
                self.manager,
                "current",
                "home"
            )

        )


        self.layout.add_widget(back)





    def check_task(self,task,button):


        if task not in self.checked:

            self.checked.append(task)


            button.text = persian(
                "☑ " + task
            )



        if len(self.checked)==len(self.tasks):


            self.message.text = persian(

                "آفرین محدثه 💜\n"
                "آماده یک تمرین فوق‌العاده‌ای 💪"

            )