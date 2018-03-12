Run this command in your Rpi
1. sudo apt-get install build-essential libssl-dev libffi-dev python-dev
2. sudo pip install azure-storage-blob 
3. sudo pip install watchdog ( for uploading image on capture (ImgUploadToAzureOnCapture))



READ ME FOR ImgUploadToAzureOnCapture:

1.install motion lib in the pi -- sudo apt-get install motion

2.For instructions how to setup motion lib = https://circuitdigest.com/microcontroller-projects/raspberry-pi-surveillance-camera

  do necessory changes in the motion lib 

  sudo nano /etc/motion/motion.conf


3.After setuping the motion lib run the code uploader.py 

  - install before running the code

    1. sudo apt-get install build-essential libssl-dev libffi-dev python-dev

    2. sudo pip install azure-storage-blob 

    3. sudo pip install watchdog

4.change directory where to search the pictures in credentials.py

5.run uploader.py

  run motion service (sudo service motion start  )

  when ever a file(jpg,png) is created it will send to cloud and move to back up folder


6.This code send only one pic to cloud so we will make cronjob to restart service to get best picture and send it to cloud

7. type sudo cronjob -e in terminal

 at the end of the file add these two tines


 */1 * * * * sudo service motion restart

 */1,5 * * * * sudo python /home/pi/ImgUploadToAzureOnCapture/uploader.py &

  These cronjob will do for every one minute service will restart so that best motion picture is taken and it is send to cloud.

  As our code send only one pic we are runing code for ever 1.5 mintue so it won't get problem to send picture to cloud


