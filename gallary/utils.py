import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import os
import cv2
from PIL import Image
import io
from django.core.files.base import ContentFile


class Detector:
    def __init__(self):
        model_path =  os.path.join("media", "efficientdet_lite0.tflite")
        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.ObjectDetectorOptions(base_options=base_options,
                score_threshold=0.5)

        self.detector = vision.ObjectDetector.create_from_options(options)

    def detect(self, image_path):
        image = mp.Image.create_from_file(image_path)
        detection_results = self.detector.detect(image)

        return detection_results

    def visualize(self, image_path, detection_results):
        margin = 15
        row = 20
        color = (255, 255, 255)


        result_image = cv2.imread(image_path)

        for detection in detection_results.detections:
            bbox = detection.bounding_box
            start_point = (bbox.origin_x, bbox.origin_y)
            end_point = (start_point[0] + bbox.width, start_point[1] + bbox.height)

            cv2.rectangle(
                    result_image,
                    start_point,
                    end_point,
                    color,
                    )

            category = detection.categories[0]
            category_name = category.category_name
            text_location = (margin + start_point[0], row + start_point[1])

            font_scale = 1
            thinkness = 2

            cv2.putText(
                    result_image,
                    category_name,
                    text_location,
                    cv2.FONT_HERSHEY_COMPLEX,
                    font_scale,
                    color,
                    thinkness
                    )

        result_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)
        return result_image




def save_processed_image(image_mat, instance):
    image_name = "processed_image_"  + instance.image.url.split("/")[-1]
    image = Image.fromarray(image_mat)
    image_io = io.BytesIO()
    image.save(image_io, format="jpeg")

    image_file = ContentFile(image_io.getvalue(), image_name)
    instance.processed_image.save(image_name, image_file, save=True)














