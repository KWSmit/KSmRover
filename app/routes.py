from flask import render_template, jsonify, request, Response
from app import app
from robot import JoyStickRobot
from camera import Camera


joystick_robot = JoyStickRobot()
platform_type = joystick_robot.platform_type

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', platform=platform_type)

@app.route('/about')
def about_page():
    return render_template('about.html', platform=platform_type)

@app.route('/touch_page')
def touch_page():
    return render_template('touch_page.html', platform=platform_type)

@app.route('/camera_page')
def camera_page():
    return render_template('camera_page.html', platform=platform_type)

@app.route('/touch_circle', methods=['POST'])
def touch_circle():
    x = int(request.form['x_touch'])
    y = int(request.form['y_touch'])
    joystick_robot.robot.on(x, y, max_speed=100.0, radius=500.0)
    position = '(' + str(x) + ',' + str(y) + ')'
    return jsonify({'position': position})

@app.route('/touch_video', methods=['POST'])
def touch_video():
    x = int(request.form['x_touch'])
    y = int(request.form['y_touch'])
    joystick_robot.robot.on(x, y, max_speed=100.0, radius=500.0)
    position = '(' + str(x) + ',' + str(y) + ')'
    return jsonify({'position': position})

@app.route('/motor_stop', methods=['POST'])
def motor_stop():
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
