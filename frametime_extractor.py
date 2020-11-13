import cv2

video = cv2.VideoCapture('RoomShoot_2_P20_frontcamera.mp4')
i=000000
print('FPS= ' + str(video.get(cv2.CAP_PROP_FPS)) + '\n')

while video.isOpened():
  	ret,frame = video.read()
  	if ret == False : break
  	
  	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
  	
  	cv2.imwrite(str(i).zfill(6)+'.png',gray)
  	
  	with open('times.txt', 'a') as the_file: #nome del file timestamp
    		the_file.write(str(int(video.get(cv2.CAP_PROP_POS_MSEC))/1000) + ' ' + str(i).zfill(6) + '.png\n') #timestimap in seconds
    		#the_file.write(str(i).zfill(6) +'\n') #just stamps
  	i+=1
