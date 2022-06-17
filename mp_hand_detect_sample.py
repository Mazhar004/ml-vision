import argparse
import time

import cv2

from custom_lib.mediapipe_hand import HandDetector


def show_fps(frame, ptime):
    ctime = time.time()
    fps = int(1/(ctime-ptime))
    ptime = ctime
    cv2.putText(frame, str(fps), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    return frame, ptime



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--all_lm', type=bool, default=False,
                        required=False, help='Plot all hand landmark within an image')
    parser.add_argument('--connected', type=bool, default=False,
                        required=False, help='Connect the landmark')
    parser.add_argument('--lm', type=int, default=-1,
                        required=False, help='Get specific landmark [0-19]')
    parser.add_argument('--fps', type=bool, default=False,
                        required=False, help='It will display the FPS')

    
    args = parser.parse_args()
    connected = bool(args.connected)

    if args.fps:
        ptime = time.time()
    
    video = cv2.VideoCapture(0)
    hand_obj = HandDetector()

    
    while True:
        status, frame = video.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect all hands in a image
        hand_obj.hand_detect(frame_rgb)
        
        if args.all_lm:
            # Plot all hands in a image
            hand_obj.hand_draw(frame, connected=connected)

        if args.lm!=-1:
            # Plot specifi landmark point in image, I used index 4 for thumb
            lm_point = hand_obj.get_lm_point(args.lm)
            hand_obj.lm_point_draw(frame, lm_point)

        if args.fps:
            # Show FPS in a image
            frame, ptime = show_fps(frame, ptime)

        cv2.imshow('Hand detection', frame)
        cv2.waitKey(1)