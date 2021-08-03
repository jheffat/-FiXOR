from os import system, name, path
import glob, platform,re
from datetime import date
from json import loads
from random import random
from sys import exit, argv,stdout
import progressbar,keyboard
from time import sleep
def isbyte(fdata):
    try:
        fdata.decode("utf-8")
        return False
    except (UnicodeDecodeError, AttributeError):
        return True
def keypress(key):
    k=0
    while k==0:
        k=keyboard.is_pressed(chr(key))
    return
def ValidPass(Passwd):
    errx=[]
    if Passwd=="q" or Passwd=="Q":return errx
    if 8<=len(Passwd)<=16:
        if not re.search("[0-9]",Passwd):errx+=["At least one Number"]
        if not re.search("[A-Z]",Passwd):errx+=["At least one Upper case"]
        if not re.search("[a-z]",Passwd):errx+=["At least one Lower case"]
        if not re.search("[@#$!]",Passwd):errx+=["At least one Special char: @#$!"]     
    else: errx+=["Must be at least 8 or more Characters, max 16"]
    return errx

def Filehandle(Filename):
    rf=open(Filename,"rb")
    fd=rf.read()
    rf.close
    return fd

def isencrypted(fname):
    rin=open(fname,"rb");donex="";doney=""
    headx=encode("".join(list(map(chr,rin.read(200)))))
    rin.close
    if '"tox":"!CDXY"' in headx:
        donex= [headx[0:x+1] for x in range(len(headx)) if headx[x]=="}"][0]
        doney=loads(donex)
    return doney,donex 
def encode(msg):
    Pass_char="Encryptoxby!c0d3x!s";n=0;msgx=""
    for x in msg:
        msgx+=chr(ord(x) ^ (256-ord(Pass_char[n])))      
        n=n+1 
        if(n== len(Pass_char)):  n=0   
    return msgx      
def intro():
    _ = system('cls')
    print("""◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼
  ______ ___   ______  _____        🌍: www.icodexys.com
 |  ____(_) \ / / __ \|  __ \       📧: iCodexys@gmail.com
 | |__   _ \ V / |  | | |__) |      🔨: Jheff Alberty
 |  __| | | > <| |  | |  _  /       📜: GNU General Public License v3.0
 | |    | |/ . \ |__| | | \ \ 
 |_|    |_/_/ \_\____/|_|  \_\      📊Version: 1.0  (10/28/2020) 
 ◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼""" )                                                     
Password="";n=0;targets=[];op="";banfilels=[];sucessed=[];notsucessed=[];barx=0;txt=stdout;cryptdata=bytearray()

if len(argv)<=2:
    intro()
    print("Encrypt your files with this tool.")
    print("USAGE: Fixor OPTION TARGET")
    print("TARGET---> Path\Filename\*.*")
    print("OPTION---> -e for encrypt, -d for decrypt and -i for file details\n")
    print("Example: fixor -e mydiary.txt")
    sleep(3)
    exit()
#needs work--------------------------------------
if "*" not in argv[2]:
    if path.exists(argv[2])==False:
        exit("❌Invalid path\Filename...")
 
targets=glob.glob(argv[2])
optionx=argv[1]
#-------------------------------------------------------
if optionx=="-i":
    intro()  
    print("\nFILES ENCRYPTED DETAILS","▒"*80,"\n")
    for xc in targets:
        if len(isencrypted(xc)[0])>0:
            idinfo=isencrypted(xc)[0]
            print("[✔️"+xc+"]","_"*60)
            print("■📄Original Filename:",idinfo["file"])
            print("■📐Size:",idinfo["size"],"Bytes")
            print("■📆Date Encrypted:",idinfo["date"])
            print("■💻OS:",idinfo["os"],"\n")  
        else:
            print("[❌"+xc+"] ", "is not encrypted.\n")
    if len(targets)==0:exit("***Canceled process, files not found***")
if optionx=="-e":
    intro()   
    print("\nTARGET'S LIST","▒"*80,"\n")
    for xc in targets:     
        if len(isencrypted(xc)[0])>0:
            filemsg=">>> Is already encrypted, removed from the target's list..."
            banfilels+=[xc];emoj="❌"
        else: filemsg="";emoj="✔️"
        print("|FILE:["+emoj+ "📄 "+xc+"] "+filemsg)
    for xc in banfilels:
        targets.remove(xc)
    if len(targets)==0:exit("***Canceled process, no files to encrypt***")
    print("\n|ENCRYPTION PROCESS....")
    print("|",len(targets),"Files will be encrypted.\n")
    print("Type a password to encrypt the Target's List")
    print("Type 'q' or press CTRL+Z to CANCEL\n")   
    state=["0"]
    while state!=[]:
        Password=input("|🗝️PASSWORD:")
        state=ValidPass(Password)      
        if len(state)> 0:
            for x in range(len(state)):
                print("🚫: "+state[x])
    if Password=="q" or Password=="Q":exit("***Canceled process...***")
    lp=len(Password)
    lentarg=len(targets)
    intro()
    print("|☢️ Forgetting your password means that you will lose your encrypted data forever. ")
    print("Avoid that headache, there is a possibility of recovering the key with a charge. ")
    print("Go to www.icodexys.com/getmylostpassword/ for details....")
    print("Press [ENTER] to Continue or [CTRL+Z] to Cancel the process...")
    keypress(13)
    for Filename in targets:     
        try:
            lensuc=len(sucessed)
            perc=int(((lensuc)/lentarg)*100)
            intro()
            print("\n|ENCRYPTION PROCESS","▒"*80)  
            print("\n|Total Files Encrypted:",lensuc," of ",lentarg)
            txt.write("[%s]" % (" " * (101)))
            txt.write("%"+str(perc))
            txt.write("\b" * (100+4)) 
            txt.write("█"*perc)
            print("\n|Encrypting: 📝[ "+Filename+" ]...")  
            txt.flush()          
            fdata=Filehandle(Filename)
            Fsize=len(fdata)
            if isbyte(fdata)==True:
                ldata=(int(Fsize*0.25))
                fdt1=bytes(fdata[:ldata])
                fdt2=bytes(fdata[ldata:])
            else:
                ldata=(Fsize)
                fdt1=bytes(fdata[:ldata])
                fdt2=""
            Fout=open(Filename,"wb+")
            Fout.write(bytes(list(map(ord,encode('{"tox":"!CDXY","file":"'+Filename+'","size":"'+str(Fsize)+'","date":"'+str(date.today())+'","pass":"'+Password+'","os":"'+platform.system()+" "+platform.release()+'"}')))))
            bar = progressbar.ProgressBar(maxval=ldata, widgets=[progressbar.Bar('█', '[', ']'), ' ', progressbar.Percentage()])
            bar.start()
            for b in fdt1:     
                bar.update(barx)     
                barx+=1   
                cryptdata+=bytes([(b^int(256-ord(Password[n])))])
                n+=1
                if(n == lp):
                    n=0;     
            Fout.write(cryptdata)
            if len(fdt2)>0:
                Fout.write(fdt2)
            barx=0
            cryptdata=bytearray()
            bar.finish()
            Fout.close
            sucessed+=[Filename]
        except IOError as errz:
            print ("\n🚫",errz, " [Press enter]")
            keypress(13)
            notsucessed+=[Filename]
    if len(sucessed)>0: 
        intro()
        print("\n|DONE ENCRYPTING...😃\n")
        print("✔️Encrypted:",len(sucessed),"Files ", "❌Error:",len(notsucessed),"Files\n")
        l=open("Encryptox.log","a")
        l.write("***FILES ENCRYPTED ON "+str(date.today())+"\n")
        for f in sucessed:
            l.write("==>"+f+"\n") 
        if len(notsucessed)>0:
            l.write("***FAILED TO ENCRYPT ON "+str(date.today())+"\n")
            for f in notsucessed:
                l.write("==>"+f+"\n")
        l.close()
        print("|📋 Check file Encryptox.log to see more details....")
        exit("Done!") 
if optionx=="-d":
    intro()  
    print("\nTARGET'S LIST","▒"*80,"\n")
    for xc in targets:
        if len(isencrypted(xc)[0])>0:
            filemsg="";emoj="✔️"
        else: 
            filemsg=">>> Is not encrypted & removed from the target's list";
            emoj="❌";banfilels+=[xc]
        print("|FILE:["+emoj+ "📄 "+xc+"] "+filemsg)
    for xc in banfilels:
        targets.remove(xc) 
    if len(targets)==0:exit("***Canceled process, no files to decrypt***")
    print("\n|DECRYPTION PROCESS...")
    print("|",len(targets),"Files will be decrypted.\n")
    print("Type a password to decrypt the Target's List")
    print("type 'q' or press CTRL+Z to CANCEL\n")   
    state=["0"]
    while state!=[]:
        Password=input("🗝️PASSWORD:")
        state=ValidPass(Password)      
        if len(state)> 0:
            for x in range(len(state)):
                print("🚫: "+state[x])
    if Password=="q" or Password=="Q":exit("Canceled process...")
    lp=len(Password)
    lentarg=len(targets)
    for Filename in targets:
        headinfo=isencrypted(Filename)[0]
        headlen=len(isencrypted(Filename)[1])
        if headinfo["pass"] ==Password:        
            try:
                lensuc=len(sucessed)
                perc=int(((lensuc)/lentarg)*100)
                intro()
                print("\n|DECRYPTION PROCESS","▒"*80) 
                print("\n|Total Files Decrypted:",lensuc," of ",lentarg)
                txt.write("[%s]" % (" " * (101)))
                txt.write("%"+str(perc))
                txt.write("\b" * (100+4)) 
                txt.write("█"*perc)
                print("\n|Dencrypting: 📝[ "+Filename+" ]...")                                            
                txt.flush()
                fdata=Filehandle(Filename)[headlen:]
                Fsize=len(fdata)
                if isbyte(fdata)==True:
                    ldata=(int(Fsize*0.25))
                    fdt1=bytes(fdata[:ldata])
                    fdt2=bytes(fdata[ldata:])
                else:
                    ldata=(Fsize)
                    fdt1=bytes(fdata[:ldata])
                    fdt2=""
                Fout=open(headinfo["file"],"wb+")
                bar = progressbar.ProgressBar(maxval=ldata, widgets=[progressbar.Bar('█', '[', ']'), ' ', progressbar.Percentage()]) 
                bar.start()
                for b in fdt1:
                    bar.update(barx)
                    barx+=1  
                    cryptdata+=bytes([(b^int(256-ord(Password[n])))])
                    n=n+1 
                    if(n== len(Password)):                   
                        n=0;                 
                Fout.write(cryptdata)
                if len(fdt2)>0:
                    Fout.write(fdt2)
                bar.finish()
                barx=0
                cryptdata=bytearray()
                Fout.close
                sucessed+=[Filename]
            except IOError as Errz:
                print ("🚫",Errz, " [Press enter]")
                keypress(13)
                notsucessed+=[Filename]
        else:
            print("❌Your password is invalid for this file:",Filename)
            print("Press [ENTER] to Continue...")
            keypress(13)
            notsucessed+=[Filename]
    if len(sucessed)>0: 
        intro()
        print("\n|DONE DECRYPTING...😃\n")
        print("✔️Decrypted:",len(sucessed),"Files ", "❌Error:",len(notsucessed),"Files\n")
        l=open("Decryptox.log","a")
        l.write("***FILES DECRYPTED ON "+str(date.today())+"\n")
        for f in sucessed:
            l.write("==>"+f+"\n")
        if len(notsucessed)>0:
            l.write("\n***FAILED TO DECRYPT ON "+str(date.today())+"\n")
            for f in notsucessed:
                l.write("==>"+f+"\n")
        l.close()
        print("|📋 Check Decryptox.log to see more details")
        exit("Done!") 
      

#Developed by Jheff Mat(iCODEXYS) 10/28/2020
