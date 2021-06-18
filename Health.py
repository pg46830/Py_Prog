def getdate():
    import datetime
    return datetime.datetime.now()
def getdata(x):
    with open(x,'r') as f:
        print(f.readlines())
def setdata(x):
    with open(x,'a') as f:
        f.write(f"{getdate()},{y}")
if __name__=='__main__':
    a=int(input('''1.Retrieve Data
2.Lock Data\n'''))
    b=int(input('''1.Rohit
2.Hamid
3.Suresh\n'''))
    c=int(input('''1.Excercise
2.Food\n'''))
    if a==2:
        if b==1:
            if c==1:
                y=input('Which Exercise you done Rohit')
                setdata('rt_exe.txt')
            elif c==2:
                y=input('Which food you eat Rohit')
                setdata('rt_fd.txt')
            else:
                print('You entered wrong choice')
        elif b==2:
            if c==1:
                y=input('Which Exercise you done Hamid')
                setdata('hm_exe.txt')
            elif c==2:
                y=input('Which food you eat Hamid')
                setdata('hm_fd.txt')
            else:
                print('You entered wrong choice')
        elif b==3:
            if c==1:
                y=input('Which Exercise you done Suresh')
                setdata('sr_exe.txt')
            elif c==2:
                y=input('Which food you eat Suresh')
                setdata('sr_fd.txt')
            else:
                print('You entered wrong choice')
        else:
            print('You entered wrong choice')
    elif a==1:
        if b==1:
            if c==1:
                getdata('rt.exe.txt')
            elif c==2:
                getdata('rt_fd.txt')
            else:
                print('You entered wrong choice')
        elif b==2:
            if c==1:
                getdata('hm_exe.txt')
            elif c==2:
                getdata('hm_fd.txt')
            else:
                print('You entered wrong choice')
        elif b==3:
            if c==1:
                getdata('sr_exe.txt')
            elif c==2:
                getdata('sr_fd.txt')
            else:
                print('You entered wrong choice')
        else:
            print("You entered wrong choice")
    else:
        print('You entered wrong choice')