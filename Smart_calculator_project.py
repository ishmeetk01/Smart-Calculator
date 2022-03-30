responses=["Welcome to smart calculator","My name is smarty","Thank You"]
def extract_numbers(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
            
        except ValueError:
            pass
    return(l)
def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1
def big(a,b):
    return a if a>b else b
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def myname():
    print("My name is Smarty")
def end():
    print(responses[2])
    print("Enter enter key to exit")
    exit()
def help():
    print("List of valid commands")
    for k in operations:
        print(k)
    for k in commands:
        print(k)

operations={"ADD":add,"ADDITION":add,"PLUS":add,"MULTIPLY":multiply,"MINUS":sub,"SUBTRACT":sub,"SUB":sub,"LCM":lcm,"HCF":hcf,"GREATER":big,"BIG":big}
commands={"NAME":myname,"END":end,"EXIT":end,"CLOSE":end,"HELP":help}
def main():
    
    print(responses[0])
    print(responses[1])
    while True:
        text=input("Enter text: ")
        for word in text.split(' '):
            if word.upper() in operations.keys():
                try:
                    
                    l=extract_numbers(text)
                    result=operations[word.upper()](l[0],l[1])
                    print(result)
                except:
                     print("Something is wrong please retry")
                finally:
                    break
            elif word.upper() in commands.keys():
                commands[word.upper()]()
                break
    else:
        print("Sorry")
if __name__=="__main__":
    main()
                
            
    
    
            
            
            
