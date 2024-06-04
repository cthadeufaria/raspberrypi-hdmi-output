from time import sleep
import threading

from sensor import Sensor
from video import Video



def main():
    sensor = Sensor(trigger=18, echo=24)
    video = Video()

    sensor_thread = threading.Thread(target=sensor.listen)
    video_thread = threading.Thread(target=video.play)
    
    sensor_thread.start()
    video_thread.start()

    while True:
        sleep(0.1)

        print("Distance: {} cm".format(sensor.distance))

        if sensor.in_range:
            video.set_playing(True)
        else:
            video.set_playing(False)


if __name__ == "__main__": 
    main()