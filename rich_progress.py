import time
from rich.progress import track

sleep_time = 0.1
for i in track(range(100), description="Testing..."):
    time.sleep(sleep_time)
    sleep_time /= 0.9

