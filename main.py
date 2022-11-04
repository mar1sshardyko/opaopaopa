import random
class Shadowfiend:
    def __init__(self, name = "Shadowfiend" , shadowraze = None , souls = None , ult = None) :
         self.name = name
         self.shadowraze = shadowraze
         self.souls = souls
         self.ult = ult
         self.gladness = 50
         self.stiety = 50
         def get_souls(self):
              pass
         def get_ult(self):
              pass
         def get_shadowraze(self):
              pass
         def get_souls(self):
              pass
         def eat(self):
              pass
         def work(self):
              pass
         def shopping(self):
              pass
         def eat_souls(self):
              pass
         def  day_indexes(self):
              pass
         def is_alive(self):
              pass
         def live(self):
              pass
         class Ultimate:
              def __init__(self, brand_list):
                   self.brand = random.choice(list(brand_list))
                   self.fuel = brand_list[self.brand]["damage"]
                   self.strenght = brand_list[self.brand]["soulsaway"]
                   self.cosumption = brand_list[self.brand]["strah"]
                   brands_of_cars = {"1soulult": {"damage":55, "soulsaway":1, "cosumption":55 },
                                                 "15soulult": {"damage": 111, "soulsaway": 15, "cosumption": 111},
                                                 "soulofcapybara": {"damage":999, "soulsaway":999, "cosumption":999 }}