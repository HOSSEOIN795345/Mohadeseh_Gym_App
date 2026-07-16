import json
import os
from datetime import date, timedelta


STREAK_FILE = "data/streak.json"


def load_streak():

    if not os.path.exists(STREAK_FILE):
        return {
            "count": 0,
            "last_day": ""
        }

    with open(
        STREAK_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def save_streak(data):

    with open(
        STREAK_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def update_streak():

    data = load_streak()

    today = str(date.today())


    # اگر امروز قبلا ثبت شده
    if data["last_day"] == today:
        return data["count"]


    if data["last_day"] == "":

        data["count"] = 1


    else:

        last = date.fromisoformat(
            data["last_day"]
        )

        yesterday = date.today() - timedelta(days=1)


        if last == yesterday:

            data["count"] += 1

        else:

            data["count"] = 1



    data["last_day"] = today


    save_streak(data)


    return data["count"]



def get_streak():

    data = load_streak()

    return data["count"]