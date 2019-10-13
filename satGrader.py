import json

class satGrader:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rawMathScore = None
        self.rawWritingScore = None
        self.rawReadingScore = None
        self.finalTotalScore = None

    def calculateMathScore(self):
        with open('JSON/satScoreGuide1.json', 'r') as jsonFile:
            data = json.load(jsonFile)
            temp = data['Math']

            for x in temp:
                print(x)
                for (key) in x:
                    print(x.get(key))


test = satGrader()
test.calculateMathScore()