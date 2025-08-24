# Part 2: Reasoning-Based Questions

## Q1: Choosing the Right Approach
I would use **object detection** to identify whether a product is missing its label because it allows the model to locate the label on each item. Simple classification wouldn’t work well since the products look almost identical, and segmentation might be more detailed than necessary. Detection helps focus only on the area where the label should be. If detection struggles, I would try **binary classification** on cropped images of each product to predict labeled vs unlabeled as a fallback.

## Q2: Debugging a Poorly Performing Model
If my model performs poorly on new factory images, I would start by **visualizing predictions versus the actual labels** to see where it fails. I’d check if the new images have differences in lighting, angle, or background compared to my training set. I’d also test data augmentation to handle these variations. Reviewing class balance and label quality is important, and analyzing a **confusion matrix** can show which classes the model struggles with. Adding more representative images from the factory could improve performance.

## Q3: Accuracy vs Real Risk
In this case, **accuracy is misleading** because missing even a few defective products can have serious consequences. Instead, I would look at **recall**, which measures how many defective products are correctly detected. Precision matters too, but recall is more critical for safety. A high recall ensures that fewer defective items slip through, even if overall accuracy drops a little. A confusion matrix would help me understand false negatives and false positives better.

## Q4: Annotation Edge Cases
I would include blurry or partially visible objects in the dataset if they reflect real-world conditions because the model needs to handle such scenarios. However, I would label them carefully to avoid confusion. The trade-off is that some noisy labels might slightly reduce accuracy, but excluding them could make the model fail in real situations. Balancing dataset quality with practical coverage is key to creating a robust model.
