import cv2
import mediapipe as mp


class FaceMesh:
    def __init__(self):
        self.mp_face = mp.solutions.face_mesh
        self.mp_draw = mp.solutions.drawing_utils
        self.mp_draw_styles = mp.solutions.drawing_styles

        self.mp_face_obj = self.mp_face.FaceMesh(max_num_faces=2)

        self.all_face = None

    def face_mesh(self, image):
        self.all_face = None

        results = self.mp_face_obj.process(image)
        if results.multi_face_landmarks:
            self.all_face = results.multi_face_landmarks

        return self.all_face

    def mesh_draw(self, image, connected=False):
        if self.all_face is None:
            return image

        for each_landmark in self.all_face:
            if connected:
                self.mp_draw.draw_landmarks(image=image,
                                            landmark_list=each_landmark,
                                            connections=self.mp_face.FACEMESH_CONTOURS,
                                            landmark_drawing_spec=None,
                                            connection_drawing_spec=self.mp_draw_styles.get_default_face_mesh_contours_style()
                                            )
                
            else:
                self.mp_draw.draw_landmarks(image=image,
                                            landmark_list=each_landmark,
                                            connections=self.mp_face.FACEMESH_TESSELATION,
                                            landmark_drawing_spec=None,
                                            connection_drawing_spec=self.mp_draw.DrawingSpec(color=(255,  255, 105), thickness=1, circle_radius=1)
                                            )
                
        return image