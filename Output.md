# Gloved vs Ungloved Hand Detection - Results and Outputs

## Model Training Summary
- **Model:** YOLOv8n  
- **Epochs:** 50  
- **Training Time:** 2.517 hours  
- **Parameters:** 3,005,843  
- **GFLOPs:** 8.1  
- **Optimizer:** Stripped from `last.pt` and `best.pt` (6.2MB each)

### Validation Metrics
| Class   | Images | Instances | Precision | Recall | mAP@50 | mAP@50-95 |
|---------|--------|-----------|-----------|--------|--------|-----------|
| gloves  | 828    | 1775      | 0.976     | 0.939  | 0.982  | 0.824     |

- **Fitness:** 0.839  
- **Inference Speed per Image:** 2.2ms  
- **Postprocess Speed:** 2.4ms  

---

## Sample Detection Outputs

### 1. Gloved Hands
![Gloved Hands](https://github.com/jatinavi/Glove_Detection/blob/main/02_b143366b-b211-4004-8ffb-56d3a8038745_jpg.rf.806cf5381a7db99673bb463048c9f86e.jpg)

**Detection Output:** 2 gloves detected  

---

### 2. Bare Hands
![Bare Hands](https://github.com/jatinavi/Glove_Detection/blob/main/stock-photo-close-up-bare-hands-of-male-in-isolated-white-background-505624180.jpg)

**Detection Output:** No gloves detected  

---

**Conclusion:**  
The YOLOv8n model successfully detects gloved and bare hands with high accuracy (mAP@50: 0.982). It is suitable for safety compliance applications on images or video streams.  
