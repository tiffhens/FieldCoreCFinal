import raspi
import random
from flask import *

app = Flask(__name__)
raspi = raspi.Raspi()

response = ""
myList = ["Casa", "Comida", "Persona", "Deportes"]
myList2 = ["De donde eres?", "Cual es tu animal favorito? Porque?", "Que te gustas hacer?"]

# Index route
@app.route("/")

def index():
# Read the value of the sensor
    value = raspi.read_sensor()
    if value[0] == 1:
        response1 = myList[random.randint(0,3)]
    else:
        response1 = "Por favor, pulse el boton"
    if value[1] == 1:
        response2 = myList2[random.randint(0,2)]
    else:
        response2 = "Por favor, pulse el boton"    
# Render the index.html template passing the value of the sensor
    return render_template('index.html', sensor_value = [response1, response2])

# About route
@app.route("/about")
def about():
# Render the about.html template
  return render_template('about.html')

# Starts the app listening to port 5000 with debug mode
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
