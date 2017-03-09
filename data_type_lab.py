def data_type(type_of_data):
    
    
    if type(type_of_data) == str:
        return  (len(type_of_data))
    
    elif type(type_of_data) == int:
        if type_of_data >100:
            return "more than 100"
        elif type_of_data <100:
            return "less than 100"
        else:
            return "equal to 100"
            
    elif type(type_of_data) == bool:
        return type_of_data
    
    elif type (type_of_data) == list:
      #new section
        if len(type_of_data) >= 3:
            return type_of_data[2]
        else:
            return None
    
    else: 
        return "no value"
    
        
data_type("andela")
data_type(None)
data_type(True)
data_type(3)
data_type(200)
data_type([1, 2, 3])
def data_type(type_of_data):
    
    
