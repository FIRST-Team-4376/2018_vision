#/bin/bash
v4l2-ctl --set-ctrl=exposure_auto=1
v4l2-ctl --set-ctrl=exposure_absolute=5
python /home/pi/2018_vision/vision_main.py
