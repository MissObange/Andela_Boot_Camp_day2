class Department:
    def __init__(self, dep_id, dep_name):
        self.dep_id = dep_id
        self.dep_name = dep_name
    
    def department_details(self):
        
        
        print ([self.dep_id, self.dep_name])
        
        
class Students(Department):
    def __init__(self, std_name, std_id):
        self.std_name = std_name
        self.std_id = std_id
        
    
        
    def student_details(self):
        Department.__init__(self, self.dep_name, self.dep_id)
        print (self.dep_name)
        
        print ([self.std_name, self.std_id])
        

class Lecturers(Department):
    def __init__(self, lec_name, lec_id):
        self.lec_name = lec_name
        self.lec_id = lec_id
        #self.lec_dep = self.dep_name
        
    def lecturer_details(self):
        Department.__init__(self, self.dep_name, self.dep_id)
        print (self.dep_name)
        
        print ([self.lec_name, self.lec_id])

        
department1 = Department(34, "Architecture")
print ("Dep ID: "+str(department1.dep_id), " Dep Name: " + str(department1.dep_name))

     


student1 = Students("Sharon Obange", 11200740)
print ("Student ID: "+ str(student1.std_id), " Student Name: " + str(student1.std_name))
#print("Department: " + student1.dep_name)


lecturer1 = Lecturers("Winston Ojenge", 345, )
print ("Lec ID: "+ str(lecturer1.lec_id), " Lec Name: " + str(lecturer1.lec_name))
#print("Department: " + lecturer1.dep_name)
