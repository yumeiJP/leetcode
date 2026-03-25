class Solution:
    def turnIntoDenary(self, number:str):

        length = len(number)

        count = 0

        for i in range (len(number)):
            if number[i]==1:
                power = length-i-1
            count += 2**(power)
        
        return power
    

    '''    def findHighestPower(number):
        i = 0
        while 1:
            if 2**i > number:
                return i-1'''
    
    def turnIntoBinary(self, number):
        '''
        highestPower = self.findHighestPower(number)
        binaryID = []

        for i in len(highestPower):
            power = highestPower - i

            difference = number - 2**power
        '''

        binary = []
        if number == 0:
            return "0"
        while number 0 1:
            binary.append(number%2)
            number = int(number/2)

        binary.reverse()
        
        output = ""

        for num in binary:
            output += str(num)
        return output

    def addBinary(self, a: str, b: str) -> str:

        aDen = self.turnIntoDenary(a)
        bDen = self.turnIntoDenary(b)

        totalDen = aDen + bDen

        return self.turnIntoBinary(totalDen)
