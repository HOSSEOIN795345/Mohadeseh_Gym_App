from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
from kivy.core.text import LabelBase
from kivy.animation import Animation

import json
import os

import arabic_reshaper
from bidi.algorithm import get_display


LabelBase.register(
    name="Persian",
    fn_regular="assets/fonts/Vazirmatn-Bold.ttf"
)


def persian(text):
    return get_display(arabic_reshaper.reshape(str(text)))


with open("data/workouts.json", "r", encoding="utf-8") as f:
    workouts = json.load(f)


PROGRESS_FILE = "data/progress.json"


def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return {}
    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_progress(data):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)



# 🎨 بک‌گراند با قابلیت انیمیشن
class PurpleBackground(FloatLayout):

    def __init__(self, color=(0.35,0.1,0.6,1), **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            self.color_instruction = Color(*color)
            self.bg = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_bg, pos=self.update_bg)


    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos


    def animate_to(self, new_color):
        Animation(
            r=new_color[0],
            g=new_color[1],
            b=new_color[2],
            duration=0.6
        ).start(self.color_instruction)



# 🏠 صفحه اصلی
class HomePage(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = PurpleBackground(color=(0.5,0.2,0.7,1))

        title = Label(
            text=persian("باشگاه محدثه من 💜"),
            font_name="Persian",
            font_size=35,
            size_hint=(1,0.2),
            pos_hint={"top":1}
        )

        layout.add_widget(title)

        buttons = [
            ("برنامه تمرینی","workout"),
            ("رکوردهای من","records"),
            ("قبل از باشگاه","preparation")
        ]

        y = 0.6

        for text,page in buttons:

            btn = Button(
                text=persian(text),
                font_name="Persian",
                size_hint=(0.6,0.1),
                pos_hint={"center_x":0.5,"center_y":y}
            )

            btn.bind(
                on_press=lambda x,p=page:
                setattr(self.manager,"current",p)
            )

            layout.add_widget(btn)

            y -= 0.15

        self.add_widget(layout)



# 📅 منوی روزها
class WorkoutMenu(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = PurpleBackground(color=(0.6,0.1,0.8,1))
        self.add_widget(self.layout)

    def on_enter(self):

        self.layout.clear_widgets()

        y = 0.7

        for day in workouts:

            btn = Button(
                text=persian(day),
                font_name="Persian",
                size_hint=(0.6,0.1),
                pos_hint={"center_x":0.5,"center_y":y}
            )

            btn.bind(
                on_press=lambda x,d=day:
                self.open_day(d)
            )

            self.layout.add_widget(btn)

            y -= 0.15


    def open_day(self, day):
        self.manager.get_screen("day").show_workout(day)
        self.manager.current = "day"



# 🏋️ لیست حرکات هر روز
class DayPage(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = PurpleBackground(color=(0.4,0.1,0.7,1))
        self.add_widget(self.layout)

        self.current_day = None


    def show_workout(self, day):

        self.current_day = day

        self.layout.clear_widgets()

        progress = load_progress()

        if day not in progress:
            progress[day] = 0
            save_progress(progress)

        done_index = progress[day]


        box = BoxLayout(
            orientation="vertical",
            size_hint_y=None
        )

        box.bind(minimum_height=box.setter("height"))


        for i, exercise in enumerate(workouts[day]):

            text = exercise

            if i < done_index:
                text = "✔ " + text

            btn = Button(
                text=persian(text),
                font_name="Persian",
                size_hint_y=None,
                height=60
            )

            if i > done_index:
                btn.disabled = True

            btn.bind(
                on_press=lambda x,e=exercise,i=i:
                self.open_exercise(e, i)
            )

            box.add_widget(btn)


        scroll = ScrollView()
        scroll.add_widget(box)

        self.layout.add_widget(scroll)


    def open_exercise(self, exercise, index):

        ex = self.manager.get_screen("exercise")

        ex.start_exercise(exercise)
        ex.exercise_index = index
        ex.day_name = self.current_day

        self.manager.current = "exercise"