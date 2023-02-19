import subprocess #สำหรับ รัน terminal command

if __name__ == "__main__":
    ## basic
    # subprocess.run(["ls","-ltr"])
    # subprocess.run(["python","python_script101.py","--x","8"])

    ## use output of subprocess
    # process1 = subprocess.Popen(["python","python_script101.py","--x","6"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # out, err = process1.communicate()
    # print(out.decode('utf-8'))

    sumxt = 0
    count = 0 

    for x in range(1,100):

        if x % 2 != 0:
            count +=1

            print(f'<>'*10)
            print(f'This is number {x}')

            process = subprocess.Popen(["python","python_script101.py","--x",f"{x}"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)    
            out, err = process.communicate()
            print(out.decode('utf-8'))

            sum = (x*2)
            sumxt += (x*2)
            print(f'This is round {count}')
            print(f'sum of {x} is = {sum}')
            print(f'sum total is {sumxt}')
            print(f'--'*10)

    print(f'=='*10)
    print(f'SUM of XT ={sumxt}')
    print(f'=='*10)

#สั่งรัน python_script101.py 50 รอบ โดย x = 1,3,5,7....99 แล้วให้เอา output ของ xt มารวมกันแล้วปริ้นออกมา