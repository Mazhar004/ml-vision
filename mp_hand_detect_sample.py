import cv2
import time

from custom_lib.mediapipe_hand import HandDetector


def show_fps(frame, ptime):
    ctime = time.time()
    fps = int(1/(ctime-ptime))
    ptime = ctime
    cv2.putText(frame, str(fps), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    return frame, ptime


ptime = time.time()
video = cv2.VideoCapture(0)
hand_obj = HandDetector()

while True:
    status, frame = video.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Detect all hands in a image
    hand_obj.hand_detect(frame_rgb)

    # Plot all hands in a image
    hand_obj.hand_draw(frame, connected=True)

    # Plot specifi landmark point in image
    lm_point = hand_obj.get_lm_point(4)
    hand_obj.lm_point_draw(frame, lm_point)

    # Show FPS in a image
    frame, ptime = show_fps(frame, ptime)

    cv2.imshow('Hand detection', frame)
    cv2.waitKey(1)