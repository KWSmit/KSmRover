from flask import render_template, jsonify, request, Response
from app import app
from robot import JoyStickRobot
from camera import Camera
import math


joystick_robot = JoyStickRobot()
platform_type = joystick_robot.platform_type

@app.route('/')
@app.route('/index')
def index():
    """ Show the homepage."""
    return render_template('index.html', platform=platform_type)

@app.route('/about')
def about_page():
    """ Show the About page."""
    return render_template('about.html', platform=platform_type)

@app.route('/touch_page')
def touch_page():
    """ Show the webpage with touch control."""
    return render_template('touch_page.html', platform=platform_type)

@app.route('/camera_page')
def camera_page():
    """ Show the webpage with live videofeed and touch control."""
    return render_template('camera_page.html', platform=platform_type)

@app.route('/touch_circle', methods=['POST'])
def touch_circle():
    """ Handle received data from the webpage with touch control."""
    x = int(request.form['x_touch'])
    y = int(request.form['y_touch'])
    joystick_robot.robot.on(x, y, max_speed=100.0, radius=500.0)
    position = '(' + str(x) + ',' + str(y) + ')'
    return jsonify({'position': position})

@app.route('/touch_video', methods=['POST'])
def touch_video():
    """ Handle received data from webpage with videofeed and touch control."""
    x = float(request.form['x_touch'])
    y = float(request.form['y_touch'])
    # Scale x and y to make the robot react less sensitive
    x = math.floor(x/3)
    y = math.floor(y/3)
    joystick_robot.robot.on(x, y, max_speed=100.0, radius=300.0)
    position = '(' + str(x) + ',' + str(y) + ')'
    return jsonify({'position': position})

@app.route('/motor_stop', methods=['POST'])
def motor_stop():
    """ Stop all motors."""
    motor_action = request.form['motor_action']
    if motor_action == 'stop':
        joystick_robot.robot.off()
        speed = '(0,0)'
    else:
        speed = 'ERROR motor_stop!'
    return jsonify({'text': speed})

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
