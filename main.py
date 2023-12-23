import os
import io
from google.cloud import vision_v1
from google.cloud.vision_v1 import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'

client = vision_v1.ImageAnnotatorClient()

FILE_NAME = 'PC.jpg'
FOLDER_PATH = r'D:\Jaipur Police Hackathon'
OUTPUT_FILE = 'output.txt'

def detect_text_from_image(file_path, output_file):

    image_path = os.path.join(FOLDER_PATH, FILE_NAME)

    try:
        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision_v1.types.Image(content=content)

        response = client.document_text_detection(image=image)
        doc_text = response.full_text_annotation.text

        output_path = os.path.join(FOLDER_PATH, output_file)
        with open(output_path, 'w', encoding='utf-8') as out_file:
            out_file.write(doc_text)

        print(f"Text written to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

detect_text_from_image(FOLDER_PATH, OUTPUT_FILE)
