import signal

APPINDICATOR_ID = 'CUDA-Indicator'

from widget import widget

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    widget(APPINDICATOR_ID)
