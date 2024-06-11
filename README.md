# FACE-RECOGNITION-BASED-ATTENDANCE

                                                               ABSTRACT

  	Face recognition is among the most productive image processing applications and has a pivotal role in the technical field. Recognition of the human face is an active issue for authentication purposes specifically in the context of attendance of students. Attendance system using face recognition is a procedure of recognizing students by using face biostatistics based on the high definition monitoring and other computer technologies. The development of this system is aimed to accomplish digitization of the traditional system of taking attendance by calling names and maintaining pen-paper records. Present strategies for taking attendance are tedious and time-consuming. Attendance records can be easily manipulated by manual recording. The traditional process of making attendance and present biometric systems are vulnerable to proxies. This paper is therefore proposed to tackle all these problems. The proposed system makes the use of Haar classifiers, KNN, CNN, SVM, Generative adversarial networks, and Gabor filters. After face recognition attendance reports will be generated and stored in excel format. The system is tested under various conditions like illumination, head movements, the variation of distance between the student and cameras. After vigorous testing overall complexity and accuracy are calculated. The Proposed system proved to be an efficient and robust device for taking attendance in a classroom without any time consumption and manual work. The system developed is cost-efficient and need less installation.
 The modules of this project are divided as follows:
    • main
    • face  read
    • train images
    • recognizer
    • modify or delete
    • show attendance


                                                                  Introduction:
     
Traditional method of attendance marking is a tedious task in many schools and colleges. It is also an extra burden to the faculties who should mark attendance by manually calling the names of students which might take about 5 minutes of entire session. This is time consuming. There are some chances of proxy  attendance.  Therefore,  many  institutes  started deploying  many  other  techniques  for  recording  attendance 
like  use of  Radio Frequency  Identification (RFID) , iris recognition , fingerprint recognition, and so on. However, these  systems  are queue  based which  might  consume  more time and are intrusive in nature.  Face  recognition  has  set an  important  biometric  feature, which  can  be  easily  acquirable  and  is  non-intrusive.  Face recognition based systems are relatively oblivious to various facial  expression.  Face  recognition  system  consists  of  two categories:  verification  and  face  identification.  Face verification  is  an  1:1  matching  process,  it  compares  face image against the template face images and whereas is an 1:N  problems that compares a query face images .  The purpose of this system is to build a attendance system which is based on face  recognition techniques. Here face of an  individual  will  be  considered  for  marking  attendance. Nowadays,  face recognition  is gaining  more popularity  and has been widely used. In this  paper, we  proposed a  system which detects the faces of students from live streaming video of classroom and attendance will  be marked  if the detected face is found in the database.This new system will consume less time than compared to traditional methods.  

                                                                     LBPH Algorithm:
	Local Binary Pattern (LBP) is a simple yet very efficient texture operator which labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number.
It was first described in 1994 (LBP) and has since been found to be a powerful feature for texture classification. It has further been determined that when LBP is combined with histograms of oriented gradients (HOG) descriptor, it improves the detection performance considerably on some datasets.
Using the LBP combined with histograms we can represent the face images with a simple data vector.
As LBP is a visual descriptor it can also be used for face recognition tasks, as can be seen in the following step-by-step explanation.
Now that we know a little more about face recognition and the LBPH, let’s go further and see the steps of the algorithm:

    1. Parameters: the LBPH uses 4 parameters:
    • Radius: the radius is used to build the circular local binary pattern and represents the radius around the central pixel. It is usually set to 1.
    • Neighbors: the number of sample points to build the circular local binary pattern. Keep in mind: the more sample points you include, the higher the computational cost. It is usually set to 8.
    • Grid X: the number of cells in the horizontal direction. The more cells, the finer the grid, the higher the dimensionality of the resulting feature vector. It is usually set to 8.
    • Grid Y: the number of cells in the vertical direction. The more cells, the finer the grid, the higher the dimensionality of the resulting feature vector. It is usually set to 8.
Don’t worry about the parameters right now, you will understand them after reading the next steps.

2. Training the Algorithm: First, we need to train the algorithm. To do so, we need to use a dataset with the facial images of the people we want to recognize. We need to also set an ID (it may be a number or the name of the person) for each image, so the algorithm will use this information to recognize an input image and give you an output. Images of the same person must have the same ID. With the training set already constructed, let’s see the LBPH computational steps.

3. Applying the LBP operation: The first computational step of the LBPH is to create an intermediate image that describes the original image in a better way, by highlighting the facial characteristics. To do so, the algorithm uses a concept of a sliding window, based on the parameters radius and neighbors.
The image below shows this procedure:

Based on the image above, let’s break it into several small steps so we can understand it easily:
    • Suppose we have a facial image in grayscale.
    • We can get part of this image as a window of 3x3 pixels.
    • It can also be represented as a 3x3 matrix containing the intensity of each pixel (0~255).
    • Then, we need to take the central value of the matrix to be used as the threshold.
    • This value will be used to define the new values from the 8 neighbors.
    • For each neighbor of the central value (threshold), we set a new binary value. We set 1 for values equal or higher than the threshold and 0 for values lower than the threshold.
    • Now, the matrix will contain only binary values (ignoring the central value). We need to concatenate each binary value from each position from the matrix line by line into a new binary value (e.g. 10001101). Note: some authors use other approaches to concatenate the binary values (e.g. clockwise direction), but the final result will be the same.
    • Then, we convert this binary value to a decimal value and set it to the central value of the matrix, which is actually a pixel from the original image.
    • At the end of this procedure (LBP procedure), we have a new image which represents better the characteristics of the original image.

4. Extracting the Histograms: Now, using the image generated in the last step, we can use the Grid X and Grid Y parameters to divide the image into multiple grids, as can be seen in the following image:

Based on the image above, we can extract the histogram of each region as follows:
    • As we have an image in grayscale, each histogram (from each grid) will contain only 256 positions (0~255) representing the occurrences of each pixel intensity.
    • Then, we need to concatenate each histogram to create a new and bigger histogram. Supposing we have 8x8 grids, we will have 8x8x256=16.384 positions in the final histogram. The final histogram represents the characteristics of the image original image.
The LBPH algorithm is pretty much it.

5. Performing the face recognition: In this step, the algorithm is already trained. Each histogram created is used to represent each image from the training dataset. So, given an input image, we perform the steps again for this new image and creates a histogram which represents the image.
    • So to find the image that matches the input image we just need to compare two histograms and return the image with the closest histogram.
    • We can use various approaches to compare the histograms (calculate the distance between two histograms), for example: euclidean distance, chi-square, absolute value, etc. In this example, we can use the Euclidean distance (which is quite known) based on the following formula:

                           

    • So the algorithm output is the ID from the image with the closest histogram. The algorithm should also return the calculated distance, which can be used as a ‘confidence’ measurement. Note: don’t be fooled about the ‘confidence’ name, as lower confidences are better because it means the distance between the two histograms is closer.
    • We can then use a threshold and the ‘confidence’ to automatically estimate if the algorithm has correctly recognized the image. We can assume that the algorithm has successfully recognized if the confidence is lower than the threshold defined.

Conclusions
    • LBPH is one of the easiest face recognition algorithms.
    • It can represent local features in the images.
    • It is possible to get great results (mainly in a controlled environment).
    • It is robust against monotonic gray scale transformations.
    • It is provided by the OpenCV library (Open Source Computer Vision Library).

                                                                  
