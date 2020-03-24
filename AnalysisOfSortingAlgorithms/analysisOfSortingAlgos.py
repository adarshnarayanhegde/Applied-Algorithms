#Sorting Algorithms
import time
import os
import matplotlib.pyplot as plt

size = [5000,10000,15000,20000,25000,30000]

#Insertion sort
def insertionsort(numbers):
        print("Running Insertion Sort")
        startTime = time.time()
        for j in range(1, len(numbers)):
                key = numbers[j]
                i = j-1
                while i >=0 and numbers[i] > key :
                        numbers[i+1] = numbers[i]
                        i = i-1
                numbers[i+1] = key
        endTime = time.time()
        return numbers,endTime-startTime

#Selection Sort
def selectionsort(numbers):
        print("Running Selection Sort")
        startTime = time.time()
        end = len(numbers)
        for i in range(len(numbers)-1):
                index = i
                list = numbers[index:end]
                mini = numbers.index(min(list))
                numbers[index],numbers[mini] = numbers[mini],numbers[index]
        endTime = time.time()
        return numbers,endTime-startTime

#Converting string to list
def convert_to_list(resString):
        res = list(resString.split(","))
        for i in range(len(res)):
                res[i] = int(res[i])
        return res

#Converting list to string
def convert_to_string(plot):
        res = ','.join([str(i) for i in plot])   #This line is referred from stackoverflow
        return res

timeList = []
timeInsertion = {}
timeSelection = {}
def sort(plot,out,file):
        loc_in = plot+"/"+file
        fileOb = open(loc_in,"r")
        inpString = fileOb.read()
        fileOb.close()

        inpList= convert_to_list(inpString)
        #Calling sorting algorithms on the input data
        ins_list=list(inpList)
        result_insert,time_taken_insert=insertionsort(ins_list)
        print("Time taken by Insertion Sort for file %s: " %(file),time_taken_insert)
        sel_list=list(inpList)
        result_select,time_taken_select=selectionsort(sel_list)
        print("Time taken by Selection Sort for file %s: " %(file),time_taken_select)

        #Storing time data in respective dictionaries
        timeInsertion.update({file:time_taken_insert})
        timeSelection.update({file:time_taken_select})

        #Writing sorted output onto a file
        str_insert=convert_to_string(result_insert)
        str_select=convert_to_string(result_select)
        loc_out= out+"/"+file+"_output.txt"
        fileObject = open(loc_out,"w")
        fileObject.write("\nInsertion Sort: ")
        fileObject.write(str_insert)
        fileObject.write("\n\nRun Time: "+str(time_taken_insert))
        fileObject.write("\n\n\n\nSelection Sort: ")
        fileObject.write(str_select)
        fileObject.write("\n\nRun Time: "+str(time_taken_select))
        fileObject.close()

#Function to return list of files in a directory
def fileList(path):
        filelist = []
        for f in os.listdir(path):
                if not f.startswith('.'):
                        filelist.append(f)
        filelist.sort()
        return filelist

#Function to plot graph (This function is referred from GeeksForGeeks)
def plotGraph(size,insert,select):
        plt.plot(size,insert, label="Inesrtion Sort")
        plt.plot(size,select, label="Selection Sort")
        plt.xlabel('Input Size')
        plt.ylabel('Time taken')
        plt.title('Insertion Sort VS Selection Sort for Plot %d'%(plot) )
        plt.legend()
        plt.show()

#Function to calculate average time values
def avgTime(times):
        avg_time=[]
        buf=0
        for i in range(0,len(times),3):
            a=i
            for j in range(3):
                    buf+=times[a]
                    a=a+1
            avg=buf/3
            avg_time.append(avg)
            buf=0
        return avg_time


plot = int(input("Enter plot number (1/2/3/4/5): "))
#Fetching input files and sorting
if plot is 1:
        path=os.getcwd() +"/plot1/input"
        filelist = fileList(path)
        plot1_dir_in = os.path.join(os.getcwd(),"plot1/input")
        plot1_dir_out = os.path.join(os.getcwd(),"plot1/output")
        for file in filelist:
                sort(plot1_dir_in,plot1_dir_out,file)

elif plot is 2:
        path=os.getcwd() +"/plot2/input"
        filelist = fileList(path)
        plot2_dir_in = os.path.join(os.getcwd(),"plot2/input")
        plot2_dir_out = os.path.join(os.getcwd(),"plot2/output")
        for file in filelist:
                sort(plot2_dir_in,plot2_dir_out,file)

elif plot is 3:
        path=os.getcwd() +"/plot3/input"
        filelist = fileList(path)
        plot3_dir_in = os.path.join(os.getcwd(),"plot3/input")
        plot3_dir_out = os.path.join(os.getcwd(),"plot3/output")
        for file in filelist:
                sort(plot3_dir_in,plot3_dir_out,file)

elif plot is 4:
        path=os.getcwd() +"/plot4/input"
        filelist = fileList(path)
        plot4_dir_in = os.path.join(os.getcwd(),"plot4/input")
        plot4_dir_out = os.path.join(os.getcwd(),"plot4/output")
        for file in filelist:
                sort(plot4_dir_in,plot4_dir_out,file)

else:
        path=os.getcwd() +"/plot5/input"
        filelist = fileList(path)
        plot5_dir_in = os.path.join(os.getcwd(),"plot5/input")
        plot5_dir_out = os.path.join(os.getcwd(),"plot5/output")
        for file in filelist:
                sort(plot5_dir_in,plot5_dir_out,file)


#Plotting graph for the inputs
if plot in (1,4):
        buf = 0
        avg = 0
        insert_t = list(timeInsertion.values()) #storing dictionary values to a list
        print("insert_t",insert_t)
        insert_avg_t = avgTime(insert_t)
        select_t = list(timeSelection.values()) #storing dictionary values to a list
        select_avg_t = avgTime(select_t)
        print("Average time for insertion sort: ",insert_avg_t)
        print("Average time for selection sort: ",select_avg_t)
        plotGraph(size,insert_avg_t,select_avg_t)

if plot in (2,3):
        insert_t = list(timeInsertion.values())
        select_t = list(timeSelection.values())
        print("Time taken by insertion sort: ",insert_t)
        print("Time taken by selection sort: ",select_t)
        plotGraph(size,insert_t,select_t)
