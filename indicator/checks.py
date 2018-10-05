<<<<<<< HEAD
import threading
import time
import datetime

from gi.repository import Notify as notify

from fetch import fetch_utilization, fetch_temperature

def launch_temp_check(WARNING_REFRESH_TIME, WARNING_TEMPERATURE):
    flag = 0
    time_over_temp = datetime.datetime.now()
    i = 0
    while i < 100:
        time.sleep(WARNING_REFRESH_TIME)
        current_temperature = fetch_temperature()

        if int(current_temperature) > WARNING_TEMPERATURE and flag == 1:
            if datetime.datetime.now() - time_over_temp >= datetime.timedelta(5, 0, 0):
                notify.Notification.new("<b>Temperature Warning </b>", "Temperature reached above "+str(WARNING_TEMPERATURE)+"*C", None).show()

        elif int(current_temperature) > WARNING_TEMPERATURE and flag == 0:
            flag = 1
            time_over_temp = datetime.datetime.now()
            notify.Notification.new("<b>Temperature Warning </b>", "Temperature reached above "+str(WARNING_TEMPERATURE)+"*C", None).show()

        elif int(current_temperature) < WARNING_TEMPERATURE:
            flag = 0
        i = i + 1

def launch_util_check(WARNING_REFRESH_TIME, WARNING_UTILIZATION):
    flag = 0
    time_over_util = datetime.datetime.now()
    i = 0
    while i < 100:
        time.sleep(WARNING_REFRESH_TIME)
        current_utilization = fetch_utilization()

        if int(current_utilization) > WARNING_UTILIZATION and flag == 1:
            if datetime.datetime.now() - time_over_util >= datetime.timedelta(5, 0, 0):
                notify.Notification.new("<b>Utilization Warning </b>", "Utilization reached above "+str(WARNING_UTILIZATION)+"%", None).show()

        elif int(current_utilization) > WARNING_UTILIZATION and flag == 0:
            flag = 1
            time_over_util = datetime.datetime.now()
            notify.Notification.new("<b>Utilization Warning </b>", "Utilization reached above "+str(WARNING_UTILIZATION)+"%", None).show()

        elif int(current_utilization) < WARNING_UTILIZATION:
            flag = 0
        i = i + 1

def all_checks(APPINDICATOR_ID, WARNING_CHECK_FLAG, WARNING_REFRESH_TIME, WARNING_TEMPERATURE, WARNING_UTILIZATION):
    notify.init(APPINDICATOR_ID)
    if WARNING_CHECK_FLAG == 1:
        temp_check = threading.Thread(target=launch_temp_check, args=(WARNING_REFRESH_TIME, WARNING_TEMPERATURE))
        util_check = threading.Thread(target=launch_util_check, args=(WARNING_REFRESH_TIME, WARNING_UTILIZATION))
        temp_check.start()
        util_check.start()

    if WARNING_CHECK_FLAG == 2:
        temp_check = threading.Thread(target=launch_temp_check, args=(WARNING_REFRESH_TIME, WARNING_TEMPERATURE))
        temp_check.start()

    if WARNING_CHECK_FLAG == 3:
        util_check = threading.Thread(target=launch_util_check, args=(WARNING_REFRESH_TIME, WARNING_UTILIZATION))
        util_check.start()
=======
from gi.repository import Notify as notify
import threading

def launch_temp_check():
    pass
>>>>>>> ae0a17dc2f93504475d7a4c24a40c32e342b7943
