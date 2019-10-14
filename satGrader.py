import json

class satGrader:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.finalMathScore = None
        self.finalWritingScore = None
        self.finalReadingScore = None
        self.finalTotalScore = None

    def calculateMathScore(self, score, category):
        # error handling

        # if score is not number
            #if(int(score))
        try:
            foo = int(score)
        except ValueError as err:
            print(err)
            return ValueError

        if(category != 'Math' or category != 'Reading' or category != "Writing"):
            return ValueError

        # temp[score].get[Str(score)]
        with open('JSON/satScoreGuide1.json', 'r') as jsonFile:
            data = json.load(jsonFile)
            temp = data[category]

            # if categories for right final score var


            print(temp[score].get(str(score)))

            '''
            Original alg
            for x in temp:
                for (key) in x:
                    if(key == '7'):
                        print("found")
                        print(x.get(key))
            '''


test = satGrader()
test.calculateMathScore("7m", 'Math')