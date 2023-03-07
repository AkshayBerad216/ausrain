from flask import Flask, request,render_template
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

model = pickle.load(open('log_model.pkl', 'rb'))
col_list = pickle.load(open('col_list.obj', 'rb'))


app = Flask(__name__)


@app.route('/')
def man():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    MinTemp = float(request.form['MinTemp'])
    MaxTemp = float(request.form['MaxTemp'])
    Rainfall = float(request.form['Rainfall'])
    Evaporation = float(request.form['Evaporation'])
    Sunshine = float(request.form.get('Sunshine'))
    WindGustSpeed = float(request.form.get('WindGustSpeed'))
    WindDir9am = request.form.get('WindDir9am')
    WindDir3pm =request.form.get('WindDir3pm')
    WindSpeed9am =float(request.form.get('WindSpeed9am'))
    WindSpeed3pm =float(request.form.get('WindSpeed3pm'))
    Humidity9am =float(request.form.get('Humidity9am'))
    Humidity3pm = float(request.form.get('Humidity3pm'))
    Pressure9am =float(request.form.get('Pressure9am'))
    Pressure3pm =float(request.form.get('Pressure3pm'))
    Cloud9am =float(request.form.get('Cloud9am'))
    Cloud3pm =float(request.form.get('Cloud3pm'))
    Temp9am =float(request.form.get('Temp9am'))
    Temp3pm =float(request.form.get('Temp3pm'))
    RainToday = request.form.get('RainToday')
    Year = float(request.form.get('Year'))
    Month = float(request.form.get('Month'))
    Day = float(request.form.get('Day'))
    Location = request.form.get('Location')
    WindGustDir = request.form.get('WindGustDir')


    print('MinTemp == ',MinTemp)
    print(type(MinTemp))
    print('MaxTemp == ',MaxTemp)
    print("Rainfall == ",Rainfall)
    print("Evaporation == ",Evaporation)
    print("Location == ",Location)
    print("WindGustDir == ",WindGustDir)

    if WindDir9am ==  "W":
        WindDir9am = 0
    elif WindDir9am ==  "NNW":
        WindDir9am = 1
    elif WindDir9am ==  "SE":
        WindDir9am = 2
    elif WindDir9am ==  "ENE":
        WindDir9am = 3
    elif WindDir9am ==   "SW":
        WindDir9am = 4
    elif WindDir9am ==  "SSE":
        WindDir9am = 5
    elif WindDir9am ==   "S":
        WindDir9am =6
    elif WindDir9am ==  "NE":
        WindDir9am = 7
    elif WindDir9am ==  "N":
        WindDir9am = 8
    elif WindDir9am ==  "SSW":
        WindDir9am = 9
    elif WindDir9am ==  "WSW":
        WindDir9am = 10
    elif WindDir9am ==  "ESE":
        WindDir9am = 11
    elif WindDir9am ==  "E":
        WindDir9am = 12
    elif WindDir9am ==  "NW":
        WindDir9am = 13
    elif WindDir9am ==  "WNW":
        WindDir9am = 14
    elif WindDir9am ==  "NNE":
        WindDir9am = 15


    if WindDir3pm ==  "WNW":
        WindDir3pm = 0
    elif WindDir3pm ==   "WSW":
        WindDir3pm =1
    elif WindDir3pm ==  "E":
        WindDir3pm = 2
    elif WindDir3pm ==  "NW":
        WindDir3pm = 3
    elif WindDir3pm ==  "W":
        WindDir3pm = 4
    elif WindDir3pm ==  "SSE":
        WindDir3pm = 5
    elif WindDir3pm ==  "ESE":
        WindDir3pm = 6
    elif WindDir3pm ==  "ENE":
        WindDir3pm = 7
    elif WindDir3pm ==  "NNW":
        WindDir3pm = 8
    elif WindDir3pm ==  "SSW":
        WindDir3pm = 9
    elif WindDir3pm ==  "SW":
        WindDir3pm = 10
    elif WindDir3pm ==   "SE":
        WindDir3pm = 11
    elif WindDir3pm ==  "N":
        WindDir3pm = 12
    elif WindDir3pm ==  "S":
        WindDir3pm = 13
    elif WindDir3pm ==   "NNE":
        WindDir3pm = 14
    elif WindDir3pm ==  "NE":
        WindDir3pm = 15

    
    if RainToday == 'No':
        RainToday = 0
    else:
        RainToday = 1



    arr = np.zeros(col_list.shape[0])
    print(arr)

    arr[0] = MinTemp
    arr[1] = MaxTemp
    arr[2] = Rainfall
    arr[3] = Evaporation
    arr[4] = Sunshine
    arr[5] = WindGustSpeed
    arr[6] = WindDir9am
    arr[7] = WindDir3pm
    arr[8] = WindSpeed9am
    arr[9] = WindSpeed3pm
    arr[10] = Humidity9am
    arr[11] = Humidity3pm
    arr[12] = Pressure9am
    arr[13] = Pressure3pm
    arr[14] = Cloud9am
    arr[15] = Cloud3pm
    arr[16] = Temp9am
    arr[17] = Temp3pm
    arr[18] = RainToday
    arr[19] = Year
    arr[20] = Month
    arr[21] = Day
   
    index1 = np.where(col_list==Location)[0][0]
    print(index1)

    index2 = np.where(col_list==WindGustDir)[0][0]
    print(index2)

    
    arr[index1] = 1
    arr[index2] = 1

    print(MinTemp)
    print(type(MinTemp))
    print(Location)
    print(col_list)

    print(arr)
   
    prediction = model.predict([arr])
    print("prediction : ",prediction[0])
    if prediction[0] == 0:
        print("No, rain tomorrow....You can do your work")
    else :
        print("Yes, there is rain tomorrow ....Enjoy with hot coffee and snacks")
    

    return render_template('after.html',data=prediction)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)   
