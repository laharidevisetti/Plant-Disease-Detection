from flask import Flask, redirect, url_for, request, render_template
import numpy
from PIL import ImageTk, Image
import tensorflow as tf
from tensorflow.keras.models import load_model

model = load_model(r"C:/Users/hp/Desktop/Project/Project1.h5")
app = Flask(__name__)

classes = { 0:'Healthy',
            1:'Bacterial', 
            2:'Virus', 
            3:'Lateblight', 
            }
@app.route('/BacteriaRemedies')
def BacteriaRemedies():
    return render_template("BacteriaRemedies.html")

@app.route('/VirusRemedies')
def VirusRemedies():
    return render_template("VirusRemedies.html")

@app.route('/LateBlightRemedies')
def LateBlightRemedies():
    return render_template("LateBlightRemedies.html")

@app.route('/Selection')
def Selection():
    return render_template("Selection.html")

@app.route('/Result')
def Result():
    return render_template("Result.html")

@app.route('/Classify')
def Classify():
    return render_template("login.html")

@app.route('/Remedies')
def Remedies():
    return render_template("Remedies.html")

@app.route('/Algorithms')
def Algorithms():
    return render_template("Algorithms.html")

@app.route('/Data')
def Data():
    return render_template("Data.html")
@app.route('/Healthy')
def Healthy():
    return render_template("Healthy.html")
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      TRAIN_DIR = 'C:/Users/hp/Downloads/PlantDiseaseDetection-master/PlantDiseaseDetection-master/train/train/'
      img = (TRAIN_DIR) + ( request.form['img'])
      print(img)
      image = Image.open(img)
      image = image.resize((50,50))
      image = numpy.expand_dims(image, axis=0)
      image = numpy.array(image) 
      #print(image.shape)
      #print( model.predict_classes([image]))
      pred = model.predict_classes([image])[0]
      print("Label = " + str(pred))
     # classify.result = pred
      sign = classes[pred]
      print(sign)
      if pred == 0:
            return render_template("Healthy.html")
      elif pred == 1:
            return render_template("Bacterial.html", result = sign)
      elif pred == 2:
           return render_template("Viral.html", result = sign)
      else:
           return render_template("LateBlight.html", result = sign)
   

@app.route('/')
def Entry():
    return render_template("Entry.html")

if __name__ == '__main__':
    app.run()