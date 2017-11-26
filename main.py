import iot_temp_humidity.main as th
import iot_pir.main as pir
import os
import Thread

def Thread1():
    print "temp and humidity started"
    th.scheduleAndDoAll()

def Thread2():
    print "pir started"
    pir.start()

def Thread3():
    os.system("sudo uv4l -nopreview --auto-video_nr --driver raspicam --encoding mjpeg --width 640 --height 480 --framerate 20 --server-option '--port=9090' --server-option '--max-queued-connections=30' --server-option '--max-streams=25' --server-option '--max-threads=29'")
    print "uv4l streaming started"

#thread.start_new_thread(Thread1, ())
#thread.start_new_thread(Thread2, ())
#thread.start_new_thread(Thread3, ())
    Thread3()