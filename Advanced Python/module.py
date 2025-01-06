def func():
        print("Hello World")
func()

print(__name__) # it will give __main__ means it is running from module program only
#__name=="__main__" is used so that the inner will be executed only if the same function excuted but 
#not when imported function runs
if __name__=="__main__":
    def func():
        print("Hi i am excuted only if u run module.py")
    func()

    
