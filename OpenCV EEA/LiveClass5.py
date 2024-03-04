import cv2
from djitellopy import Tello

tello =Tello()
tello.connect()


tello.send_command_with_return("Command")

tello.stream_on()

tello.send_command_with_return("takeoff")

tello.send_command_without_return("left 10")
