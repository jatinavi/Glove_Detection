# Gloved vs Ungloved Hand Detection

## Overview
Detects whether hands are gloved or bare using YOLOv8.

## Dataset
- **Roboflow – “glove-szkfk”** (only `gloved_hand` class).
- To meet project scope, manual labeling needed for `bare_hand` class or supplemental dataset.

## Model
- **YOLOv8n** fine-tuned for ~50 epochs on glove dataset.
- Achieved:
  - Precision: ~97.6%
  - Recall: ~93.9%
  - mAP@50: ~98.2%
  - 
## live Output Example --
## when there was 2 gloves in the image --
![Gloved Hand](https://github.com/jatinavi/Glove_Detection/blob/main/02_b143366b-b211-4004-8ffb-56d3a8038745_jpg.rf.806cf5381a7db99673bb463048c9f86e.jpg)
image 1/1 /content/glove-30/valid/images/02_b143366b-b211-4004-8ffb-56d3a8038745_jpg.rf.806cf5381a7db99673bb463048c9f86e.jpg: 608x640 2 glovess, 10.2ms
Speed: 6.5ms preprocess, 10.2ms inference, 2.4ms postprocess per image at shape (1, 3, 608, 640)
Results saved to runs/detect/predict2
Detected 2 glove(s)
## when there was no glove in the image --
![No Gloved Hand](https://github.com/jatinavi/Glove_Detection/blob/main/stock-photo-close-up-bare-hands-of-male-in-isolated-white-background-505624180.jpg)
image 1/1 /content/stock-photo-close-up-bare-hands-of-male-in-isolated-white-background-505624180.jpg: 480x640 (no detections), 41.1ms
Speed: 3.3ms preprocess, 41.1ms inference, 0.8ms postprocess per image at shape (1, 3, 480, 640)
Results saved to runs/detect/predict3
No Gloves
## How to Run Detection
```bash
python detection_script.py --input path/to/images --output output/ --logs logs/ --model best.pt --confidence 0.5
