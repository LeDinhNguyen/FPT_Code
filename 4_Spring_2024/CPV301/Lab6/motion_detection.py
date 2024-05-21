import cv2

capture = cv2.VideoCapture("./video.mp4")

frame_width = int(capture.get(3)) 
frame_height = int(capture.get(4)) 

size = (frame_width, frame_height) 

result = cv2.VideoWriter(
    'result_videos.avi',  
    cv2.VideoWriter_fourcc(*'MJPG'),
    10, size)

_, first_frame = capture.read()
first_frame = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_frame = cv2.GaussianBlur(first_frame, (21, 21), 0)

while True:
    ret, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21), 0)

    difference = cv2.absdiff(first_frame, gray)
    threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]


    # Apply morphological operations to reduce noise and fill gaps
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    fgmask = cv2.erode(threshold, kernel, iterations=2)
    fgmask = cv2.dilate(threshold, kernel, iterations=2)

    contours, hierachy = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue

        (x, y, w, h) = cv2.boundingRect(contour) # get Bouding box 
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    result.write(frame)
    cv2.imshow("Video Stream", frame)
    key = cv2.waitKey(1)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()