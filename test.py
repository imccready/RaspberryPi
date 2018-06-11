from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template
from flask_socketio import SocketIO
import datetime




class MyClass:
    def __init__(self, start):
        print("class")
        self.test2 = start
        self.time = datetime.datetime.now() + datetime.timedelta(seconds = 10)
        self.state = False


def sensor(test):
    """ Function for test purposes. """
    if test.time <=  datetime.datetime.now(): 
        test.time = datetime.datetime.now() + datetime.timedelta(seconds = 10)
        print(str(test.time))
        test.state =  not test.state

    print (test.state)
    

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()   
    templateData = {
      'title' : 'HELLO!',
      'time': now
      }
    return render_template('main.html', **templateData)

    """obj.test2 = obj.test2 * 2
    return "value: " + str(obj.test2)"""
    
"""app.config['SECRET_KEY'] = 'secret!'"""
socketio = SocketIO(app)

if __name__ == "__main__":
    obj = MyClass(1)
    socketio.run(app)
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(sensor,'interval', seconds=5, id='my_job', args=[obj])
    sched.start()  
    app.run(host='0.0.0.0', port=91, use_reloader=False)
    