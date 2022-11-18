print("[START J.C.I]")
from playsound import playsound
from threading import Thread
from time import sleep
Thread(target=playsound, args=("J.C.I/start.mp3",)).start()
startup = ["GUI"]
#["Jessica", "Cloud", "Initialization", "GUI"]
error = 0
sleep(7)
for i in startup:
    if i == "Jessica":
        try:
            playsound("J.C.I/start_jessi.mp3")
            import Jessica.main
            Thread(target=Jessica.main.start_js, args=("start",)).start()
            playsound("J.C.I/end_jessi.mp3")
        except:
            plausound("J.C.I/error_jessi.mp3")
            error += 1
    if i == "Cloud":
        try:
            playsound("J.C.I/start_cloud.mp3")
            import Cloud.main
            Thread(target=Cloud.main.init, args=("start",)).start()
            playsound("J.C.I/end_cloud.mp3")
        except:
            playsound("J.C.I/error_cloud.mp3")
            error += 1
    if i == "Initialization":
        try:
            playsound("J.C.I/start_initialization.mp3")
            import Initialization.server
            Thread(target=Initialization.server.init, args=()).start()
            playsound("J.C.I/end_initialization.mp3")
        except:
            playsound("J.C.I/error_initialization.mp3")
            error += 1
    if i == "GUI":
        try:
            playsound("J.C.I/start_GUI.mp3")
            import GUI.main
            Thread(target=GUI.main.prog, args=()).start()
            playsound("J.C.I/end_GUI.mp3")
        except:
            playsound("J.C.I/error_GUI.mp3")
            error += 1

if error > 0:
    playsound("J.C.I/error_start1.mp3")



