import os
import cv2
import torch
import logging
import pandas as pd

# Configure logging
logging.basicConfig(
    filename='object_detection.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Load YOLO model
try:
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', source='github')
    logging.info("YOLO model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading YOLO model: {e}")
    exit()

# Define paths
IMAGE_DIR = os.path.abspath("../data/scraped_images")
DETECTION_RESULTS_DIR = os.path.abspath("../data")
DETECTION_RESULTS = os.path.join(DETECTION_RESULTS_DIR, "detection_results.csv")

# Ensure the image directory exists
if not os.path.exists(IMAGE_DIR):
    logging.error(f"Error: Image directory '{IMAGE_DIR}' not found.")
    exit()

# Ensure the detection results directory exists
os.makedirs(DETECTION_RESULTS_DIR, exist_ok=True)

# Process each image
results = []
for image_name in os.listdir(IMAGE_DIR):
    image_path = os.path.join(IMAGE_DIR, image_name)
    if os.path.isfile(image_path):
        try:
            img = cv2.imread(image_path)
            result = model(img)
            result.save()  # Save results to file
            results.append(result.pandas().xyxy[0])  # Collect results
            logging.info(f"Processed image: {image_name}")
        except Exception as e:
            logging.error(f"Error processing image '{image_name}': {e}")

# Filter out empty DataFrames
results = [df for df in results if not df.empty]

# Save detection results
if results:
    try:
        results_df = pd.concat(results, ignore_index=True)
        results_df.to_csv(DETECTION_RESULTS, index=False)
        logging.info(f"Saved detection results to: {DETECTION_RESULTS}")
    except Exception as e:
        logging.error(f"Error saving detection results: {e}")
else:
    logging.info("No detection results to save.")