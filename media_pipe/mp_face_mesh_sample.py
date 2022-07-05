import argparse
import time

import cv2

from custom_lib.mediapipe_face_mesh import FaceMesh


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--connected', type=bool, default=False,
                        required=False, help='Connect the landmark')

    
    args = parser.parse_args()
    connected = bool(args.connected)

    video = cv2.VideoCapture(0)
    face_obj = FaceMesh()

    
    while True:
        status, frame = video.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect all faces in a image
        face_obj.face_mesh(frame_rgb)
        
        # Plot all faces in a image
        face_obj.mesh_draw(frame, connected=connected)

        cv2.imshow('Face Mesh Detection', frame)
        cv2.waitKey(1)