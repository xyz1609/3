import os
import shutil
import cv2

video = r"C:/Users/hammad/Desktop/MSC IT Part1/Data Science/nature.mp4"
out_dir = r"C:/VKHCG/05-DS/9999-Data/temp/"

# Clean output folder
shutil.rmtree(out_dir, ignore_errors=True)
os.makedirs(out_dir, exist_ok=True)

print("=== Start Movie to Frames ===")

cap = cv2.VideoCapture(video)
if not cap.isOpened():
    print("ERROR: Cannot open video.")
else:
    count = 0
    while True:
        ret, frame = cap.read()
        if not ret or count > 100:
            break

        fname = os.path.join(out_dir, f"nature-frame-{count:04d}.jpg")
        cv2.imwrite(fname, frame)
        print("Extracted:", fname)

        if os.path.getsize(fname) == 0:
            os.remove(fname)
            print("Removed:", fname)
            continue

        count += 1

print("Generated:", count, "frames")
print("=== Done ===")
