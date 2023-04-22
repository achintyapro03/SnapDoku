from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np


class numberReader():
    def __init__(self, image):
        np.set_printoptions(suppress=True)
        self.model = load_model("keras_model.h5", compile=False)
        self.class_names = open("labels.txt", "r").readlines()
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        self.cells = [["" for k in range(9)] for _ in range(9)]
        self.numbs = [[0 for k in range(9)] for _ in range(9)]
        self.image = image.resize((900, 900))

    def processPic(self):
        for i in range(9):
            for j in range(9):
                x = self.image.crop((j * 100 + 10, i * 100 + 10, (j + 1) * 100 - 10, (i + 1) * 100 - 10))
                path = "cells/" + str(i) + str(j) + ".png"
                numImg = np.asarray(x)
                myArr = np.zeros((80, 80)).astype(np.uint8)
                for p in range(80):
                    for q in range(80):
                        if numImg[p][q] >= 220:
                            myArr[p][q] = 255
                img = Image.fromarray(myArr, mode='L')
                self.cells[i][j] = path
                img.save(path, quality=100)

    def picToNum(self, path):
        image = Image.open(path).convert("RGB")

        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

        image_array = np.asarray(image)

        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        self.data[0] = normalized_image_array

        prediction = self.model.predict(self.data)
        index = np.argmax(prediction)
        class_name = self.class_names[index]
        return int(class_name[2])

    def printArr(self, li):
        for i in li:
            for j in i:
                print(j, end=" ")
            print()

    def run(self):
        self.processPic()
        for i in range(9):
            for j in range(9):
                self.numbs[i][j] = self.picToNum(self.cells[i][j])

    def getNumbs(self):
        return self.numbs

# image1 = Image.open('Sudoku_matrix.png')
# image1 = image1.convert("L")
# 
# cells = [["" for k in range(9)] for _ in range(9)]
# numbs = [[0 for k in range(9)] for _ in range(9)]
# 
# image1 = image1.resize((900, 900))
