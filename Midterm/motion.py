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
        self.__length_i = 1 / length

    def getCircleXPos(r,theta):
        return r * math.cos(theta)

    def getCircleYPos(r,theta):
        return r * math.sin(theta)

    def getCircleXYPos(r, theta):
        return [motion.getCircleXPos(r, theta), motion.getCircleYPos(r, theta)]
    
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

    def motionAckermanPredicted(self, deltaT, vRear, alpha, x, y, theata):
        theata_Now = theata + (self.__length_i * vRear *  deltaT * math.tan(alpha))
        theata_diff = theata_Now - theata
        x_now = x - (vRear * (math.sin(theata_Now)) * deltaT)
        x_diff = x_now - x
        y_now = y + (vRear * (math.cos(theata_Now)) * deltaT)
        y_diff = y_now - y
        return [x_now, y_now, theata_Now], [x_diff, y_diff, theata_diff]

    def forwardMotionAckermanPredicted(self, deltaT, vRear, alpha, x, y, theta):
        x_now = x - (vRear * (math.sin(theta * .92)) * deltaT)
        x_diff = x_now - x
        y_now = y + (vRear * (math.cos(theta * .92)) * deltaT)
        y_diff = y_now - y
        theata_Now = theta + (self.__length_i * vRear *  deltaT * math.tan(alpha))
        theata_diff = theata_Now - theta
        return [x_now, y_now, theata_Now], [x_diff, y_diff, theata_diff]

    def calculateMotionAckerman(self, dt):
        currentx = 0
        currenty = 0
        currentTheata = 0
        for vector in self.__commands:
            i = dt
            while i <= vector[0]:
                var = self.motionAckermanPredicted(dt, vector[1], vector[2], currentx, currenty, currentTheata)
                self.__possitionsPredicted.append(var[0])
                self.__velocityPredicted.append(var[1])
                currentx = self.__possitionsPredicted[-1][0]
                currenty = self.__possitionsPredicted[-1][1]
                currentTheata = self.__possitionsPredicted[-1][2]
                i += dt

    def calculateForwardMotionAckerman(self, dt):
        currentx = 2.5
        currenty = 0
        currentTheata = 0
        for vector in self.__commands:
            i = dt
            self.__possitionsPredicted.append([currentx, currenty, currentTheata])
            self.__velocityPredicted.append([0, 0, 0])

            while i <= vector[0]:
                var = self.forwardMotionAckermanPredicted(dt, vector[1], vector[2], currentx, currenty, currentTheata)
                self.__possitionsPredicted.append(var[0])
                self.__velocityPredicted.append(var[1])
                currentx = self.__possitionsPredicted[-1][0]
                currenty = self.__possitionsPredicted[-1][1]
                currentTheata = self.__possitionsPredicted[-1][2]
                i += dt

    def calculateForwardMotionAckermanSlip(self, dt):
        currentx = 2.5
        currenty = 0
        currentTheata = 0
        for vector in self.__commands:
            i = dt
            self.__possitionsPredicted.append([currentx, currenty, currentTheata])
            self.__velocityPredicted.append([0, 0, 0])

            while i <= vector[0]:
                var = self.forwardMotionAckermanPredicted(dt, vector[1], vector[2], currentx, currenty, currentTheata)
                self.__possitionsPredicted.append(var[0])
                self.__velocityPredicted.append(var[1])
                currentx = self.__possitionsPredicted[-1][0]
                currenty = self.__possitionsPredicted[-1][1]
                currentTheata = self.__possitionsPredicted[-1][2]
                i += dt


class motionArm():
    def __init__(self, d):
        self.d = d

        
    def calculateMotionArmNotCorrected(self, theata, dList=0):
        # r11 = (math.cos(theata[0]) * math.cos(theata[3]) * math.cos(theata[4]) * math.cos(theata[5])) - (math.cos(theata[0]) * math.sin(theata[3]) * math.sin(theata[5])) + (math.sin(theata[0]) * math.sin(theata[4]) * math.cos(theata[5]))
        # r21 = (math.sin(theata[0]) * math.cos(theata[3]) * math.cos(theata[4]) * math.cos(theata[5])) - (math.sin(theata[0]) * math.sin(theata[3]) * math.sin(theata[5])) - (math.cos(theata[0]) * math.sin(theata[4]) * math.cos(theata[5]))
        # r31 = - (math.sin(theata[3]) * math.cos(theata[4]) * math.cos(theata[5])) - (math.cos(theata[3]) * math.sin(theata[5]))
        # r12 = - (math.cos(theata[0]) * math.cos(theata[3]) * math.cos(theata[4]) * math.sin(theata[5])) - (math.cos(theata[0]) * math.sin(theata[3]) * math.cos(theata[5])) - (math.sin(theata[0]) * math.sin(theata[4]) * math.cos(theata[5]))
        # r22 = - (math.sin(theata[0]) * math.cos(theata[3]) * math.cos(theata[4]) * math.sin(theata[5])) - (math.sin(theata[0]) * math.sin(theata[3]) * math.sin(theata[5])) + (math.cos(theata[0]) * math.sin(theata[4]) * math.cos(theata[5]))
        # r32 = (math.sin(theata[3]) * math.cos(theata[4]) * math.cos(theata[5])) - (math.cos(theata[3]) * math.cos(theata[5]))
        # r13 = (math.cos(theata[0]) * math.cos(theata[3]) * math.sin(theata[4])) - (math.sin(theata[0]) * math.cos(theata[4]))
        # r23 = (math.sin(theata[0]) * math.cos(theata[3]) * math.sin(theata[4])) + (math.cos(theata[0]) * math.cos(theata[4]))
        # r33 = -(math.sin(theata[3]) * math.sin(theata[4]))

        if dList != 0:
            # Neither of these two affect the end result so we will just use the same values the entire calculation
            d1 = self.d[0]
            d6 = self.d[5]

            # These two values will change and need to be updated as we go
            d2 = dList[1]
            d3 = dList[2]
        else:
            d1 = self.d[0]
            d2 = self.d[1]
            d3 = self.d[2]
            d6 = self.d[5]

        # (c1 * c4 * s5 * d6) - (s1 * c5 * d6) - (s1 * d3)
        dx =  (math.cos(theata[0]) * math.cos(theata[3]) * math.sin(theata[4]) * d6) - (math.sin(theata[0]) * math.cos(theata[5]) * d6) - (math.sin(theata[0]) * d3)
        
        # (s1 * c4 * s5 * d6) + (c1 * c5 * d6) + (c1 * d3)
        dy =  (math.sin(theata[0]) * math.cos(theata[3]) * math.sin(theata[4]) * d6) - (math.cos(theata[0]) * math.cos(theata[5]) * d6) + (math.cos(theata[0]) * d3)
        
        # (-s4 * s5 * d6) + d1 + d2
        dz =  -(math.sin(theata[3]) * math.sin(theata[4]) * d6) + d1 + d2

        return [dx, dy, dz]
