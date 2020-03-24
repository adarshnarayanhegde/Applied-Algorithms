import operator

def computeMaxWeight(input):
    #reading input from the file
    fd=open(input,'r')
    input_jobs=fd.read()
    fd.close()

    #storing jobs with their start-time, finish-time and weight
    jobs = list(input_jobs.split("\n"))
    for i in range(len(jobs)-1):
        jobs[i]=jobs[i].split(' ')

    #removing last empty line
    del jobs[-1]

    #converting values stored as string to int
    for i in range(len(jobs)):
        jobs[i]=list(map(int,jobs[i]))

    #sorting jobs by their finish time
    jobs=sorted(jobs,key=operator.itemgetter(1))

    #storing weights of each jobs in a list
    weight=[]
    for i in range(len(jobs)):
        weight.append(jobs[i][2])

    #for each jobs calculating the compatible job which has the largest index. i.e. index of the most recent compatible job
    print("Computing indices of most recent compatible job for the input '%s'..."%input)
    recent_comp_job=[-1]*len(jobs)
    for i in range(0,len(jobs)):
        for j in range(i-1,-1,-1): #searching from previous job for compatibility
            if jobs[j][1]<=jobs[i][0]:
                recent_comp_job[i]=j
                break

    #initializing max_weight for each jobs with 0
    max_weight=[0]*len(jobs)

    print("Computing maximum weight...")
    #for all the jobs comparing (weight of current job + max_weight of recent compatible job) and the previous job's max_weight
    for j in range(len(jobs)):
        max_weight[j]=max((weight[j]+max_weight[recent_comp_job[j]]),max_weight[j-1])

    print("Maximum weight for the input '%s' is: "%input,max(max_weight))
    print("\n")

#computing maximum weight for 'input1.txt'
computeMaxWeight('input1.txt')
#computing maximum weight for 'input2.txt'
computeMaxWeight('input2.txt')
