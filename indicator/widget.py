import os
import json
import random

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify

from fetch import fetch_utilization, fetch_temperature
import checks
import notification

def widget(APPINDICATOR_ID):
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('images/logo.jpeg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())

    notify.init(APPINDICATOR_ID)

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

def quit(_):
    notify.uninit()
    gtk.main_quit()
