import iot_temp_humidity.main as th
import iot_pir.main as pir
import os

def start()
    th.scheduleAndDoAll()
    print "temp and humidity started"
    pir.start()
    print "pir started"
    os.system("sudo uv4l -nopreview --auto-video_nr --driver raspicam --encoding mjpeg --width 640 --height 480 --framerate 20 --server-option '--port=9090' --server-option '--max-queued-connections=30' --server-option '--max-streams=25' --server-option '--max-threads=29'")
    print "uv4l streaming started"