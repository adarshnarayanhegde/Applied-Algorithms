#Sorting Algorithms
import time
import os
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.setrecursionlimit(100000)
size = [5000,10000,15000,20000,25000,30000]

#Insertion sort
def insertionsort(numbers):
        #print("Running Insertion Sort")
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


def mergesort(a):
    startTime = time.time()
    if len(a) >1:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]
        mergesort(left)
        mergesort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i+=1
            else:
                a[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            a[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            a[k] = right[j]
            j+=1
            k+=1
            endTime = time.time()
    return a,endTime-startTime

#Quick sort
def partition(a,p,r):
    pivot=a[r]
    i=p-1

    for j in range(p,r):
        if a[j]<=pivot:
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[r]=a[r],a[i+1]
    return i+1

def quicksort(a,p,r):
    startTime = time.time()
    if p<r:
        q=partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)
    endTime = time.time()
    return a,endTime-startTime

#Converting string to list
def convert_to_list(resString):
        res = list(resString.split(","))
        for i in range(len(res)):
                res[i] = int(res[i])
        return res

#Storing input-5 in an array of shape <100000,50>. i.e. 100000 sequences of length 50 each
def convert_to_list_plot5(resString):
        res = np.asarray(resString.split(","))
        for i in range(len(res)):
                res[i] = int(res[i])
        res=np.reshape(res,(100000,50)).astype(int)
        return res

#Converting list to string
def convert_to_string(plot):
        res = ','.join([str(i) for i in plot])   #This line is referred from stackoverflow
        return res

timeList = []
timeInsertion = {}
timeMerge = {}
timeQuick = {}
def sort(plot,out,file):
    loc_in = plot+"/"+file
    fileOb = open(loc_in,"r")
    inpString = fileOb.read()
    fileOb.close()
    f=0
    #Checking if the input type is input-5 and gathering input in an array
    if plot == os.path.join(os.getcwd(),"plot5/input"):
        inpList= convert_to_list_plot5(inpString)
        f=1
    else:
        inpList= convert_to_list(inpString)
        f=0

    #Calling sorting algorithms on the input data
    if(f==0): #if input type is not input-5
        ins_list=list(inpList)
        print("\n\nRunning Insertion Sort...")
        result_insert,time_taken_insert=insertionsort(ins_list)
        print("Time taken by Insertion Sort on file %s: " %(file),time_taken_insert)

        mer_list=list(inpList)
        print("\n\nRunning Merge Sort...")
        result_merge,time_taken_merge=mergesort(mer_list)
        print("Time taken by Merge Sort on file %s: " %(file),time_taken_merge)

        qck_list=list(inpList)
        l=len(qck_list)
        print("\n\nRunning Quick Sort...")
        result_quick,time_taken_quick=quicksort(qck_list,0,l-1)
        print("Time taken by Quick Sort on file %s: " %(file),time_taken_quick)

    else:#if input type is input-5
        res_ins=[]
        res_mer=[]
        res_qck=[]
        ins_list=list(inpList)
        print(inpList)
        print("\n\nRunning Insertion Sort...")
        t_ip5_st=time.time()
        print("starting time for insertion:",t_ip5_st)
        for i in range(len(ins_list)):
            result_insert,time_taken_insert=insertionsort(ins_list[i])
            res_ins.append(result_insert)
        t_ip5_end=time.time()
        print("ending time for insertion:",t_ip5_end)
        time_taken_insert=t_ip5_end-t_ip5_st
        print("Time taken by Insertion Sort on file %s: " %(file),time_taken_insert)

        mer_list=list(inpList)
        print(inpList)
        print("\n\nRunning Merge Sort...")
        t_ip5_st=time.time()
        print("starting time for merge:",t_ip5_st)
        for i in range(len(mer_list)):
            result_merge,time_taken_merge=mergesort(mer_list[i])
            res_mer.append(result_merge)
        t_ip5_end=time.time()
        print("ending time for merge:",t_ip5_end)
        time_taken_merge=t_ip5_end-t_ip5_st
        print("Time taken by Merge Sort on file %s: " %(file),time_taken_merge)

        qck_list=list(inpList)
        l=len(qck_list)
        print(inpList)
        print("\n\nRunning Quick Sort...")
        t_ip5_st=time.time()
        print("starting time for quick:",t_ip5_st)
        for i in range(len(qck_list)):
            result_quick,time_taken_qiuck=mergesort(qck_list[i])
            res_qck.append(result_quick)
        t_ip5_end=time.time()
        print("ending time for quick:",t_ip5_end)
        time_taken_quick=t_ip5_end-t_ip5_st
        print("Time taken by Quick Sort on file %s: " %(file),time_taken_quick)


    #Storing time data in respective dictionaries
    timeInsertion.update({file:time_taken_insert})
    timeMerge.update({file:time_taken_merge})
    timeQuick.update({file:time_taken_quick})

    #Writing sorted output onto a file
    if f==0:
        str_insert=convert_to_string(result_insert)
        str_merge=convert_to_string(result_merge)
        str_quick=convert_to_string(result_quick)
    else:
        str_insert=convert_to_string(res_ins)
        str_merge=convert_to_string(res_mer)
        str_quick=convert_to_string(res_qck)

    loc_out= out+"/"+"output_"+file
    fileObject = open(loc_out,"w")
    fileObject.write("\nInsertion Sort: ")
    fileObject.write(str_insert)
    fileObject.write("\n\nRun Time: "+str(time_taken_insert))
    fileObject.write("\n\n\n\nMerge Sort: ")
    fileObject.write(str_merge)
    fileObject.write("\n\nRun Time: "+str(time_taken_merge))
    fileObject.write("\n\n\n\nQuick Sort: ")
    fileObject.write(str_quick)
    fileObject.write("\n\nRun Time: "+str(time_taken_quick))
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
def plotGraph(size,insert,merge,quick):
        plt.plot(size,insert, label="Inesrtion Sort")
        plt.plot(size,merge, label="Merge Sort")
        plt.plot(size,quick, label="Quick Sort")
        plt.xlabel('Input Size')
        plt.ylabel('Time taken')
        plt.title('Insertion Sort VS Merge Sort VS Deterministic Quick Sort, for Input: %d'%(plot) )
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
        insert_avg_t = avgTime(insert_t)
        merge_t = list(timeMerge.values()) #storing dictionary values to a list
        merge_avg_t = avgTime(merge_t)
        quick_t = list(timeQuick.values()) #storing dictionary values to a list
        quick_avg_t = avgTime(quick_t)
        print("Average time for Insertion Sort: ",insert_avg_t)
        print("Average time for Merge Sort: ",merge_avg_t)
        print("Average time for Quick Sort: ",quick_avg_t)
        plotGraph(size,insert_avg_t,merge_avg_t,quick_avg_t)

if plot in (2,3):
        insert_t = list(timeInsertion.values())
        merge_t = list(timeMerge.values())
        quick_t = list(timeQuick.values())
        print("Time taken by Insertion Sort: ",insert_t)
        print("Time taken by Merge Sort: ",merge_t)
        print("Time taken by Quick Sort: ",quick_t)
        plotGraph(size,insert_t,merge_t,quick_t)

