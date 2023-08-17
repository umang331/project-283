from controller import Robot
from controller import Motor
from controller import Altimeter
import math


class MyController(Robot):
    def __init__(self):
        super(MyController, self).__init__()
        self.timeStep = 32

        self.distanceSensor = self.getDevice("ds0")
        self.distanceSensor.enable(self.timeStep)

        self.accelerometer = self.getDevice("accelerometer")
        self.accelerometer.enable(self.timeStep)

        self.left_motor = self.getDevice("left wheel motor")
        self.right_motor = self.getDevice("right wheel motor")
        self.left_motor.setPosition(math.inf)
        self.right_motor.setPosition(math.inf)

        self.left_motor.setVelocity(0.5)
        self.right_motor.setVelocity(-0.5)
        self.direction_switch = True
        self.accValues = []

    def run(self):
        while self.step(self.timeStep) != -1:
            for i in range(3):
                self.accValues.append(self.accelerometer.getValues())

            self.accValues = []


controller = MyController()
controller.run()