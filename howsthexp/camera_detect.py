import os
import cv2
import numpy as np
from keras.models import model_from_json,load_model
from keras.preprocessing import image
import time
from collections import Counter
#import playsound
#import pygame

model = model_from_json(open("fer.json","r").read())
model.load_weights('fer.h5')

# face_haar_cascade = cv2.CascadeClassifier('harcascade_frontalface_default.xml')
face_cascade=cv2.CascadeClassifier('harcascade_frontalface_default.xml')
print(face_cascade)
cap = cv2.VideoCapture(0)
i=0
ls=[]
while True:
    ret,test_img=cap.read()
    if not ret:
        continue
    gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)

    # faces_detected = face_cascade.detectMultiscale(gray_img,1.32,5)
    faces_detected=face_cascade.detectMultiScale(gray_img,1.3,5)
    for (x,y,w,h) in faces_detected:
        cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=7)

        roi_gray=gray_img[y:y+w,x:x+h]
        roi_gray = cv2.resize(roi_gray,(48,48))
        img_pixels = image.img_to_array(roi_gray)

        img_pixels = np.expand_dims(img_pixels,axis=0)

        img_pixels/=255

        predictions = model.predict(img_pixels)

        max_index = np.argmax(predictions[0])

        emotions = ('angry','disgust','fear','happy','sad','surprise','neutral')

        predicted_emotion = emotions[max_index]
        print('predicted emotion',predicted_emotion)
        if(i%5==0):
            ls.append(predicted_emotion)
        cv2.putText(test_img,predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    resized_img = cv2.resize(test_img, (1000, 700))

    cv2.imshow('Facial emotion analysis ',resized_img)
    i=i+1

    if cv2.waitKey(10) == ord('q'):
        break

    elif i==60:
        break

# cv2.release()
print(ls)
# using Counter() + set() + list comprehension
# list frequency of elements
res = dict(Counter(ls))
print(res)
Keymax = max(res, key=res.get)
print('your emotion is ',Keymax)

cap.release()
cv2.destroyAllWindows()
# pygame.init()
# pygame.mixer.music.load('/home/ekta/pyproject/song.wav')
# pygame.mixer.music.play()
# time.sleep(100)
# pygame.mixer.music.stop()

# playsound.playsound('/home/ekta/pyproject/song.mp3', True)
