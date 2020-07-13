import os
import datetime
import time


os.environ["TZ"] = "Europe/Berlin"
time.tzset()

shift = [
    {"name": "Spät", "start": datetime.time(14, 0, 0), "stop": datetime.time(22, 0, 0)},
    {"name": "Früh", "start": datetime.time(6, 0, 0), "stop": datetime.time(14, 0, 0)},
    {"name": "Nacht", "start": datetime.time(22, 0, 0), "stop": datetime.time(6, 0, 0)},
]


def getshift():
    _, week, _ = datetime.date.today().isocalendar()
    week_index = week % len(shift)
    next_week_index = (week + 1) % len(shift)
    current_shift = shift[week_index]
    next_shift = shift[next_week_index]
    current_time = datetime.datetime.now().time()
    work_info = "er arbeitet momentan"
    if current_shift["start"] <= current_time < current_shift["stop"]:
        pass
    else:
        work_info += " nicht"
    msg = (
        f"Benni hat diese Woche {current_shift['name']}- und nächste Woche {next_shift['name']}schicht. "
        f"Es ist gerade {datetime.datetime.now().strftime('%H:%M')} Uhr und {work_info}. "
        f"Die {current_shift['name']}schicht geht von {current_shift['start']} bis {current_shift['stop']} Uhr. "
        f"Die {next_shift['name']}schicht geht von {next_shift['start']} bis {next_shift['stop']} Uhr."
    )
    return msg
