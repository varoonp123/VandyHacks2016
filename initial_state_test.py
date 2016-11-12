import time
from ISStreamer.Streamer import Streamer

streamer = Streamer(bucket_key = "4a7796bd-b844-4c02-81db-66b0cb208a15",access_key="et2FqaeesA6KtWNxufN8smIRLQebb4z7")

streamer.log("My Messages", "Stream Starting")
for num in range(200, 300):
    time.sleep(0.1)
    streamer.log("My Numbers", num)
    if num%2 == 0:
        streamer.log("My Booleans", "false")
    else:
        streamer.log("My Booleans", "true")
    if num%3 == 0:
        streamer.log("My Events", "pop")
    if num%150 == 0:
        streamer.log("My Messages", "Stream Half Done")
streamer.log("My Messages", "Stream Done")
