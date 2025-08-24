import os
import cv2
import json
import argparse
from ultralytics import YOLO

def run_detection(input_folder, output_folder, log_folder, model_path, confidence):
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(log_folder, exist_ok=True)

    model = YOLO(model_path)

    for img_name in os.listdir(input_folder):
        if not img_name.lower().endswith('.jpg'):
            continue
        img_path = os.path.join(input_folder, img_name)
        results = model.predict(source=img_path, conf=confidence)
        img = cv2.imread(img_path)

        detections = []
        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                conf = float(box.conf[0])
                cls_id = int(box.cls[0])
                label = model.names[cls_id]

                detections.append({
                    "label": label,
                    "confidence": conf,
                    "bbox": [x1, y1, x2, y2]
                })

                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img, f"{label} {conf:.2f}", (x1, y1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cv2.imwrite(os.path.join(output_folder, img_name), img)
        log = {"filename": img_name, "detections": detections}
        with open(os.path.join(log_folder, img_name.replace('.jpg', '.json')), 'w') as f:
            json.dump(log, f, indent=2)

    print("Detection complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input folder (.jpg)")
    parser.add_argument("--output", default="output", help="Where annotated images go")
    parser.add_argument("--logs", default="logs", help="Where JSON logs go")
    parser.add_argument("--model", default="best.pt", help="Trained YOLO model")
    parser.add_argument("--confidence", type=float, default=0.5, help="Confidence threshold")
    args = parser.parse_args()

    run_detection(args.input, args.output, args.logs, args.model, args.confidence)
