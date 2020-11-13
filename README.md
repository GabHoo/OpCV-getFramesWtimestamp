# OpCV-getFramesWtimestamp

Quick script for extracting grey-scale frames out of a video while creating the Timestamp.txt. 

The timestamp.txt fill be created in the same folder with the following format: [time(seconds) frame]
You can also just get the file with frame names and no times by commenting the main write_in_file line and uncommenting the one below.

You can change the format of the output frames file to jpg just by changing the appended string from png to jpg.

You can also get the timestamp in milli micro o just seconds by changing the multiplyng factor.

Also you can get original coloured frames by commenting the gray-scale line
