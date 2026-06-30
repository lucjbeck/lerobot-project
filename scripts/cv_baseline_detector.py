import cv2
import numpy as np

CAMERA_INDEX = 0

COLOR_RANGES = {
    "red1": ((0, 80, 80), (10, 255, 255)),
    "red2": ((170, 80, 80), (180, 255, 255)),
    "blue": ((90, 80, 80), (130, 255, 255)),
    "green": ((35, 60, 60), (85, 255, 255)),
}


def get_zone(x, width):
    if x < width / 3:
        return "left"
    if x < 2 * width / 3:
        return "center"
    return "right"


def main():
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open camera index {CAMERA_INDEX}")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame")
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        height, width = frame.shape[:2]

        masks = {}
        red_mask_1 = cv2.inRange(hsv, np.array(COLOR_RANGES["red1"][0]), np.array(COLOR_RANGES["red1"][1]))
        red_mask_2 = cv2.inRange(hsv, np.array(COLOR_RANGES["red2"][0]), np.array(COLOR_RANGES["red2"][1]))
        masks["red"] = red_mask_1 | red_mask_2
        masks["blue"] = cv2.inRange(hsv, np.array(COLOR_RANGES["blue"][0]), np.array(COLOR_RANGES["blue"][1]))
        masks["green"] = cv2.inRange(hsv, np.array(COLOR_RANGES["green"][0]), np.array(COLOR_RANGES["green"][1]))

        best = None
        for color, mask in masks.items():
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if not contours:
                continue
            contour = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(contour)
            if area < 300:
                continue
            x, y, w, h = cv2.boundingRect(contour)
            cx = x + w // 2
            cy = y + h // 2
            if best is None or area > best["area"]:
                best = {"color": color, "area": area, "bbox": (x, y, w, h), "center": (cx, cy)}

        if best:
            x, y, w, h = best["bbox"]
            cx, cy = best["center"]
            zone = get_zone(cx, width)
            label = f"{best['color']} / {zone}"
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
            cv2.circle(frame, (cx, cy), 5, (255, 255, 255), -1)
            cv2.putText(frame, label, (x, max(20, y - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            print(label)

        cv2.imshow("Color detector", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
