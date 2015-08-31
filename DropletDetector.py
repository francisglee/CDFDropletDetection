#Title				: DropletDetector.py
#Description		        : Utilizing OpenCV libraries in python to track droplets in video.
#Author				: M.B. Adams
#Date				: 08-14-2015
#Version			: 1.0
#Usage				: python DropletDetector.py
#Notes				: GUI for debugging, output in ASCII.
#Python Version		        : 2.6.6
#===========================================================================================

#Importing Libraries: OpenCV, and dropletobject.py
import cv2
import cv2.cv as cv
import numpy as np


#File I/O: Input file: Path to movie, path/name of output file, x_left, x_right, thres1, thres2, R_min, R_max
inputfile = open("VideoAnalysis.inp", "r")

VideoPath = inputfile.readline()[:-1]
DataFile = inputfile.readline()[:-1]
x_left = int(inputfile.readline())
x_right = int(inputfile.readline())
thres1 = int(inputfile.readline())
thres2 = int(inputfile.readline())
R_min = int(inputfile.readline())
R_max = int(inputfile.readline())

outfile = open(DataFile, "w")

#Path to video, grabbed by CV
VideoGrab = cv2.VideoCapture(VideoPath)

#Debugger, waiting for vid
while not VideoGrab.isOpened():
	VideoGrab = cv2.VideoCapture(VideoPath)
	cv2.waitKey(1000) #waitKey waits for a pressed key; the delay is 1s.
	print "Wait for the file to be available :)" #To indicate path is incorrect, or something wrong with video.

#Define the Frames of the VideoGrab
PosFrame = VideoGrab.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)


#===========================================================================================
# DETECTION
#===========================================================================================
while True:
	flag, Frame = VideoGrab.read() #Reading the Frames

	if flag:
		Frame = Frame[:,x_left:-1*x_right] #Cropping
		Frame = cv2.cvtColor(Frame, cv2.cv.CV_RGB2GRAY) #Convert to gray scale
		Frame = cv2.Canny(Frame,thres1,thres2) #Canny edge effects with thresholding levels
		#Hough circle algorithm
		circles = cv2.HoughCircles(Frame, cv2.cv.CV_HOUGH_GRADIENT, 3, 200, minRadius=R_min, maxRadius=R_max)
		#If frames have no circles
		if circles is None:
			continue
		circles = np.uint16(np.around(circles))
		for i in circles[0,:]:
			#Draw the outer circle
			cv2.circle(Frame,(i[0], i[1]), i[2], (255,255,255), 2)
			#Draw the center of the circle
			cv2.circle(Frame,(i[0], i[1]), 2, (255,255,255), 3)
			#File I/O: Columns are frame number, (x,y) coordinates of the center, and radius
			outfile.write("{0}\t{1}\t{2}\t{3}\n".format(str(PosFrame),i[0],i[1],i[2]))
		cv2.imshow('Video', Frame) #Shows the video
		PosFrame = VideoGrab.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
	else:
		VideoGrab.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, PosFrame-1)
		print "Frame is not ready"
		cv2.waitKey(1000) #Otherwise it does not run the video and counts back one.

#Break options: waitKey intrinsically requires an escape option by the user (hence decimal 27 = escape)
	if cv2.waitKey(10) == 27:
		break

#Here we break when the number of frames = number of frames in the video, i.e. stops when the video does
	if VideoGrab.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) == VideoGrab.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
		break

#File I/O
close.outfile()
close.inputfile()
