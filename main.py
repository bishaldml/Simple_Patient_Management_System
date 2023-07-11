import modules as md

'''
    Patient Management System
'''


class Hospital:
    def __init__(self,action):
        self.action = action

    def PatientMgmt(self):

         #INSERTION OPERATION
        if self.action == "insert" or self.action == "i":
            md.insert()

        #DISPLAY PATIENT DATA
        if self.action == "display" or self.action == "dis":
            File = open("patient.data","r")
            contents = File.read()
            print(contents)
            File.close()

        #DELETION OPERATION
        if self.action == "delete"or self.action == "d":
            File = open("patient.data","r+")
            pd = File.readlines()
            print()
            print("Patient Data: Before Deletion, Choose the patient that you want to delete")
            for data in pd:
                print(data.strip())
            File.seek(0)
            File.truncate()
            
            print()
            pid = input("Enter PID : ")
            for data in pd:
                s1 = data.find(pid)
                if s1 != 0:
                    File.write(data)
            File.close()
                

action = "start"
while action != "stop" and action != "s":
    action = input("Please enter your action (Insert-I, Delete-D, Display-Dis and Stop-S) ").lower()
    hosp = Hospital(action)
    hosp.PatientMgmt()