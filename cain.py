def qsort(data,low,high):
    if (high-low)<=1:
        return(data)
    temt=data[low]
    i=low
    k=low
    j=high-1
    while  not i==j:
        while i<j:
           if data[j]<temt:
               data[k]=data[j]
               k=j
               break
           else:
                j=j-1
        while i<j:
            if data[i]>temt:
                data[k]=data[i]
                k=i
                break
            else:
                i=i+1
    data[i]=temt
    qsort(data,low,i)
    qsort(data,i+1,high)

def rndlist(a,b,n):
    import random
    lst=[]
    for i in range(n):
        lst.append(random.uniform(a,b))
    return(lst)

def testtime(a,*args):
    import datetime
    stime=datetime.datetime.now()
    b=a(*args) #code
    etime=datetime.datetime.now()
    print(etime-stime)

def test1():
    import datetime
    a=rndlist(0,1,1000000)
    stime=datetime.datetime.now()
    a.sort()
    etime=datetime.datetime.now()
    return(etime-stime)

