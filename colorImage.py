'''         Image processing and computer vision
                  Pedro Elí Ruiz Zárate
               Electronic engineering student
              Pontificia Universidad Javeriana
                      Bogotá - 2020
'''
import numpy #import numpy library
import cv2 #import openCV library

class colorImage: #create the class

    def __init__(self, route=None): #Initialize the class
        if route is None: #If the user does not enter the path, one is left by default
            self.route='C:/Users/pedro.ruiz/Documents/GitHub/colorImage/lena.png' #Default path
        else:
            self.route = route
        self.image = cv2.imread(self.route) #Save the image in slef


    def displayProperties(self): #displayProperties method
        alto, ancho, comp = self.image.shape #Save image properties
        print('The size of the image is ',alto, 'x', ancho,'.') #Show properties

    def makeGray(self): #makeGray method
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) #Convert color image to grayscale
        cv2.imshow('GRAY', gray) #Show grayscale image
        cv2.waitKey(0) #Use waitKey(0) to prevent the program from stopping

    def colorizeRGB(self, comp=None): #colorizeRGB method
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)#Convert color image to grayscale
        if comp is None: #If the user does not enter the color, red is left by default
            self.comp = 'red'
        else:
            self.comp = comp

        if self.comp == 'red': #Show red component of image
            image_red = numpy.copy(self.image) #Create a copy of image
            image_red[:,:,0] = 0 #Set B component to zeros
            image_red[:,:,1] = 0 #Set G component to zeros
            cv2.imshow('RED_Comp', image_red) #Sow modified image
            cv2.waitKey(0)#Use waitKey(0) to prevent the program from stopping
        elif self.comp == 'green': #Show green component of image
            image_green = numpy.copy(self.image) #Create a copy of image
            image_green[:,:,0] = 0 #Set B component to zeros
            image_green[:,:,2] = 0 #Set R component to zeros
            cv2.imshow('GREEN_Comp', image_green) #Sow modified image
            cv2.waitKey(0)#Use waitKey(0) to prevent the program from stopping
        elif self.comp == 'blue': #Show blue component of image
            image_blue = numpy.copy(self.image) #Create a copy of image
            image_blue[:,:,1] = 0 #Set G component to zeros
            image_blue[:,:,2] = 0 #Set R component to zeros
            cv2.imshow('BLUE_Comp', image_blue) #Sow modified image
            cv2.waitKey(0)#Use waitKey(0) to prevent the program from stopping
        else:
            print('None of the entered values is valid') #User does not enter a valid value

    def makeHue(self): #makeHue method
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV) #Convert BGR image to HSV image
        hsv[:,:,1]=255 #Set S component to 255
        hsv[:,:,2]=255 #Set V component to 255
        hue = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR) #Convert HSV image to BGR image
        cv2.imshow('HUE', hue) #Sow modified image
        cv2.waitKey(0)#Use waitKey(0) to prevent the program from stopping