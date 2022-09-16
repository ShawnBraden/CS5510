import math


class motion:
    def __init__(self, commands, width, length):
        self.__possitionsPredicted = []
        self.__velocityPredicted = []
        self.__commands = commands
        self.__width = width
        self.__length = length
        self.__width_i = 1 / width
        self.__widthAvg = width / 2

    def motionSkidSteerPredicted(self, deltaT, V_left, V_right, x, y, theata):
        theata_Now = theata + (self.__width_i * (V_right - V_left) * deltaT)
        theata_diff = theata_Now - theata
        x_now = x - (0.5 * (V_right + V_left) * (math.sin(theata_Now)) * deltaT)
        x_diff = x_now - x
        y_now = y + (0.5 * (V_right + V_left) * (math.cos(theata_Now)) * deltaT)
        y_diff = y_now - y
        return [x_now, y_now, theata_Now], [x_diff, y_diff, theata_diff]

    # Not needed for hw but needed for midterm :)
    def motionSkidSteerPredictedCorrected(self, V_left, V_right, x, y):
        try :
            r = self.__widthAvg * ((V_right + V_left) / (V_right - V_left))
        except :
            return [x, y]
        c = 2 * math.pi * r
        theataError = 360 * (y / c)
        yCorrected = math.degrees(math.sin(theataError)) * r
        xCorrected = math.degrees(math.cos(theataError)) * r
        return [yCorrected, xCorrected]

    def calculateMotion(self):
        currentx = 0
        currenty = 0
        currentTheata = 0
        for vector in self.__commands:
            self.__possitionsPredicted.append(self.motionSkidSteerPredicted(vector[0], vector[1], vector[2], currentx, currenty, currentTheata))
            self.__possitionsCorrected.append(self.motionSkidSteerPredictedCorrected(vector[1], vector[2], self.__possitionsPredicted[-1][0], self.__possitionsPredicted[-1][1]))
            currentx = self.__possitionsCorrected[-1][0]
            currenty = self.__possitionsCorrected[-1][1]
            currentTheata = self.__possitionsPredicted[-1][2]

    # Using this method for the hw
    def calculateMotionNotCorrected(self, dt):
        currentx = 0
        currenty = 0
        currentTheata = 0
        for vector in self.__commands:
            i = dt
            while i <= vector[0]:
                var = self.motionSkidSteerPredicted(dt, vector[1], vector[2], currentx, currenty, currentTheata)
                self.__possitionsPredicted.append(var[0])
                self.__velocityPredicted.append(var[1])
                currentx = self.__possitionsPredicted[-1][0]
                currenty = self.__possitionsPredicted[-1][1]
                currentTheata = self.__possitionsPredicted[-1][2]
                i += dt

    def getPossitionsPredicted(self):
        return self.__possitionsPredicted

    def getVelocityPredicted(self):
        return self.__velocityPredicted
        