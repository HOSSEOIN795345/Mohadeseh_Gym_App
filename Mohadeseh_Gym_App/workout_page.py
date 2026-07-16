from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.text import LabelBase

import json
import os

import arabic_reshaper
from bidi.algorithm import get_display

from love_messages import get_message
from streak import update_streak

LabelBase.register(name="Persian", fn_regular="assets/fonts/Vazirmatn-Bold.ttf")


RECORD_FILE = "data/records.json"
PROGRESS_FILE = "data/progress.json"


def persian(text):
    return get_display(arabic_reshaper.reshape(str(text)))


def load(path):

    if not os.path.exists(path):
        return {}

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save(path, data):

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


class ExercisePage(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.exercise_name = ""
        self.day_name = ""
        self.exercise_index = 0

        self.current_set = 1

        self.time = 0
        self.timer_event = None

        self.layout = FloatLayout()

        self.title = Label(
            font_name="Persian", font_size=32, size_hint=(1, 0.15), pos_hint={"top": 1}
        )

        self.info = Label(
            font_name="Persian",
            font_size=22,
            size_hint=(1, 0.2),
            pos_hint={"center_y": 0.65},
        )

        self.record = TextInput(
            font_name="Persian",
            multiline=False,
            size_hint=(0.5, 0.08),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        self.button = Button(
            text=persian("ثبت ست ✓"),
            font_name="Persian",
            size_hint=(0.5, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.35},
        )

        self.button.bind(on_press=self.action)

        self.message = Label(
            font_name="Persian",
            font_size=24,
            opacity=0,
            size_hint=(1, 0.2),
            pos_hint={"center_y": 0.2},
        )

        for w in [self.title, self.info, self.record, self.button, self.message]:
            self.layout.add_widget(w)

        self.add_widget(self.layout)

    def start_exercise(self, name):

        self.exercise_name = name
        self.current_set = 1

        self.title.text = persian(name)

        if "دوچرخه" in name:

            self.record.opacity = 0

            self.button.text = persian("شروع ۵ دقیقه 🚴")

            self.info.text = persian("۵ دقیقه رکاب بزن")

        else:

            self.record.opacity = 1
            self.record.text = ""

            self.button.text = persian("ثبت ست ✓")

            self.update()

    def update(self):

        self.info.text = persian(f"ست {self.current_set} از 3\nتکرار: 10 تا 12")

    def action(self, btn):

        if "دوچرخه" in self.exercise_name:

            self.start_timer()

        else:

            self.complete()

    def start_timer(self):

        self.button.disabled = True

        self.time = 300

        self.timer_event = Clock.schedule_interval(self.timer, 1)

    def timer(self, dt):

        self.time -= 1

        m = self.time // 60
        s = self.time % 60

        self.info.text = persian(f"{m}:{s:02d}")

        if self.time <= 0:

            self.timer_event.cancel()

            self.finish(False)

    def is_record(self, value):

        data = load(RECORD_FILE)

        old = data.get(self.exercise_name, {}).get("record", 0)

        try:
            return float(value) > float(old)
        except:
            return False

    def complete(self):

        value = self.record.text.strip()

        if value == "":
            return

        data = load(RECORD_FILE)

        data.setdefault(self.exercise_name, {})

        new = self.is_record(value)

        data[self.exercise_name][f"set{self.current_set}"] = value

        data[self.exercise_name]["record"] = value

        save(RECORD_FILE, data)

        if self.current_set < 3:

            self.current_set += 1

            self.record.text = ""

            self.update()

        else:

            self.finish(new)

    def finish(self, new=False):

        progress = load(PROGRESS_FILE)

        progress.setdefault(self.day_name, 0)

        if self.exercise_index == progress[self.day_name]:

            progress[self.day_name] += 1

        save(PROGRESS_FILE, progress)

        if new:

            text = "🔥 رکورد جدید زدی!\nعالی بود 💜"

        else:

            text = get_message()

        if progress[self.day_name] >= 3:

            text += f"\n🔥 استریک {update_streak()} روز"

        self.message.text = persian(text)

        Animation(opacity=1, duration=0.3).start(self.message)

        Clock.schedule_once(self.back, 4)

    def back(self, dt):

        self.manager.current = "day"
