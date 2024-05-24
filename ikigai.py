class Ikigai():
    @property
    def ikigai(self):
        return self.__ikigai
    
    def __init__(self, love=[], need=[], paid=[], good=[]): 
        # Level 1
        self.love = love
        self.need = need
        self.paid = paid
        self.good = good
        self.__ikigai = []        

    def generate(self):
        # Level 4
        mission, vocation, profession, passion = self.__generate_2()
        unsuccessful, incertanty, empty, useless = self.__generate_3(
            mission, vocation, profession, passion)
        
        self.__ikigai = list(set(unsuccessful).intersection(
            list(set(incertanty).intersection(
                list(set(empty).intersection(
                    useless
                )) )) ))
        return self.__ikigai

    def __generate_2(self):
        # Level 2
        mission = list(set(self.love).intersection(self.need))
        vocation = list(set(self.need).intersection(self.paid))
        profession = list(set(self.paid).intersection(self.good))
        passion = list(set(self.good).intersection(self.love))
        
        return mission, vocation, profession, passion

    def __generate_3(self, mission, vocation, profession, passion):
        # Level 3
        unsuccessful = list(set(passion).intersection(mission))
        incertanty = list(set(mission).intersection(vocation))
        empty = list(set(vocation).intersection(profession))
        useless = list(set(profession).intersection(passion))
        
        return unsuccessful, incertanty, empty, useless

    def show_message(self):
        other = "You can also live for things like:\n" + \
                str([self.__ikigai[i] for i in range(1, len(self.__ikigai))]) \
                if len(self.__ikigai) > 1 \
                else ""
        
        print("What you love to do, that you do so good that the worlds needs and will pay you to do so is:\n",
                self.__ikigai[0], 
                "\n (Acording to your inputs.)\n",
                other
                )
        
    def save(self, file_name):
        if file_name:
            f = open(file_name, "a")
            f.write(str(self.love) + "\n" + str(self.need) + "\n" + str(self.paid) + "\n" + str(self.good))
            f.write("\n" + str(self.__ikigai))
            f.close()