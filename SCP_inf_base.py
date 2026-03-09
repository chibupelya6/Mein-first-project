class Employee():
    def __init__(self, name, born, position, subdivision, job_start, number, acess, status):
        self.name = name
        self.born = born
        self.position = position
        self.subdivision = subdivision
        self.job_start = job_start
        self.number = number
        self.acess = acess
        self.status = status

    def prEmployeeinf(self):
        print('Emploeyee: Name:', self.name, 'Birthday:', self.born, 'Position:', self.position, 'Subdivision:', self.subdivision, 'Started work at:', self.job_start, 'Number:', self.number, 'Status:', self.status) 

    def prShortinf(self):
        print(f'Name: {self.name} Subdivision: {self.subdivision} Number: {self.number}')

    def cStatus(self):
        cS = input('Type new status. Alive or Dead ')
        self.status = cS        


class SCP():
    def __init__(self, code_name, class_, number, cont_conds, status):
        self.code_name = code_name
        self.class_ = class_
        self.number = number
        self.cont_conds = cont_conds
        self.status = status

    def prSCPinf(self):
        print(f'SCP: Code name: {self.code_name} Class: {self.class_} Number: {self.number} Containment conditions: {self.cont_conds} Status: {self.status}')    
    

    def cStatus(self):
        cS = input('Type new status. Alive or Dead ')
        self.status = cS 


d9341 = Employee('Mike Brown', '14.06.1986', 'Light Containment Zone', 'D_Class', '16.10.2003', '9341', '0', 'live')
d9341.prEmployeeinf()
a0234 = Employee('Radeon Gay', '24.12.1999', 'Reinforced Containment Zone', 'A_Class', '17.8.2020', '234', '2', 'live')
a0234.prEmployeeinf()


scp_173 = SCP('Cookie', 'Euclid', '173', 'Container', 'Containts')
scp_173.prSCPinf()
d9341.cStatus()
d9341.prEmployeeinf()


