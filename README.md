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

## How to Run Detection
```bash
python detection_script.py --input path/to/images --output output/ --logs logs/ --model best.pt --confidence 0.5
