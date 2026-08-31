<img width="1280" height="720" alt="banner1" src="https://github.com/user-attachments/assets/dd7dd623-ee17-451a-9846-85067b2d5d77" />
## Synthetic Glass & Transparent Packaging Dataset (YOLO BBox + Segment)

A photorealistic **synthetic computer vision dataset** for transparent glass and packaging objects, designed for object detection and image segmentation under challenging lighting conditions. The dataset is intended for YOLO validation, transparent object detection, instance segmentation, synthetic-to-real experiments, and computer-vision research involving transparent and reflective materials.

This repository contains a **3-image sample dataset** with dual ground-truth annotations so you can test pipeline compatibility instantly.

## Dataset at a Glance

| Property | Details |
|---|---|
| Dataset type | Synthetic computer vision dataset |
| Objects | Transparent glass and packaging |
| Images | 240 |
| Resolution | 1024 × 1024 |
| Training split | 200 images |
| Validation split | 40 images |
| Detection annotations | YOLO bounding boxes |
| Segmentation annotations | YOLO instance segmentation polygons |
| Image format | PNG |
| Annotation format | YOLO `.txt` |
| Ground truth | Generated from 3D scene data |
| Primary tasks | Object detection and instance segmentation |
| Material challenges | Transparency, reflections, refractions, specular highlights |
| License | Commercial single-team license |

## 🛒 Download the Full Production Dataset (240 Images)

To fine-tune or evaluate your models on the complete dataset, access the full pack on Gumroad:

👉 **[Download Full Dataset on Gumroad ($49)](https://5940734191807.gumroad.com/l/yafpul)**

### Full Dataset Specifications

* **240 Renders @ 1024x1024:** 200 Train / 40 Val at native resolution.
* **Synthetic Computer Vision Dataset:** Photorealistic renders of transparent glass and packaging objects.
* **Dual Ground-Truth Annotations:** Includes both 2D Bounding Boxes (`labels_box/`) and Multi-Point Instance Segmentation Polygons (`labels_segment/`).
* **Physics-Based Ground Truth:** Annotations are generated directly from the underlying 3D scene, avoiding manual labeling errors.
* **Challenging Transparent Materials:** Designed to capture transparency, specular highlights, reflections, and surface refractions under difficult lighting conditions.
* **YOLO Compatible:** Bounding boxes and instance segmentation annotations are provided in YOLO-compatible format.
* **Commercial Single-Team License:** Royalty-free commercial usage rights to train, evaluate, and deploy models.

---

## Repository Structure

```text
.
├── data/
│   ├── images/          # Sample 1024x1024 PNG renders
│   ├── labels_box/      # YOLO format bounding box annotations (.txt)
│   └── labels_segment/  # YOLO format instance segmentation polygons (.txt)
├── src/
│   └──visualize_sample.py  # Script to draw bounding box and polygon overlays
└── README.md
```

## Applications

This synthetic glass object detection dataset can be used for:

- Transparent object detection
- Glass and transparent packaging detection
- YOLO object detection
- Instance segmentation
- Synthetic-to-real computer vision experiments
- Robotics and 3D vision research
