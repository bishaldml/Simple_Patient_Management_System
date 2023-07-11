def insert():
    pid = input("Enter PID : ")
    #Check for duplicate value for PID
    pdf = open("patient.data","r")
    pd = pdf.readlines()
    if len(pd) > 0:
        for data in pd:
            s1 = data.find(pid)
            print(data)
            if s1 == 0:
                print("The Patient ID: ",pid," Already exists")
                pdf.close()
                break
            else:
                pdf.close()
                pname = input("Enter Patient Name : ")
                padd = input("Enter Patient Address : ")
                pdf = open("patient.data","a")          
                pdf.write(pid + ":" + pname + ":" + padd)
                pdf.write("\n")
                pdf.close()
                break
    else:
        pdf.close()
        pname = input("Enter Patient Name : ")
        padd = input("Enter Patient Address : ")
        pdf = open("patient.data","a")          
        pdf.write(pid + ":" + pname + ":" + padd)
        pdf.write("\n")
        pdf.close()
        #break
