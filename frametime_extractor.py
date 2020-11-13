import cv2

video = cv2.VideoCapture('INSERT_PATH_OR_NAME_OF_VIDEOFILE_HERE.mp4')
i=000000

print('FPS= ' + str(video.get(cv2.CAP_PROP_FPS)) + '\n') #additional fps info in console 

while video.isOpened():
  	ret,frame = video.read()
  	if ret == False : break
  	
  	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #get grayscale frames
  	
  	cv2.imwrite(str(i).zfill(6)+'.png',gray)
  	
  	with open('times.txt', 'a') as the_file: #nome del file timestamp
    		the_file.write(str(int(video.get(cv2.CAP_PROP_POS_MSEC))/1000) + ' ' + str(i).zfill(6) + '.png\n') #writing in file, timestimap in seconds
    		#the_file.write(str(i).zfill(6) +'\n') #writes just the stamps
        
  	i+=1
