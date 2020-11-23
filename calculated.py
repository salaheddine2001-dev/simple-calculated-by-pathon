#start function to welcome
def start():
    print("#"*40)
    print("welcome in simple calculated ! !")
    print("#"*40)
#cal the start function
start()

#function to calculated any equation
def  cal():
    try:
        print(float(eval(input("write the calculated :"))))
    except:
        print("error please enter valid Numbers :")
#cal the function in inside the infinite loop
while True:
    cal()