# Copyright 2020 Lukas Lösche <lloesche@fedoraproject.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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


def getshift(week_offset=0):
    _, week, _ = datetime.date.today().isocalendar()
    week += week_offset
    week_index = week % len(shift)
    next_week_index = (week + 1) % len(shift)
    current_shift = shift[week_index]
    next_shift = shift[next_week_index]
    current_time = datetime.datetime.now().time()
    work_info = "er arbeitet momentan"
    if current_shift["stop"] < current_shift["start"]:
        # night shift that crosses midnight
        if (
            current_shift["start"] <= current_time
            or current_time < current_shift["stop"]
        ):
            pass
        else:
            work_info += " nicht"
    else:
        # normal shift
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
