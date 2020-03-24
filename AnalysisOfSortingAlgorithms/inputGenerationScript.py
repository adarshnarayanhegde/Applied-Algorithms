# Random number generation onto a file
import random
import os

#Random number generation
def generate_random(size,start,end):
        numbers = []
        for index in range(size):
                numbers.append(random.randint(start,end))
        return numbers

#Input generation for plot5
def generate_random_plot5(size,seq,start,end):
        numbers=[]
        for i in range(seq):
                for j in range(size):
                        numbers.append(random.randint(start,end)) #Generating 100,000 sequences of length 50 each
        return numbers

#Converting list to string
def convert_to_string(plot2):
        res = ','.join([str(i) for i in plot2])   #from stackoverflow // https://stackoverflow.com/questions/438684/how-to-convert-a-list-of-longs-into-a-comma-separated-string-in-python
        return res


size = [5000,10000,15000,20000,25000,30000]
plot = int(input("Enter plot number (1/2/3/4/5): "))
if plot not in (1,2,3,4,5):
        print("Please enter valid plot number")
        exit(0)

#Plot1 file generation
if plot is 1:
        plot1_dir = os.path.join(os.getcwd(),"plot1/input")
        if not os.path.exists(plot1_dir):
                os.mkdir(plot1_dir)
        for s in size:
                start = 1
                end = s
                for i in range(3):
                        numberlist = generate_random(s,start,end)
                        plot1 = numberlist
                        plot1_str=convert_to_string(plot1)
                        if s is 5000:
                                filename = "plot1_0" + str(s) + "_" + str(i)+".txt"
                        else:
                                filename = "plot1_" + str(s) + "_" + str(i)+".txt"
                        filepath = os.path.join(plot1_dir,filename)
                        fileObject = open(filepath,"w")
                        fileObject.write(plot1_str)
                        fileObject.close()
        print("Plot1 files successfully generated")

#Plot2 file generation
elif plot is 2:
        plot2_dir = os.path.join(os.getcwd(),"plot2/input")
        if not os.path.exists(plot2_dir):
                os.mkdir(plot2_dir)
        for s in size:
                start = 1
                end = s
                numberlist = generate_random(s,start,end)
                numberlist.sort()
                plot2 = numberlist
                plot2_str=convert_to_string(plot2)
                if s==5000:
                        filename = "plot2_0" + str(s)+".txt"
                else:
                        filename = "plot2_" + str(s)+".txt"
                filepath = os.path.join(plot2_dir,filename)
                fileObject = open(filepath,"w")
                fileObject.write(plot2_str)
                fileObject.close()
        print("Plot2 files successfully generated")

#Plot3 file generation
elif plot is 3:
        plot3_dir = os.path.join(os.getcwd(),"plot3/input")
        if not os.path.exists(plot3_dir):
                os.mkdir(plot3_dir)
        for s in size:
                start = 1
                end = s
                numberlist = generate_random(s,start,end)
                numberlist.sort(reverse = True)
                plot3 = numberlist
                plot3_str=convert_to_string(plot3)
                if s==5000:
                        filename = "plot3_0" + str(s)+".txt"
                else:
                        filename = "plot3_" + str(s)+".txt"
                filepath = os.path.join(plot3_dir,filename)
                fileObject = open(filepath,"w")
                fileObject.write(plot3_str)
                fileObject.close()
        print("Plot3 files successfully generated")

#Plot4 file generation
elif plot is 4:
        plot4_dir = os.path.join(os.getcwd(),"plot4/input")
        if not os.path.exists(plot4_dir):
                os.mkdir(plot4_dir)
        for s in size:
                start = 1
                end = s
                for a in range(3):
                        numberlist = generate_random(s,start,end)
                        numberlist.sort()
                        for i in range(50):
                                i = random.randint(1,s)
                                j = random.randint(1,s)
                                numberlist[i],numberlist[j] = numberlist[j], numberlist[i]

                        plot4 = numberlist
                        plot4_str=convert_to_string(plot4)
                        if s is 5000:
                                filename = "plot4_0" + str(s) + "_" + str(a)+".txt"
                        else:
                                filename = "plot4_" + str(s) + "_" + str(a)+".txt"
                        filepath = os.path.join(plot4_dir,filename)
                        fileObject = open(filepath,"w")
                        fileObject.write(plot4_str)
                        fileObject.close()
        print("Plot4 files successfully generated")

#Plot5 file generation
else:
        plot5_dir = os.path.join(os.getcwd(),"plot5/input")
        if not os.path.exists(plot5_dir):
                os.mkdir(plot5_dir)
        start = 1
        end= 50
        size=50
        seq=100000
        numberlist = generate_random_plot5(size,seq,start,end)
        plot5 = numberlist
        plot5_str=convert_to_string(plot5)
        filename = "plot5_" + "100000.txt"
        filepath = os.path.join(plot5_dir,filename)
        fileObject = open(filepath,"w")
        fileObject.write(plot5_str)
        fileObject.close()
        print("Plot5 files successfully generated")
