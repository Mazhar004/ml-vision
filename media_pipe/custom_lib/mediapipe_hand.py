import cv2
import mediapipe as mp


class HandDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.mp_hand_obj = self.mp_hands.Hands()

        self.all_hand = None

    def hand_detect(self, image):
        self.all_hand = None

        results = self.mp_hand_obj.process(image)
        if results.multi_hand_landmarks:
            self.all_hand = results.multi_hand_landmarks

        return self.all_hand

    def hand_draw(self, image, connected=False):
        if self.all_hand is None:
            return image

        for each_landmark in self.all_hand:
            if connected:
                self.mp_draw.draw_landmarks(image, each_landmark, self.mp_hands.HAND_CONNECTIONS)
            else:
                self.mp_draw.draw_landmarks(image, each_landmark)
        return image

    def get_lm_point(self, idx=None):
        if self.all_hand is None:
            return []

        if idx is None:
            return [each_hand.landmark for each_hand in self.all_hand]
        else:
            return [[each_hand.landmark[idx]] for each_hand in self.all_hand]

    def lm_point_draw(self, image, all_hand_lm_point):
        h, w, c = image.shape
        for each_hand_lm_points in all_hand_lm_point:
            for point in each_hand_lm_points:
                cx, cy = map(int, [w*point.x, h*point.y])
                cv2.circle(image, (cx, cy), 15, (0, 0, 255), cv2.FILLED)
        return image