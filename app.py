from flask import Flask, render_template
import csv    

f = open("Forbes2000.csv", 'rb') 
try:
    reader = csv.reader(f) 
    for row in reader:   
        print row  
finally:
    f.close()      

app = Flask(__name__)

@app.route("/")
def forbes():
    return render_template("forbes.html")
