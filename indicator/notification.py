from gi.repository import Notify as notify
import fetch

def utilization_notification(_):
    notify.Notification.new("<b>Utilization</b>", "Current GPU Utilization - "+fetch.fetch_utilization()+"%", None).show()

def temperature_notification(_):
    notify.Notification.new("<b>Temperature</b>", "Current GPU Temperature - "+fetch.fetch_temperature()+" *C", None).show()
