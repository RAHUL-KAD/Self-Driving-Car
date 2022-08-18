# 3D object detection notes

2d Object detection algorithm has 4 parameters as input (x, y, w, h) but 3D object detection has 9 paramters (x, y, w, h, l, r, p, y).
Lets explore what those are we all know x, y, w, and h. 
1. l is length. What is the total length of the object that we want to detect
2. r is Roll: its left to right motion
3. p is pitch: its back and forth motion
4. y is yaw: its up and down motion

In Most of the cases we dont use r and p beacuse our car is or any object is on the rode or it is not moving that way we have less paramerts to give to 3d model.

![roll pitch yaw](/3d-object-detection/images/roll-pitch-yaw.png)

