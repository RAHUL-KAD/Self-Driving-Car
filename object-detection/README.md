# Object Detection

Object detection is one of the most important method is self driving car. To detect an objects we use object detectors like YOLO family, Faster RCNN, Fast RCNN, Singal shot detection(SSD). In this repo I used [YOLOv5](https://github.com/ultralytics/yolov5).

## YOLO (You only look once)
[Paper](https://arxiv.org/pdf/1803.01534v4.pdf)

You only look once (YOLO) is one of the most popular model architectures and algorithms for object detection. Usually, the first concept found on a Google search for algorithms on object detection is the YOLO architecture.

Working process of YOLO:

![YOLO architecture image](/object-detection/images/YOLO-object-detection-algorithm.webp)

Advantages:

1. The computation and processing speed of YOLO is quite high, especially in real-time compared to most of the other training methods and object detection algorithms.

2. Apart from the fast computing speed, the YOLO algorithm also manages to provide an overall high accuracy with the reduction of background errors seen in other methods.

3. The architecture of YOLO allows the model to learn and develop an understanding of numerous objects more efficiently.

Disadvantages:
1. Failure to detect smaller objects in an image or video because of the lower recall rate.

2. Cant’t detect two objects that are extremely close to each other due to the limitations of bounding boxes.

## How to use this repo
You can use this repo to build your own object detection model.

**Steps:**

1. Download Object detection using YOLOv5.ipynb file.
2. Upload it to google drive to use COlab and free GPU.
3. Follow the instructions from the .ipynb file and train your model.
4. Got an error, google it or create an issue with proper explanation and screenshots.
5. Happy coding