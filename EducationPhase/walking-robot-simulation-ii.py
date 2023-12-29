class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.xpos = 0
        self.ypos = 0
        self.dir = "East"
        self.stepsOverall = 0
    def step(self, num: int) -> None:
        self.stepsOverall += num
        self.stepsOverall = self.stepsOverall% (2*(self.width+self.height)-4)
        if self.stepsOverall>(self.width+self.width+self.height-3) and self.stepsOverall<=2*(self.width+self.height)-4:  
            self.xpos = 0
            self.ypos = (self.height-1)-self.stepsOverall%(self.width+self.height+self.width-3)
            self.dir = "South"
        elif self.stepsOverall>self.width-1 and self.stepsOverall<=self.height+self.width-2:
            self.ypos = self.stepsOverall-(self.width-1)
            self.xpos = self.width-1
            self.dir = "North"
        elif self.stepsOverall>self.height+self.width-2 and self.stepsOverall<=((2*(self.width-1))+(self.height-1)):
            self.xpos = (self.width - 1) - self.stepsOverall%(self.width+self.height-2)
            self.ypos = self.height-1
            self.dir = "West"
        
            #if self.stepsOverall == 0:
            #    self.dir = "East"
        elif self.stepsOverall<=self.width-1:
            self.xpos = self.stepsOverall
            self.ypos = 0
            self.dir= "East"
        if self.xpos == 0 and self.ypos == 0:
            self.dir = "South"
    def getPos(self) -> List[int]:
        return [self.xpos,self.ypos]

    def getDir(self) -> str:
        return self.dir


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()