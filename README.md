# Lesson Editor
This is a basic editor that can seperate and add sound from mp4/webm files. Note that seperated audio files get saved in mp3, merged video and audio files get saved in mp4 format.

This code uses os, pathlib, time, ctypes and moviepy modules.
os, pathlib, time and ctypes modules are a part of the python standart library and the moviepy module can be installed from pip using ```pip install moviepy```.

**************************************************

## Origin
So currently (Q2 21) all of my courses (10) are online. We, students, log in to univerity's distance education (uzaktan eğitim) and join *live* classes based on our sllyabus because uni keeps attendance.

After lecture is finished, its get uploaded to the system for students to rewatch it. I realized that i can download lectures with [Chrome extantion vGet](https://chrome.google.com/webstore/detail/vget-cast-dlna-controller/ekdjofnchpbfmnfbedalmbdlhbabiapi?hl=tr). Lecture have webcam and deskshare videos in mp4 or webm format. webcam has professors webcam, mic and deskshare has desktops screen record with sound (except mic). So instead of having two seperate videos where one is muted, i came up with the idea of editing these two videos to one. Couldn't find a program satisfy so i decided to make one instead.

## Some issues
Not every lecture has deskshare video. Apparently professors can upload a presentation insted of sharing screen so some lectures only have webcam video and i don think that i  can edit those in any way.

File size is a big issue, i am trying to keeps things as small as possible. I don't need 4K HDR lectures, a low quality 720p@24 video is more than enough.

**************************************************

## Program
The goal is to make a program that can extract the audio from webcam and add it to deskshare.
### Deciding on modules
One module to seperate audio from webcam video.

One module to add audio to deskshare video.

One module to take user input and do both seperating and adding audio.
Three modules in total. Yes i can technically make all of these modules in one file but like this i can use seperating and adding audio as a script when i need only those one of those two.
### Seperating audio from webcam video
Used moviepy to seperate audio and saving it in mp3 format is the webcam video file exists.
### Adding audio to deskshare video
Used again, moviepy to *set* (not add) audio to deskshare and export it as mp4
### Control + UI
In ```main.py``` i made four methods. First one takes user input for name of course and check if course exists in the list of courses that i am taking, second one does the same for week as an integer and checks if its pozitif and lower than seventeen (one semester is sixteen weeks long). With knowing these two program can know what lesson that user wants ( {course}H{week} H-->Hafta, Hafta means week in Turkish). Third method asks user to verify, fourth method starts the editing process and handles any errors like file not found.
