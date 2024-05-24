def mera_function(filepath):
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
            location = element[1] + ',' + element[2]
        elif i == 2:
            date = element[1]
            month = element[2]
            year = element[3]
        elif i == 3:
            motto = element[1]
        i += 1
    #self.university = University(name,location,motto,date,month,year)
    for element in file_list[7:]:
        print(element)
        #ref_id = element[0]
        #job_id = element[1]
        #first_name = element[2].split(' ')[0]
        #last_name = element[2].split(' ')[1]
        #sup_ref = element[3]
        #position = element[4]
        #self.employee = Employee(first_name,last_name,ref_id,job_id,sup_ref)
      
mera_function('McGill_OrgChart.csv')        