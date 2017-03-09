class Car(object):
 

  def __init__(self, name='General', model='GM', carType=None):
   
    self.name = name
    self.model = model
    self.carType = carType
    self.speed = 0


    if self.name == "Porshe" or self.name == "Koenigsegg":
     
       self.num_of_doors = 2
     
    else:
     
      self.num_of_doors = 4
     
     


  def is_saloon(self):
   
    if self.carType != 'trailer':
     
        self.carType == 'saloon'
       
        return True
       
    return False

if self.is_saloon() is False:
     
      self.num_of_wheels = 8
     
else:
     
      self.num_of_wheels = 4

  def drive(self, spd):
    
        if self.carType == 'trailer':
         
            self.speed = spd * 11
           
        else:
         
            self.speed = 10 ** spd

        return self