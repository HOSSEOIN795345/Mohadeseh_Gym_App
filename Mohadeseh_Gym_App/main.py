from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.core.text import LabelBase

from app_pages import HomePage, WorkoutMenu, DayPage
from workout_page import ExercisePage
from records_page import RecordsPage
from preparation_page import PreparationPage


LabelBase.register(
    name="Persian",
    fn_regular="assets/fonts/Vazirmatn-Bold.ttf"
)


class MohadesehGym(App):

    def build(self):

        sm = ScreenManager(
            transition=SlideTransition(duration=0.4)
        )


        sm.add_widget(
            HomePage(name="home")
        )

        sm.add_widget(
            WorkoutMenu(name="workout")
        )

        sm.add_widget(
            DayPage(name="day")
        )

        sm.add_widget(
            ExercisePage(name="exercise")
        )

        sm.add_widget(
            RecordsPage(name="records")
        )

        sm.add_widget(
            PreparationPage(name="preparation")
        )


        return sm



if __name__ == "__main__":
    MohadesehGym().run()