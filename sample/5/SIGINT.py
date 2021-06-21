import signal
import time


def handler(signum, time):
    print("\nI got SIGINT, but I'm not gonna stop")


signal.signal(signal.SIGINT, handler)
i = 0
while True:
    time.sleep(.1)
    print("\r{}".format(i), end="")
    i += 1
