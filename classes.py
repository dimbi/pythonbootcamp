class Eric:
    def __init__(self,eyes="brown",elbows=2,brain=.5):
        self.eyes = eyes
        self.elbows = elbows
        self.brain = brain

    def program(self,code):
        program = open("program.py","w")
        program.write(code)

    def juggle(self):
        self.emotional_state= "Happy!!!"

    def holocaust(self):
        self.emotional_state= "sad"

    def mood(self):
        return self.emotional_state

    def self_esteem(self,merry_talks=True):
        self.emotional_state = "horribly depressed"
        return self.emotional_state

    def __str__(self):
        return repr([self.eyes,self.elbows,self.brain,self.emotional_state])
