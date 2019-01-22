# KSmRover

KSmRover is a remote controlled robot which can be used on a
LEGO Mindstorms EV3 brick or mindsensors.com PiStorms. The latter
can be used with a picamera to view live videofeed where it's moving.

The program runs on the ev3dev operating system, so be sure it's
running on the EV3-brick or Raspberry Pi. More information about
ev3dev can be found on: [www.ev3dev.org](https://www.ev3dev.org/).

The program is a Flask application: it runs a webserver on the robot
so it can be controlled from a mobile device with touchscreen. On the robot
you start the application by running

```bash
./start_KSmRover.sh
```

Make sure this script is executable. If not, run

```bash
chmod a+x start_KSmROver.sh
```

When the webserver is started, open the webpage on your mobile device

```bash
http://<ip-address-robot>:5000/
```

You will see the homepage of the robot. On the EV3-brick you can open
the `touch`-page to use the interface. The green dot works like a joystick,
you can move your finger around. At the center the robot will stop,
when you move your finger to the top, the robot will move formward.
Or when you move your finger to the right, it will move that way.
You can adjust the driving speed by varying the distance between
your finger and the center of the dot.

When using the PiStorms with Raspberry Pi, you got the same touch
userinterface. But there is more: on the `camera`-page you see a live
video-feed (when a picamera is attached to the pi). This video-feed
contains the same touch steering capabilities. So by touching the
video and point your finger into the direction you want to go, the
robot will drive in that direction.

You'll find more information (including a video) on my
[website](https://kwsmit.github.io).

Have fun!

Kees Smit
