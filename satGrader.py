
class satGrader:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.readingScore = None
        self.mathScore = None
        self.writingScore = None
        self.totalScore = None

    def getRawReading(self, rawRead):
        self.readingScore = self.readingConversion(rawRead)

    def getRawMath(self, rawMath):
        self.mathScore = self.mathConversion(rawMath)

    def getRawWriting(self, rawWrite):
        self.writingScore = self.writingConversion(rawWrite)

    def readingConversion(self, rawRead):
        # TODO put conversion code in 

        try:
            if (int(rawRead) <= 0):
                raise ValueError("Value is below 0")
            if (int(rawRead) > 52):
                raise ValueError("Value is over 52")
            if (type(rawRead) != int):
                raise ValueError("Not and integer")
            
        except ValueError as err:
            print("There was an error in the raw reading score", err)
        finally:
            if(rawRead == 0):
                return 10
            elif(rawRead == 1):
                return 10
            elif(rawRead == 2):
                return 10
            elif(rawRead == 3):
                return 11
            elif(rawRead == 4):
                return 12
            elif(rawRead == 5):
                return 13
            elif(rawRead == 6):
                return 14
            elif(rawRead == 7):
                return 15
            elif(rawRead == 8):
                return 15
            elif(rawRead == 9):
                return 16
            elif(rawRead == 10):
                return 17
            elif(rawRead == 11):
                return 17
            elif(rawRead == 12):
                return 18
            elif(rawRead == 13):
                return 19
            elif(rawRead == 14):
                return 19
            elif(rawRead == 15):
                return 20
            elif(rawRead == 16):
                return 20
            elif(rawRead == 17):
                return 21
            elif(rawRead == 18):
                return 21
            elif(rawRead == 19):
                return 22
            elif(rawRead == 20):
                return 22
            elif(rawRead == 21):
                return 23
            elif(rawRead == 22):
                return 23
            elif(rawRead == 23):
                return 24
            elif(rawRead == 24):
                return 24
            elif(rawRead == 25):
                return 25
            elif(rawRead == 26):
                return 25
            elif(rawRead == 27):
                return 26
            elif(rawRead == 28):
                return 26
            elif(rawRead == 29):
                return 27
            elif(rawRead == 30):
                return 28
            elif(rawRead == 31):
                return 28
            elif(rawRead == 32):
                return 29
            elif(rawRead == 33):
                return 29
            elif(rawRead == 34):
                return 30
            elif(rawRead == 35):
                return 30
            elif(rawRead == 36):
                return 31
            elif(rawRead == 37):
                return 31
            elif(rawRead == 38):
                return 32
            elif(rawRead == 39):
                return 32
            elif(rawRead == 40):
                return 33
            elif(rawRead == 41):
                return 33
            elif(rawRead == 42):
                return 34
            elif(rawRead == 43):
                return 35
            elif(rawRead == 44):
                return 35
            elif(rawRead == 45):
                return 36
            elif(rawRead == 46):
                return 37
            elif(rawRead == 47):
                return 37
            elif(rawRead == 48):
                return 38
            elif(rawRead == 49):
                return 38
            elif(rawRead == 50):
                return 39
            elif(rawRead == 51):
                return 40
            elif(rawRead == 52):
                return 40
            

        return None

    def mathConversion(self, rawMath):
        # TODO put conversion code in
        try:
            if (int(rawMath) <= 0):
                raise ValueError("Value is below 0")
            if (int(rawMath) > 58):
                raise ValueError("Value is over 58")
            if (type(rawMath) != int):
                raise ValueError("Not an integer")

        except ValueError as err:
            print("There was an error in the raw math score", err)
        finally:
            if(rawMath == 0):
                return 200
            elif(rawMath == 1):
                return 200
            elif(rawMath == 2):
                return 210
            elif(rawMath == 3):
                return 230
            elif(rawMath == 4):
                return 240
            elif(rawMath == 5):
                return 260
            elif(rawMath == 6):
                return 280
            elif(rawMath == 7):
                return 290
            elif(rawMath == 8):
                return 310
            elif(rawMath == 9):
                return 320
            elif(rawMath == 10):
                return 330
            elif(rawMath == 11):
                return 340
            elif(rawMath == 12):
                return 360
            elif(rawMath == 13):
                return 370
            elif(rawMath == 14):
                return 380
            elif(rawMath == 15):
                return 390
            elif(rawMath == 16):
                return 410
            elif(rawMath == 17):
                return 420
            elif(rawMath == 18):
                return 430
            elif(rawMath == 19):
                return 440
            elif(rawMath == 20):
                return 450
            elif(rawMath == 21):
                return 460
            elif(rawMath == 22):
                return 470
            elif(rawMath == 23):
                return 480
            elif(rawMath == 24):
                return 480
            elif(rawMath == 25):
                return 490
            elif(rawMath == 26):
                return 500
            elif(rawMath == 27):
                return 510
            elif(rawMath == 28):
                return 520
            elif(rawMath == 29):
                return 520
            elif(rawMath == 30):
                return 530
            elif(rawMath == 31):
                return 540
            elif(rawMath == 32):
                return 550
            elif(rawMath == 33):
                return 560
            elif(rawMath == 34):
                return 560
            elif(rawMath == 35):
                return 570
            elif(rawMath == 36):
                return 580
            elif(rawMath == 37):
                return 590
            elif(rawMath == 38):
                return 600
            elif(rawMath == 39):
                return 600
            elif(rawMath == 40):
                return 610
            elif(rawMath == 41):
                return 620
            elif(rawMath == 42):
                return 630
            elif(rawMath == 43):
                return 640
            elif(rawMath == 44):
                return 650
            elif(rawMath == 45):
                return 660
            elif(rawMath == 46):
                return 670
            elif(rawMath == 47):
                return 670
            elif(rawMath == 48):
                return 680
            elif(rawMath == 49):
                return 690
            elif(rawMath == 50):
                return 700
            elif(rawMath == 51):
                return 710
            elif(rawMath == 52):
                return 730
            elif(rawMath == 53):
                return 740
            elif(rawMath == 54):
                return 750
            elif(rawMath == 55):
                return 760
            elif(rawMath == 56):
                return 780
            elif(rawMath == 57):
                return 790
            elif(rawMath == 58):
                return 800
            
        return None

    def writingConversion(self, rawWrite):
        # TODO put conversion code in 
        try:
            if (int(rawWrite) <= 0):
                raise ValueError("Value is below 0")
            if (int(rawWrite) > 44):
                raise ValueError("Value is over 44")
            if (type(rawWrite) != int):
                raise ValueError("Value is not an integer")

        except ValueError as err:
            print("There was an error in the raw reading score", err)
        finally:
            if(rawWrite == 0):
                return 10
            elif(rawWrite == 1):
                return 10
            elif(rawWrite == 2):
                return 10
            elif(rawWrite == 3):
                return 10
            elif(rawWrite == 4):
                return 11
            elif(rawWrite == 5):
                return 12
            elif(rawWrite == 6):
                return 13
            elif(rawWrite == 7):
                return 13
            elif(rawWrite == 8):
                return 14
            elif(rawWrite == 9):
                return 15
            elif(rawWrite == 10):
                return 16
            elif(rawWrite == 11):
                return 16
            elif(rawWrite == 12):
                return 17
            elif(rawWrite == 13):
                return 18
            elif(rawWrite == 14):
                return 19
            elif(rawWrite == 15):
                return 19
            elif(rawWrite == 16):
                return 20
            elif(rawWrite == 17):
                return 21
            elif(rawWrite == 18):
                return 21
            elif(rawWrite == 19):
                return 22
            elif(rawWrite == 20):
                return 23
            elif(rawWrite == 21):
                return 23
            elif(rawWrite == 22):
                return 24
            elif(rawWrite == 23):
                return 25
            elif(rawWrite == 24):
                return 25
            elif(rawWrite == 25):
                return 26
            elif(rawWrite == 26):
                return 26
            elif(rawWrite == 27):
                return 27
            elif(rawWrite == 28):
                return 28
            elif(rawWrite == 29):
                return 28
            elif(rawWrite == 30):
                return 29
            elif(rawWrite == 31):
                return 30
            elif(rawWrite == 32):
                return 30
            elif(rawWrite == 33):
                return 31
            elif(rawWrite == 34):
                return 32
            elif(rawWrite == 35):
                return 32
            elif(rawWrite == 36):
                return 33
            elif(rawWrite == 37):
                return 34
            elif(rawWrite == 38):
                return 34
            elif(rawWrite == 39):
                return 35
            elif(rawWrite == 40):
                return 36
            elif(rawWrite == 41):
                return 37
            elif(rawWrite == 42):
                return 38
            elif(rawWrite == 43):
                return 39
            elif(rawWrite == 44):
                return 40
            
        return None


    def finalScore(self):
        # TODO implement error handling for Scores if None
        # ADD(READ + WRITE) * 10 + MATH

        try:
            if (self.readingScore == None or self.readingScore < 10 or self.readingScore > 40):
                raise ValueError("Invalid Converted Reading Score")
    
            if (self.writingScore == None or self.writingScore < 10 or self.writingScore > 40):
                raise ValueError("Invalid Converted Writing Score")
        
            if (self.mathScore == None or self.mathScore < 200 or self.mathScore > 800):
                raise ValueError("Invalid Converted Math Score")
                
        
            
            self.readWriteScore = (self.readingScore + self.writingScore) * 10
            self.totalScore = self.readWriteScore + self.mathScore

            if (self.readWriteScore < 200 or self.readWriteScore > 800):
                raise ValueError("Invalid Total Converted Reading and Writing Score")
            if (self.totalScore < 400 or self.totalScore > 1600):
                raise ValueError("Invalid Final Total SAT Score")


        except ValueError as err:
            print("Something went wrong: " , err)
        finally:
            if (self.totalScore == None):
                return "Could not determine SAT SCORE"
            else:
                return self.totalScore
            
