# OpenCV

## Library Installation
- `pip install -r cv_requirements.txt`

## OpenCV Face & Eye Detection
- Face & Eye detection using OpenCV [Haarcascades XML](https://github.com/opencv/opencv/tree/master/data/haarcascades) data
- Detection from Image/WebCam [[cv_face_detect_sample.py](cv_face_detect_sample.py)]
  - Image:
    - `python cv_face_detect_sample.py --image static/demo_face_eye/female.jpg --face True`
    - `python cv_face_detect_sample.py --image static/demo_face_eye/female.jpg --eye True`
    - `python cv_face_detect_sample.py --image static/demo_face_eye/male.jpg --face True --eye True`
  - WebCam
    - `python cv_face_detect_sample.py --video True --face True --eye True`
    <table>
      <tr align='center'>
      <td><img src="static/demo_face_eye/male_box.jpg" alt="Male.jpg" width="230" height="270"/></td>
      <td><img src="static/demo_face_eye/female_box.jpg" alt="Female.jpg" width="230" height="270"/></td>
      </tr>
    </table>
## Referecne
- OpenCV [Haarcascade](https://github.com/opencv/opencv/tree/master/data/haarcascades)
  - Sample Female photo by <span><a href="https://unsplash.com/@michaeldam?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Michael Dam</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>
  - Sample Male photo by <span> <a href="https://unsplash.com/@erik_lucatero?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Erik Lucatero</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>
