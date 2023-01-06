class EePin():
    def __init__(self):
        self.age = 28
        self.alive = True

    def dance(self):

        if self.alive:
            print("dancing")
            self.alive = False
if __name__=="__main__":
    print("In Pin")