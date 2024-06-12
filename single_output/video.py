from config import *
import cv2



class Video:
    def __init__(self):
        self.playing = False
        self.video_path = VIDEO_PATH + 'flaminghott.mp4'


    def play(self):
        while True:
            while self.playing:
                self.cap = cv2.VideoCapture(self.video_path)

                if not self.cap.isOpened():
                    print("Error: Could not open video.")
                    exit()

                cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

                while self.cap.isOpened():
                    ret, frame = self.cap.read()
                    if not ret:
                        break

                    cv2.imshow('Video', frame)

                    if (cv2.waitKey(25) & 0xFF == ord('q')) or (not self.playing):
                        self.cap.release()
                        cv2.destroyAllWindows()
                        break


    def set_playing(self, playing):
        if playing:
            self.playing = True
        else:
            self.playing = False