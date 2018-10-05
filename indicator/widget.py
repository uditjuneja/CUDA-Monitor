import os
import json
import random
<<<<<<< HEAD
import time
=======
>>>>>>> ae0a17dc2f93504475d7a4c24a40c32e342b7943

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify
<<<<<<< HEAD
from gi.repository import GObject
=======
>>>>>>> ae0a17dc2f93504475d7a4c24a40c32e342b7943

from fetch import fetch_utilization, fetch_temperature
import checks
import notification

<<<<<<< HEAD
import threading

def widget(APPINDICATOR_ID, REFRESH_TIME):
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('images/logo.jpeg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    indicator.set_label("nvidia-smi", APPINDICATOR_ID)
    notify.init(APPINDICATOR_ID)

    update = threading.Thread(target=show_seconds, args=(indicator, APPINDICATOR_ID, REFRESH_TIME))
    update.setDaemon(True)
    update.start()

    GObject.threads_init()
=======
def widget(APPINDICATOR_ID):
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('images/logo.jpeg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())

    notify.init(APPINDICATOR_ID)

>>>>>>> ae0a17dc2f93504475d7a4c24a40c32e342b7943
    gtk.main()

def build_menu():
    menu = gtk.Menu()

    item_random = gtk.MenuItem("Update - Utilization")
    item_random.connect('activate', notification.utilization_notification)
    menu.append(item_random)

    item_random = gtk.MenuItem("Update - Temperature")
    item_random.connect('activate', notification.temperature_notification)
    menu.append(item_random)

    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)

    menu.show_all()
    return menu

<<<<<<< HEAD
def show_seconds(indicator, APPINDICATOR_ID, REFRESH_TIME):
    while True:
        time.sleep(REFRESH_TIME)
        mention = str(fetch_utilization()) +"% " + str(fetch_temperature())+"*C"
        # apply the interface update using  GObject.idle_add()
        GObject.idle_add(indicator.set_label, mention, APPINDICATOR_ID, priority=GObject.PRIORITY_DEFAULT)


=======
>>>>>>> ae0a17dc2f93504475d7a4c24a40c32e342b7943
def quit(_):
    notify.uninit()
    gtk.main_quit()
