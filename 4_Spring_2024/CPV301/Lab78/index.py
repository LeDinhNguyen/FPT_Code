### Record video
# import cv2

# capture = cv2.VideoCapture(0)

# frame_width = int(capture.get(3)) 
# frame_height = int(capture.get(4)) 

# size = (frame_width, frame_height) 

# result = cv2.VideoWriter(
#     'video.avi',  
#     cv2.VideoWriter_fourcc(*"MJPG"),
#     10, size)

# while True:
#     status, frame = capture.read()
#     if not status:
#         break

#     cv2.imshow("a", frame)

#     result.write(frame)
#     if cv2.waitKey(1) == ord('q'):
#         break

import cv2
video = cv2.VideoCapture("./video_motion.avi")

while True:
    sta, frame = video.read()
    print(frame)
    if not sta:
        break

    cv2.imshow("a", frame)
    if cv2.waitKey(1) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()

### Face Detection
# import cv2

# face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# video_cap = cv2.VideoCapture("./video_motion.avi")
# ### Identifuing faces in the video stream
# #### draw the bouding box
# def detect_face (vid):
#     gray = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
#     faces = face_classifier.detectMultiScale(gray, 1.1,5,minSize=(40,40))
#     for (x,y,w,h) in faces:
#         cv2.rectangle(vid, (x,y), (x+w, y+h),(0,255,0),4)
#     return faces
# ### Creating a loop for real_time face detection
# while True:
#     result, video_frame = video_cap.read()
#     if result is False:
#         break
#     faces = detect_face(video_frame)
#     cv2.imshow('Face detection', video_frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# video_cap.release()
# cv2.destroyAllWindows()

### Face Recognition
# import cv2

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
#     for (x,y,w,h) in faces:
#         print(x,y,w,h)
#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = frame[y:y+h, x:x+w]
#         cv2.imwrite("image_gray.png", roi_gray)
#         cv2.imwrite('image_color.png', roi_color)
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(20)& 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows() 