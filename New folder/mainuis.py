from flask import Flask, render_template, jsonify,request
import random
app = Flask(__name__)
destination = ""
i=0
@app.route('/')
def home():
    return render_template('mainui.html')

@app.route('/data')
def data():
    global angle,i
    arr=list(range(0,10000,4))
    dist=arr[i]
    i+=1
    angle = 20
    speed = random.randint(0,30)
    car_state= "MOVING" if speed else "STATIONARY"
    return jsonify({'speed': speed,'destination':destination,'car_state':car_state,'angle':angle,'dist':dist})

@app.route('/update_destination', methods=['POST'])
def update_destination():
    global destination
    data =  request.get_json()
    destination = data.get('destination') 
    response = {'destination': destination}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)




       