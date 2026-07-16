from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.text import LabelBase

import json
import os

import arabic_reshaper
from bidi.algorithm import get_display


LabelBase.register(
    name="Persian",
    fn_regular="assets/fonts/Vazirmatn-Bold.ttf"
)


RECORD_FILE = "data/records.json"


def persian(text):
    return get_display(
        arabic_reshaper.reshape(str(text))
    )


def load_records():

    if not os.path.exists(RECORD_FILE):
        return {}

    try:
        with open(
            RECORD_FILE,
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    except:
        return {}



def save_records(data):

    with open(
        RECORD_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )



class RecordsPage(Screen):


    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.layout = FloatLayout()

        self.add_widget(self.layout)



    def on_enter(self):

        self.build_page()



    def build_page(self):

        self.layout.clear_widgets()



        title = Label(
            text=persian("رکوردهای من 💪"),
            font_name="Persian",
            font_size=32,
            size_hint=(1,0.15),
            pos_hint={"top":1}
        )

        self.layout.add_widget(title)



        scroll = ScrollView(
            size_hint=(1,0.62),
            pos_hint={"y":0.22}
        )



        box = BoxLayout(
            orientation="vertical",
            spacing=15,
            size_hint_y=None
        )


        box.bind(
            minimum_height=box.setter("height")
        )



        records = load_records()



        if not records:


            empty = Label(
                text=persian(
                    "هنوز رکوردی ثبت نشده 💙"
                ),
                font_name="Persian",
                font_size=22,
                size_hint_y=None,
                height=80
            )

            box.add_widget(empty)



        else:


            for exercise, data in records.items():


                card = BoxLayout(
                    orientation="vertical",
                    size_hint_y=None,
                    height=150,
                    spacing=5
                )


                last = data.get(
                    "آخرین رکورد",
                    "-"
                )


                text = f"""
{exercise}

آخرین رکورد: {last}
"""


                for i in range(1,4):

                    key = f"ست {i}"

                    if key in data:
                        text += f"\n{key}: {data[key]}"



                label = Label(
                    text=persian(text),
                    font_name="Persian",
                    font_size=18
                )



                delete = Button(
                    text=persian("حذف"),
                    font_name="Persian",
                    size_hint_y=None,
                    height=40
                )


                delete.bind(
                    on_press=lambda x,e=exercise:
                    self.delete_record(e)
                )


                card.add_widget(label)
                card.add_widget(delete)


                box.add_widget(card)



        scroll.add_widget(box)

        self.layout.add_widget(scroll)



        clear = Button(
            text=persian("پاک کردن همه رکوردها"),
            font_name="Persian",
            size_hint=(0.5,0.08),
            pos_hint={
                "center_x":0.5,
                "y":0.12
            }
        )


        clear.bind(
            on_press=self.delete_all
        )


        self.layout.add_widget(clear)




        back = Button(
            text=persian("بازگشت"),
            font_name="Persian",
            size_hint=(0.3,0.08),
            pos_hint={
                "center_x":0.5,
                "y":0.02
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



    def delete_record(self, exercise):

        data = load_records()


        if exercise in data:

            del data[exercise]

            save_records(data)


        self.build_page()



    def delete_all(self, instance):

        save_records({})

        self.build_page()