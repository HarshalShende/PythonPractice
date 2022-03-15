class Computer:

    def __init__(self, cpu, ram):
        self.cpu=cpu
        self.ram=ram

    def disp(self):
        print("Configuratio is : ",self.cpu, " ", self.ram)

com1=Computer("i5", "2gb")
com2=Computer("Ryzen 5", "8gb")

com1.disp()
com2.disp()