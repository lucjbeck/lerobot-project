import cv2

for index in range(5):
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
        ret, frame = cap.read()
        print(f"Camera index {index}: opened={cap.isOpened()}, frame_read={ret}")
        cap.release()
    else:
        print(f"Camera index {index}: not available")
