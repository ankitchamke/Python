with open("log.txt" , encoding="utf-8", errors="replace") as f:
    data = f.read()
    
if("python" in data):
    print("present")
else:
    print("not present")