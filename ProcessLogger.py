def ProcessDisplay(path):

    if not os.path.exists(path):
        os.mkdir(path);
  
    filename = os.path.join(path,"log%s.txt"%time.ctime());
    
    fobj = open(filename,"w");
    
    line = "-"*44;
    
    fobj.write(line +"\n");
    fobj.write("Marvellous Process Logger at : %s\n"%time.ctime());
    fobj.write(line +"\n");
    
    for pobj in psutil.process_iter():
        fobj.write(str(pobj));

    fobj.close();

def main():
    schedule.every(1).minute.do(ProcessDisplay,path = sys.argv[1]);

    while True :
         schedule.run_pending();
         time.sleep(1);

if __name__ == "__main__":
    main(); 
