import random
class Human:
    def __init__(self, name = "Maris" , job = None , home = None , car = None) :
         self.name = name
         self.job = job
         self.home = home
         self.car = car
         self.gladness = 50
         self.stiety = 50
         def get_home(self):
              pass
         def get_car(self):
              pass
         def get_job(self):
              pass
         def get_home(self):
              pass
         def eat(self):
              pass
         def work(self):
              pass
         def shopping(self):
              pass
         def clear_home(self):
              pass
         def  day_indexes(self):
              pass
         def is_alive(self):
              pass
         def live(self):
              pass
         class Auto:
              def __init__(self, brand_list):
                   self.brand = random.choice(list(brand_list))
                   self.fuel = brand_list[self.brand]["fuel"]
                   self.strenght = brand_list[self.brand]["strenghth"]
                   self.cosumption = brand_list[self.brand]["cosumption"]
                   brands_of_cars = {"тазiк": {"fuel":2, "streght":180, "cosumption":6 },
                                                 "корито": {"fuel": 4, "streght": 220, "cosumption": 8},
                                                 "капiбара": {"fuel":999, "streght":999, "cosumption":999 }}