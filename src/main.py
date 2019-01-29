#!/usr/bin/env python
import cv2
import os
import sys
import numpy as np
from LineDetection import LineDetection

if __name__ == '__main__':
    '''
    if len(sys.argv) < 2:
        print('Image name must be added. Format must be .png')
        exit()
    
    file_name = str(sys.argv[1] + '.png')
    '''
    projectPath = os.path.abspath(os.path.pardir)
    folderPath = os.path.join(projectPath, 'test_images')
    destPath = os.path.join(projectPath, 'result_images')
    print(destPath)

    lineDetection = LineDetection()
    for root, dirs, files in os.walk(folderPath):
        for file in files:
            if file.endswith(".png"):
                filePath = os.path.join(root, file)

                img = cv2.imread(filePath)

                image_size = img.shape

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                greenLower = (29, 86, 6)
                greenUpper = (64, 255, 255)
                edges = cv2.Canny(gray, 30, 50, apertureSize=3)
                minLineLength = 10
                maxLineGap = 10

                try:
                    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                    #greenLower = (29, 86, 6)
                    greenLower = (30, 86, 6)
                    greenUpper = (85, 240, 230)
                    #greenUpper = (64, 255, 255)
                    mask = cv2.inRange(hsv, greenLower, greenUpper)
                except cv2.error:
                    print(img)
                    print("Image doesn't exists")
                newName = 'lineDetected' + file
                destination = os.path.join(destPath, newName)
                cv2.imwrite(destination , mask)

                lineDetection.analyse(destination)

                img = cv2.imread(filePath)
                img = cv2.resize(img, (640, 480))
                img = cv2.blur(img, (10, 10))
                cv2.waitKey(0)


