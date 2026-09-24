# RoadScanner

A computer vision project that detects potholes and speed breakers from
road images and videos.

Many expensive cars already come with advanced features like lane detection and driving assistance, but these features are often not available in smaller, more affordable cars. RoadScanner aims to build an affordable add-on system that can bring similar AI-based safety features to more vehicles.

## What I am building

The current version uses YOLOv8 to detect:

-   Potholes
-   Speed Breakers

The goal is to eventually run the model on a phone camera and detect
road problems in real time.

## Current Pipeline

``` text
Road Image / Video
        ↓
      YOLOv8
        ↓
Pothole / Speed Breaker
        ↓
Bounding Box + Confidence
```

## Dataset

I combined two road-defect datasets and created a unified dataset for
the two classes used in this project.

Final classes:

``` text
0 → pothole
1 → speed_breaker
```

The dataset itself is not included in this repository because of its
size.

## Model

Model: YOLOv8n

I used a pretrained YOLOv8 model and fine-tuned it on the road-defect
dataset.

Training settings used for the first version:

-   Epochs: 30
-   Image size: 640
-   Classes: 2

## Project Structure

``` text
RoadScanner/
├── Train/
│   └── train.py
├── Test/
│   ├── test.py
│   └── test_1.jpg
└── .gitignore
```

The trained model, datasets and training outputs are kept locally and
are not uploaded to this repository.

## What I did

### 1. Collected the data

I used two road-defect datasets containing road images and YOLO-format
labels.

### 2. Prepared the dataset

I combined the useful data from both datasets and kept only the two
classes I needed:

-   Pothole
-   Speed Breaker

### 3. Trained the model

I used a pretrained YOLOv8n model and fine-tuned it on the combined
dataset.

### 4. Tested the model

After training, I used the trained `best.pt` model on a new road image
that was not used for training.

The model successfully detected potholes and returned bounding boxes
with confidence scores.

## Next Steps

1.  Test on more unseen road images
2.  Run detection on road videos
3.  Run real-time detection using a webcam
4.  Connect the system to an Android camera
5.  Explore on-device Android inference

## Tech Used

-   Python
-   PyTorch
-   Ultralytics YOLOv8
-   Computer Vision
-   Git & GitHub

## Status

Work in progress

This is the first version of RoadScanner, and I am continuously improving the system by adding new capabilities and refining its hardware and software architecture.

I am working on this project with the goal of slowly developing it into an affordable add-on driving assistance device. 

The `V1` is a software-based system , and in `V2` will use an Android phone as the first actual device.

In `V3` , I plan to move toward dedicated hardware using an NVIDIA Jetson-like kit and add IMU sensors for more advanced road and driving assistance features.

This is just the first model, and I am improving it step by step as I learn and build.