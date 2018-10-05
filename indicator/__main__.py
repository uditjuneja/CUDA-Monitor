import signal
<<<<<<< HEAD
import threading
=======
>>>>>>> ae0a17dc2f93504475d7a4c24a40c32e342b7943

APPINDICATOR_ID = 'CUDA-Indicator'

from widget import widget
<<<<<<< HEAD
import checks

REFRESH_TIME = 1

WARNING_CHECK_FLAG = 1

WARNING_REFRESH_TIME = 5
WARNING_TEMPERATURE = 65
WARNING_UTILIZATION = 90

if __name__ == "__main__":
    if WARNING_CHECK_FLAG == 1:
        checks.all_checks(APPINDICATOR_ID, WARNING_CHECK_FLAG, WARNING_REFRESH_TIME, WARNING_TEMPERATURE, WARNING_UTILIZATION)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    widget(APPINDICATOR_ID, REFRESH_TIME)
=======

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    widget(APPINDICATOR_ID)
>>>>>>> ae0a17dc2f93504475d7a4c24a40c32e342b7943
