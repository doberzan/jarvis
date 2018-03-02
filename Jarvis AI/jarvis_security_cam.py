import numpy as np
import cv2
class Security_Camera:
	def record(self):
		face_cascade = cv2.CascadeClassifier('./face.xml')
		cap = cv2.VideoCapture(0)
		fourcc = cv2.VideoWriter_fourcc(*'XVID')
		out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
		out2 = cv2.VideoWriter('output2.avi',fourcc, 20.0, (640,480))
		time = 0
		#face_cascade = cv2.CascadeClassifier('./face_rec/haarcascade_frontalface_default.xml')
		while(True):
			time = time + 1
			ret, frame = cap.read()
			#faces = face_cascade.detectMultiScale(gray, 1.3, 5)
			#img = frame
			#for (x,y,w,h) in faces:
			#	img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			if ret==True and time < 200:
				out.write(frame)
			else:
				break
		cap.release()
		out.release()

		cap2 = cv2.VideoCapture('./output.avi')
		if (cap2.isOpened() == False): 
		  print("Error opening video stream or file")
		time = 0
		while(cap2.isOpened()):
		  time = time + 1
		  ret2, img2 = cap2.read()
		  if ret2 == True:
			gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
			faces = face_cascade.detectMultiScale(gray2, 1.3, 5)
			print ("%s : %s" % (len(faces),time))
			for (x,y,w,h) in faces:
				img2 = cv2.rectangle(img2,(x,y),(x+w,y+h),(255,0,0),2)
			out2.write(img2)
		  else: 
		    break
		 
		cap2.release()
		out2.release()
		cv2.destroyAllWindows()
		return True
