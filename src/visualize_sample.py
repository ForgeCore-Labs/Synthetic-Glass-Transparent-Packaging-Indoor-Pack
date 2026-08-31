import cv2
import numpy as np
from pathlib import Path

# Paths to your folders
DATA_DIR = Path("data")
IMG_DIR = DATA_DIR / "images"
BOX_DIR = DATA_DIR / "labels_box"
SEG_DIR = DATA_DIR / "labels_segment"
OUTPUT_DIR = Path("preview_output")

OUTPUT_DIR.mkdir(exist_ok=True)

# Define label colors (BGR format)
COLOR_BOX = (0, 255, 0)     # Green for Bounding Box
COLOR_SEG = (255, 0, 0)     # Blue for Segmentation Polygon

images = list(IMG_DIR.glob("*.*"))

if not images:
    print(f"❌ No images found in {IMG_DIR}")
    exit(1)

print(f"Found {len(images)} sample images. Generating preview overlays...")

for img_path in images:
    img = cv2.imread(str(img_path))
    if img is None:
        continue

    h, w, _ = img.shape
    base_name = img_path.stem

    # 1. Overlay Bounding Boxes (if present)
    box_path = BOX_DIR / f"{base_name}.txt"
    if box_path.exists():
        with open(box_path, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) < 5:
                    continue
                
                # YOLO format: class x_center y_center width height (normalized)
                cls, xc, yc, bw, bh = map(float, parts[:5])
                
                x1 = int((xc - bw / 2) * w)
                y1 = int((yc - bh / 2) * h)
                x2 = int((xc + bw / 2) * w)
                y2 = int((yc + bh / 2) * h)

                cv2.rectangle(img, (x1, y1), (x2, y2), COLOR_BOX, 2)
                cv2.putText(img, f"Box: {int(cls)}", (x1, max(y1 - 5, 15)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR_BOX, 2)

    # 2. Overlay Segment Polygons (if present)
    seg_path = SEG_DIR / f"{base_name}.txt"
    if seg_path.exists():
        with open(seg_path, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) < 3:
                    continue
                
                cls = int(parts[0])
                coords = list(map(float, parts[1:]))

                # Reconstruct (x, y) pixel coordinates
                pts = []
                for i in range(0, len(coords), 2):
                    px = int(coords[i] * w)
                    py = int(coords[i + 1] * h)
                    pts.append([px, py])

                pts = np.array(pts, dtype=np.int32).reshape((-1, 1, 2))
                cv2.polylines(img, [pts], isClosed=True, color=COLOR_SEG, thickness=2)

    # Save output preview image
    out_file = OUTPUT_DIR / f"{base_name}_preview.jpg"
    cv2.imwrite(str(out_file), img)
    print(f"✅ Saved overlay preview: {out_file}")

print(f"\n🚀 Visualization complete! Check the '{OUTPUT_DIR}' folder.")