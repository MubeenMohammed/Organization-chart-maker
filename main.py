class University:
    '''
    A data type to represent a University
    
    Instance attributes:
        name(str) : name of the university
        location(str) : location of the university
        motto(str) : motto of the university
        date(tuple) : date of the university foundation
    '''
    def __init__(self,name = 'University',location = 'Somewhere' ,motto = 'Something' ,day = 1,month = 1,year = 2023):
        '''
        Constructor of the Class University.
        It assigns values to the class attributes like name,location,motto,date
        
        (str,str,str,int,int,int) --> no output
        
        >>> myuniversity = University('UofT','Toronto,Canada','Practise makes man perfect',15,03,1827)
        >>> myuniversity.name
        'UofT'
        >>> myuniversity.location
        'Toronto,Canada'
        >>> myuniversity.motto
        'Practise makes man perfect'
        >>> myuniversity.date
        '26,03,1827'
        
        >>> mcgill = University('McGill','Montreal,Canada','Brightest minds of the world',31,03,1821)
        >>> mcgill.name
        'Mcgill'
        >>> mcgill.location
        'Montreal,Canada'
        >>> mcgill.motto
        'Brightest minds of the world'
        >>> mcgill.date
        '31,31,1821'
        
        >>> concordia = University('Concordia','Montreal,Canada','Opportunities dont happen you have to create them',24,08,1974)
        >>> concordia.name
        'Concordia'
        >>> concordia.location
        'Montreal,Canada'
        >>> concordia.motto
        'Opportunities dont happen you have to create them'
        >>> concordia.date
        '24,08,1974'
        '''
        
    
        self.name = name
        self.location = location
        self.motto = motto
        if day <= 0 or month <= 0 or year <= 0:
            raise ValueError('The date cannot be negative or equal to 0')
        else:
            self.date = day,month,year
            
            
    def __str__(self):
        '''
        converts the University object into string using its name, location and founding year
        with its motto
        
        (no input) --> str
        
        >>> myuniversity = University('UofT','Toronto,Canada','Practise makes man perfect',15,03,1827)
        >>> str(myuniversity)
        'University of UofT was founded in (15, 3, 1827)\nIts main campus is located in
        Toronto,Canada\nIts Motto is: Practise makes aan perfect'
        
        >>> mcgill = University('McGill','Montreal,Canada','Brightest minds of the world',31,03,1821)
        >>> str(mcgill)
        'University of McGill was founded in (31, 3, 1821)\nIts main campus is located in
        Montreal,Canada\nIts Motto is: Brightest minds of the world'
        
        >>> concordia = University('Concordia','Montreal,Canada','Opportunities dont happen you have to create them',24,08,1974)
        >>> str(concordia)
        'University of Concordia was founded in (24, 8, 1974)\nIts main campus is located in Montreal,
        Canada\nIts Motto is: Opportunities dont happen you have to create them'

        '''
        
        intro = 'University of '+ self.name + ' was founded in ' + str(self.date)
        location = 'Its main campus is located in ' + self.location
        motto = 'Its Motto is: ' + self.motto
        return intro + '\n' + location + '\n' + motto
    
    
class JobPosition:
    
    '''
    A data type to represent a job position
    
    Instance attributes:
        job_id(int): it is an identification number of a job position
        description(str): it is a string describing about the position
        id_description_dict(dict): it is dictionary storing all the position description
                                    with corresponding job_id range
    '''
    
    id_description_dict = {'Teaching Assistant':[0,99],
                           'Professor':[100,499],
                           'Faculty Lecturer':[500,999],
                           'Department Chair':[1000,1999],
                           'Dean':[2000,2999],
                           'Vice Principal':[3000,3999],
                           'Principal':4000}
    
    
    def id_to_description(self):
        '''
        Assigns the description value to the job's description attribute corresponding to the job_id
        by checking the id_description_dict
        
        (int) --> (str)
        
        >>> Mubeen = JobPosition(468)
        >>> Mubeen.id_to_description()
        'Professor'
        
        >>> Sharukh = JobPosition(5)
        >>> Sharukh.id_to_description()
        'Teaching Assistant'
        
        >>> Salman = JobPosition(4000)
        >>> Salman.id_to_description()
        'Principal'
        
        '''
        if self.job_id < 4000:
            for key in self.id_description_dict:
                if self.job_id >= self.id_description_dict[key][0] and self.job_id <= self.id_description_dict[key][1]:
                    return key
        else:
            return 'Principal'
    def __init__(self, ID):
        '''
        constructor of the class JobPosition and it assigns value to job_id attribute
        and also description by calling id_to_description method above
        
        (int) --> no output
        
        >>> Mubeen = JobPosition(468)
        >>> Mubeen.job_id
        468
        >>> Mubeen.description
        'Professor'
        
        >>> Sharukh = JobPosition(9)
        >>> Sharukh.job_id
        9
        >>> Sharukh.description()
        'Teaching Assistant'
        
        >>> Salman = JobPosition(4000)
        >>> Salman.job_id
        4000
        >>> Salman.description
        'Principal'
        
        '''
        
        self.job_id = ID
        self.description = self.id_to_description()
        
        
    def __str__(self):
        '''
        returns the description of the JobPosition by conversting it into string type
        
        (no input) --> str
        
        >>> Mubeen = JobPosition(468)
        >>> Mubeen.__str__()
        'Professor'
        
        >>> Sharukh = JobPosition(9)
        >>> Sharukh.__str__()
        'Teaching Assistant'
        
        >>> Salman = JobPositon(4000)
        >>> Salman.__str__()
        'Principal'
        '''
        
        return str(self.description)
        
        
    def get_id(self):
        '''
        returns the job_id in integer type
        
        (no input) --> int
        
        >>> Mubeen = JobPosition(468)
        >>> Mubeen.get_id()
        468
        
        >>> Sharukh = JobPosition(9)
        >>> Sharukh.get_id()
        9
        
        >>> Salman = JobPosition(4000)
        >>> Salman.get_id()
        4000
        '''
        
        return self.job_id
        
        
    def set_id(self,new_id):
        '''
        Changes the instance attributes job_id by assigning it with new value and also changing the description
        attribute according to the new_id
        
        (int) --> no output
        
        >>> Mubeen = JobPositon(468)
        >>> Mubeen.set_id(4000)
        >>> print(Mubeen)
        Principal
        
        >>> Sharukh = JobPosition(9)
        >>> Sharukh.set_id(500)
        >>> print(Sharukh)
        Faculty Lecturer
        
        >>> Salman = JobPosition(4000)
        >>> Salman.set_id(2)
        >>> print(Salman)
        Teaching Assistant
        '''
        
        self.job_id = new_id
        self.description = self.id_to_description(new_id)
        
        
class Employee:
    '''
    A data type to represent the Employee
    
    Instance Attributes:
        first_name(str): it is a string used to store first name of the employee
        last_name(str): it is a string used to store last name of the employee
        ref(int): it is an integer used to store a unique identification number
        position(JobPosition): it is an object of class JobPosition and it stores the position of the employee
        supervisor(int): it is a employee's supervisor reference number
        nb_employee(int): it is number that keeps track of number of Employee objects created
        
    '''
    
    nb_employee = 0
    
    
    def __init__(self,first_name='Employee',last_name='Employee',reference=0,job_id=4000,sup_ref=-1):
        '''
        It is a constructor of the class Employee and it assigns values to the class attributes
        it also creates a JobPosition object and assigns it to position attribute of class Employee
        
        (str,str,int,int,int) --> no output
        
        >>> Mubeen = Employee('Mubeen','Mohammed',50,486,3)
        >>> Mubeen.first_name
        'Mubeen'
        >>> Mubeen.last_name
        'Mohammed'
        >>> Mubeen.ref
        50
        >>> Mubeen.position
        'Professor'
        >>> Mubeen.supervisor
        3
        
        >>> employee = Employee
        >>> employee.first_name
        'Employee'
        >>> employee.last_name
        'Employee'
        >>> employee.ref
        0
        >>> employee.position
        'Principal
        >>> employee.supervisor
        -1
        
        >>> Uday = Employee('Uday','Parmar',5,958,-1)
        >>> Uday.first_name
        'Uday'
        >>> Uday.last_name
        'Parmar'
        >>> Uday.ref
        5
        >>> Uday.position
        'Faculty Lecturer'
        >>> Uday.supervisor
        -1
        
        
        '''
        
        self.first_name = first_name
        self.last_name = last_name
        self.ref = reference
        self.position = JobPosition(job_id)
        self.supervisor = sup_ref
        Employee.nb_employee += 1
        
        
    def __str__(self):
        '''
        returns a string contaning the first name, last name and position of the employee
        
        (no input) --> str
        
        >>> Mubeen = Employee('Mubeen','Mohammed',50,486,3)
        >>> str(Mubeen)
        'Mubeen Mohammed - Professor'
        
        >>> employee = Employee()
        >>> str(employee)
        'Employee Employee - Principal'
        
        >>> Uday = Employee('Uday','Parmar',5,958,-1)
        >>> str(Uday)
        'Uday Parmar - Faculty Lecturer'
        '''
        
        name = self.first_name + ' ' + self.last_name
        position = str(self.position)
        return name + '-' + position
    
    
    def find_supervisor(self,e_list):
        '''
        returns the current emplooyee's direct supervisor
        
        (list) --> Employee
        
        >>> e = Employee('Salman','Khan',1127,870,4)
        >>> e1 = Employee('Sharukh','Khan',9,870,5)
        >>> e2 = Employee('Katrina','Kaif',5,1200,3)
        >>> e3 = Employee('Ashiwariya','Rai',4,1100,3)
        >>> e4 = Employee('Mubeen','Mohammed',1,4000,-1)
        >>> e5 = Employee('Bruce','Wayne',3,2440,2)
        >>> employee_list = [e,e1,e2,e3,e4,e5]
        
        >>> supervisor_1 = e.find_supervisor(employee_list)
        >>> print(supervisor_1)
        Ashiwariya Rai - Deparment Chair
        
        >>> supervisor_2 = e4.find_supervisor(employee_list)
        >>> print(supervisor_2)
        Mubeen Mohammed - Principal
        
        >>> supervisor_3 = e2.find_supervisor(employee_list)
        >>> print(supervisor_3)
        Bruce Wayne - Dean
        
        '''
        
        sup_ref = self.supervisor
        for e in e_list:
            if sup_ref == e.ref:
                return e
        return self
            
            
    def __eq__(self,e):
        '''
        returns a boolean value by checking if the both the employee has the same refrence
        number and same first and last names
        
        (Employee) --> Boolean value
        
        >>> e1 = Employee('Sharukh','Khan',9,870,5)
        >>> e2 = Employee('Sharukh','Khan',9,520,2)
        >>> e1 == e2
        True
        
        >>> e1 = Employee('Katrina','Kaif',5,1200,3)
        >>> e2 = Employee('Katrina','Kaif',6,1200,3)
        >>> e1 == e2
        False
        
        >>> e1 = Employee('Bruce','Wayne',2,565,3)
        >>> e2 = Employee('Mubeen','Mohammed',5,586,5)
        >>> e1 == e2
        False
        
        '''
        
        if self.ref == e.ref and self.first_name == e.first_name and self.last_name == e.last_name:
            return True
        return False
    
    
class OrganizationalChart:
    
    '''
    A data type to represent the hierarchical tree of the object Employee
    
    Instance Attributes:
        university(University): it is an object of class University to represent the university
        employee_list(list): it is list of all employees of the class Employee
    '''
    
    
    def load_chart(self,filepath):
        '''
        reads the given input file and builds the employee list with employee objects of class Employee
        and also a university object with class University
        
        (str) --> no output
        
        >>> chart_1 = OrganizationalChart('FileNone.csv')
        File does not exist
        
        >>> chart_2 = OrganizationalChart('FakeFile.csv')
        File does not exist
        
        >>> chart = OrganizationalChart('McGill_OrgChart.csv')
        >>> print(chart)
        H.Deep Saini-Principal
        Angela Campbell-Vice Principal
        Bruce Lennox-Dean
        Gregor Fussmann-Department Chair
        Mathieu Blanchette-Department Chair
        Oana Balmau-Professor
        Jin Guo-Professor
        Christophe Dubach-Professor
        Guilia Albertini-Faculty Lecturer
        Faten Mhiri-Faculty Lecturer
        Joseph Vybihall-Faculty Lecturer
        Jacob Errington-Faculty Lecturer
        Saad Yousaf-Teaching Assistant
        MirHamed JafarzadehAsl-Teaching Assistant
        Neil Rahman-Teaching Assistant
        
        '''
        try:
            file = open(filepath,'r')
            file_list = []
            employee_list = []
            for line in file:
                file_list.append(line.strip().split(','))
            #file_dict = dict(file_list)
            #print(file_list)
            i = 0
            for element in file_list[0:4]:
                if i == 0:
                    name = element[1]
                elif i == 1:
                    location = element[1].strip() + ',' + element[2]
                elif i == 2:
                    date = int(element[1])
                    month = int(element[2])
                    year = int(element[3])
                elif i == 3:
                    motto = element[1]
                i += 1
            self.university = University(name,location,motto,date,month,year)
            for element in file_list[7:]:
                ref_id = int(element[0])
                job_id = int(element[1])
                first_name = element[2].split(' ')[0]
                last_name = element[2].split(' ')[1]
                sup_ref = int(element[3])
                position = element[4]
                employee = Employee(first_name,last_name,ref_id,job_id,sup_ref)
                self.employee_list.append(employee)
        except FileNotFoundError:
            print('File does not exist')
        except:
            print('There was an error with the file')
    def __init__(self,filename):
        '''
        It is a constructor of the class Organizational Chart which creates
        empty string of University object and empty list of employee of class
        Employee
        
        (str) --> no output
        
        
        >>> chart_1 = OrganizationalChart('FileNone.csv')
        File does not exist
        
        >>> chart_2 = OrganizationalChart('FakeFile.csv')
        File does not exist
        
        >>> chart = OrganizationalChart('McGill_OrgChart.csv')
        >>> print(chart)
        H.Deep Saini-Principal
        Angela Campbell-Vice Principal
        Bruce Lennox-Dean
        Gregor Fussmann-Department Chair
        Mathieu Blanchette-Department Chair
        Oana Balmau-Professor
        Jin Guo-Professor
        Christophe Dubach-Professor
        Guilia Albertini-Faculty Lecturer
        Faten Mhiri-Faculty Lecturer
        Joseph Vybihall-Faculty Lecturer
        Jacob Errington-Faculty Lecturer
        Saad Yousaf-Teaching Assistant
        MirHamed JafarzadehAsl-Teaching Assistant
        Neil Rahman-Teaching Assistant
        >>> print(chart.university)
        University of McGill was founded in (31, 3, 1821)
        Its main campus is located in Montreal,Canada
        Its Motto is: By work all things increase and grow

        '''
        
        self.university = ''
        self.employee_list = []
        self.load_chart(filename)
        
        
    def __str__(self):
        '''
        returns the employee list in the string type
        
        (no input) --> no output
        
        >>> chart = OrganizationalChart('McGill_OrgChart.csv')
        >>> str(chart)
        '\nH.Deep Saini-Principal\nAngela Campbell-Vice Principal\nBruce
        Lennox-Dean\nGregor Fussmann-Department Chair\nMathieu Blanchette-Department
        Chair\nOana Balmau-Professor\nJin Guo-Professor\nChristophe Dubach-Professor\n
        Guilia Albertini-Faculty Lecturer\nFaten Mhiri-Faculty Lecturer\nJoseph Vybihall-
        Faculty Lecturer\nJacob Errington-Faculty Lecturer\nSaad Yousaf-Teaching Assistant
        \nMirHamed JafarzadehAsl-Teaching Assistant\nNeil Rahman-Teaching Assistant'
        
        '''
        
        employee_str = ''
        for employee in self.employee_list:
            employee_str += '\n'+str(employee)
        return employee_str


    def is_in_list(self,employee):
        '''
        returns a boolean by checking whether or not the
        employee is present in the employee list
        
        (Employee) --> Boolean value
        
        >>> e1 = Employee('Guilia','Albertini',9,870,5)
        >>> chart = OrganizationalChart('McGill_OrgChart.csv')
        >>> chart.is_in_list(e1)
        True
        
        >>> e2 = Employee('Mubeen','Mohammed',5,862,6)
        >>> chart = OrganizationalChart('McGill_OrgChart.csv')
        >>> chart.is_in_list(e2)
        False
        
        >>> e3 = Employee('Uday','Mohammed',2,85,6)
        >>> chart = OrganizationalChart('McGill_OrgChart.csv')
        >>> chart.is_in_list(e3)
        False
        '''
        
        
        if employee in self.employee_list:
            return True
        else:
            return False
        
        
    def find_hierarchical_line(self,employee):
        '''
        first it checks if the employee is in the employee_list or not and
        then it makes a hierarchical list that has all the direct supervisors
        above the employee
        
        (Employee) --> no output
        
        >>> chart = OrganizationalChart('McGill_OrgChart.csv')
        >>> e1 = Employee('Guilia','Albertini',9,800,5)
        >>> chart.find_hierarchical_line(e1)
        [<__main__.Employee object at 0x000002473D26AB60>, <__main__.Employee
        object at 0x000002473D26AB00>, <__main__.Employee object at 0x00000247
        3D26AF80>, <__main__.Employee object at 0x000002473D26B370>, <__main__.
        Employee object at 0x000002473D26B820>]
        
        '''
        
        hierarchical_list = [employee]
        if self.is_in_list(employee):
            i = employee.supervisor 
            while i != -1:
                hierarchical_list.append(employee.find_supervisor(self.employee_list))
                i = (employee.find_supervisor(self.employee_list)).supervisor
                employee = employee.find_supervisor(self.employee_list)
            hierarchical_list = hierarchical_list[::-1]
            return hierarchical_list
        else:
            return []
    def print_hierarchical_line(self,employee):
        '''
        it prints the hierarchical_line, first by making the hierarchical line from
        find_hierarchical_line function and prints in the order
        
        (Employee) --> None
        
        >>> chart = OrganizationalChart('McGill_OrgChart.csv')
        >>> e = Employee('Faten','Mhiri',10,570,5)
        >>> chart.print_hierarchical_line(e)
        +-> H.Deep Saini - Principal
        | +-> Angela Campbell - Vice Principal
        | | +-> Bruce Lennox - Dean
        | | | +-> Mathieu Blanchette - Department Chair
        | | | | +-> Faten Mhiri - Faculty Lecturer
        '''
        
        hierarchical_str = ''
        hierarchical_list = self.find_hierarchical_line(employee)
        i = 0
        vertical_lines = 0
        for employee in hierarchical_list:
            hierarchical_str += '\n'*i + '| '*vertical_lines + '+-> ' + str(employee)
            vertical_lines += 1
            i += 1
        print(hierarchical_str)
      
p = OrganizationalChart('McGill_OrgChart.csv')
e = Employee('Guilia','Albertini',9,800,5)
# print(p.print_hierarchical_line(e))

        
