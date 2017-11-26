#import iot_temp_humidity.main as th
#import iot_pir.main as pir
import os
from threading import Thread


class TempAndHumidityThread(Thread):
    def run(self):
        print '1'
        #th.scheduleAndDoAll()

class PirThread(Thread):
    def run(self):
        print '2'
        #pir.start()

if __name__ == '__main__':
    os.system("sudo uv4l -nopreview --auto-video_nr --driver raspicam --encoding mjpeg --width 640 --height 480 --framerate 20 --server-option '--port=9090' --server-option '--max-queued-connections=30' --server-option '--max-streams=25' --server-option '--max-threads=29'")

    thThread = TempAndHumidityThread()
    thThread.setName('temp_and_humidity')

    pirThread = PirThread()
    pirThread.setName('pir')

    thThread.start()
    pirThread.start()

