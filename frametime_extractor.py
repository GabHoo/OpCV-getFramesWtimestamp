import cv2

video = cv2.VideoCapture('$INSERT NAME OR PATH.mp4')
i=000000
print('FPS= ' + str(video.get(cv2.CAP_PROP_FPS)) + '\n')

while video.isOpened():
  	ret,frame = video.read()
  	if ret == False : break
  	
  	with open('times.txt', 'a') as the_file:
    		the_file.write(str(int(video.get(cv2.CAP_PROP_POS_MSEC)*1000000)) + ' ' + str(i).zfill(6) + '.png\n') #timestamp in nanosec
    		
  	
  	cv2.imwrite(str(i).zfill(6)+'.png',frame)
  	i+=1
