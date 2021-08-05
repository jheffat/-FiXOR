#  -*- coding: utf-8 -*-
from shutil import copy2
from string import ascii_letters,digits
from os import system,path
from  hashlib import sha256
from tqdm import tqdm
import glob, platform,re,keyboard, bcrypt
from datetime import date, datetime
from json import loads
from random import random,randint
from sys import exit, argv
from time import sleep, time
def isZipmp3rarother(fname):
    r=Filehandle(fname,0,4)
    if r==b'Rar!' or b'PK' in r:
        r="";return 0.03
    elif b'ID3' in r:
        r="";return 0.20
    r="";return 0.02
def Fn_clear(fname):
    for c in fname:
        if c not in ascii_letters+digits+" !@#$%^&-+;.~_éáíóúñÑ":
            fname=fname.replace(c,"")        
    return fname

def gensalt(l):
    gen=""
    for _ in range(l):
        gen+="".join(chr(randint(33,254)))
    return bytes(list(map(ord,gen)))
def passhash(Pass ,Salt,Iters,kdl ):
    return bcrypt.kdf(Pass,salt=Salt,desired_key_bytes=kdl,rounds=Iters)
def checkpass(Pass,Passhashed,Salt,Iters,kdl):
    return Passhashed==bcrypt.kdf(Pass,salt=Salt,desired_key_bytes=kdl,rounds=Iters).hex()
def filesize(fname):
    f=open(fname,"rb");f.seek(0,2 );s=f.tell();f.close
    return s
def byteme(b):
    if b.isdigit():
        b=str(int(b))
        l=len(b)
        if l>=1 and l<4: exp=0;nb=" Bytes"
        if l>=4 and l<7: exp=1;nb=" KB"
        if l>=7 and l<10: exp=2;nb=" MB"
        if l>=10 and l<13: exp=3;nb=" GB"
        if l>=13 and l<16: exp=4;nb=" TB"
        if l>=16 and l<19: exp=5;nb=" PB"
        return str(round((int(b)/(1024**exp)),2))+nb
    return "Invalid digits"

def is_binary(fcontent):
    textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
    return bool(fcontent.translate(None, textchars))
def genpass():
    chars="koijQh4u@W3y1gEM2ftNRrd&BT6se5VYw7Ca8U9q0XlIZ#pA$mSOD%!cFbGPHvJxKLz";PasswordGen=""
    for x in range(14):      
        PasswordGen+=chars[int(len(chars)*random())]
    return PasswordGen
def report(mode,succ,notsuc):
    global timeprocess, rootprocess
    if mode=="1":
        termwrd=["Encryption","ENCRYPTED", "ENCRYPT"]
    else:
        termwrd=["Decryption","DECRYPTED", "DECRYPT"]

    l=open(rootprocess+"/"+termwrd[0] + ".log","a")
    l.write("***FILES "+termwrd[1]+" ON "+str(date.today())+" TIME:"+str(timeprocess)+"\n")
    l.write("***ROOT: "+rootprocess+"\n")
    for f in succ:
        l.write("==>"+f["Filename"]+ " -Verified: "+f["integrity"]+"\n")
    if len(notsuc)>0:
        l.write("***FAILED TO "+termwrd[2]+" ON "+str(date.today())+" TIME:"+str(timeprocess)+"\n")
        l.write("***ROOT: "+rootprocess+"\n")
        for f in notsuc:
            l.write("==>"+f["Filename"]+ " -Reason: "+f["error"]+"\n")
    l.close()
    print("|📋 Check file " +termwrd[0]+".log to see more details....")
    return

def keypress(key):
    keyboard.wait(key)
def ValidPass(Passwd):
    if Passwd=="q" or Passwd=="Q":return True
    if Passwd=="a" or Passwd=="A":return True
    if 8<=len(Passwd)<=16:
        if  re.search("[A-Z]",Passwd):
            if  re.search("[a-z]",Passwd): 
                if  re.search("[0-9]",Passwd): 
                    if  re.search("[@#$!%&]",Passwd):
                        return True
    return False
def inter(msg):
    N_msg=len(msg);nm=[""]*(N_msg+1)
    for y in range(N_msg):
        if y%2==0:
            nm[y+1]=msg[y]
        if y%2==1:
            nm[y-1]=msg[y]          
    nm.remove("")
    return "".join(nm)

def Filehandle(Filename,p,b):
    rf=open(Filename,"rb")
    rf.seek(p)
    fd=rf.read(b)
    rf.close
    return fd
def isencrypted (fname):
    Fs=filesize(fname)
    r=open(fname,"rb");metadata=""
    r.seek(Fs-22)
    frag_end=xor("".join(list(map(chr,r.read()))))
    if 'size":"' in frag_end:
        Size_ori="".join(re.findall("[0-9]+",frag_end)) 
        if Size_ori.isdigit(): 
            r.seek(int(Size_ori))
            metadata=xor("".join(list(map(chr,r.read())))) 
    else: 
        r.close
        return ""
    r.close
    if '"tox":"!CDXY"' in metadata: 
        return loads(metadata)
    return ""
def xor(msg):
    msgx=""
    for x in msg:
        msgx+=chr(ord(x) ^ (ord("j")) )    
    return msgx      
def intro():
    if platform.system()=='Linux':
        _ = system('clear')
    elif platform.system()=='Windows':
        _ = system("cls")
    else:
        _ = system("clear")
    print("""
  ______ ___   ______  _____        🌍: www.icodexys.com
 |  ____(_) \ / / __ \|  __ \       📧: iCodexys@gmail.com
 | |__   _ \ V / |  | | |__) |      🔨: Jheff Alberty
 |  __| | | > <| |  | |  _  /       📊: 2.11  (07/18/2021) 
 | |    | |/ . \ |__| | | \ \ 
 |_|    |_/_/ \_\____/|_|  \_\      GNU General Public License v3.0
 """ )                                                     
def warning():
    if platform.system()=='Linux':
        _ = system('clear')
    elif platform.system()=='Windows':
        _ = system("cls")
    else:
        _ = system("clear")  
    print(""" __    __                 _               _ 
/ / /\ \ \__ _ _ __ _ __ (_)_ __   __ _  / \

\ \/  \/ / _` | '__| '_ \| | '_ \ / _` |/  /
 \  /\  / (_| | |  | | | | | | | | (_| /\_/
  \/  \/ \__,_|_|  |_| |_|_|_| |_|\__, \/ 
                                  |___/""")
    print("_"*80,"|")
    print("\n|☢️| Please follow the rules & consequences of this action:")
    print("*--->Forgetting your password means that you will lose your encrypted data forever.... ")
    print("*--->During encryption, you can CANCEL the process and it will not affect files that have not reached 100%")
    print("*--->Any Password that you type or generate, make sure to write it down...Press [P] to show it.") 
    print("*--->Any action encrypt/decrypt a file, will generate a file log 'encryption.log' / 'decryption.log'....")
    print("*--->FiXOR is capable to detect if a file is encrypted or not...")
    print("*--->Also is capable to check if the password is correct or not before touch the file.")
    print("*--->By Pressing [ENTER] you are aware of your own responsibility of your data!")
    print("-"*80,"|\n")
    print
    print("Press [ENTER] to Proceed or [ESC] to Cancel the process...")
    key_p=0
    while True:
            if keyboard.is_pressed('enter'): break
            if keyboard.is_pressed('P') and key_p==0: print("--->Your Password:"+inter(Password));key_p=1    
            if keyboard.is_pressed('esc'): exit("Canceled...") 

def helpscr():
    print("\n|File Encryptor tools.\n")
    print("USAGE: Fixor OPTION TARGET | PASSWORD")
    print("TARGET---> Path\Filename\*.*")
    print("OPTION---> -e to encrypt, -d to decrypt and -s for file details")
    print("PASSWORD---> -p specify a quick password to encrypt/decrypt [OPTIONAL]\n")
    print("Example: fixor -e mydiary.txt")
    print("fixor -d c:\my downloads\handrew.jpg")
    print("fixor -e *.exe")
    print("fixor -d  *.* -p G0dl!k334#")
    sleep(2)
    exit("\nExit...\n")
Password="";n=0;targets=[];op="";banfilels=[];sucessed=[];notsucessed=[] ;lensuc=0  ;decryptdata=bytearray();encryptdata=bytearray();statuspass="";state=False ;X_integrity=0;N_integrity=0      ;esc=0 ;posbyte=0                       
timeprocess="";rootprocess=""
if len(argv)<=2:
    intro()
    helpscr()

targets=glob.glob(argv[2])

if len(targets)==0:
    intro()
    helpscr()
if len(argv)==5:
    if argv[3]=="-p":
        Password=argv[4]
optionx=argv[1]

if optionx=="-s":
    intro()  
    print("\n║FILES ENCRYPTED DETAILS╠"+"═"*100+"╣\n")
    for xc in targets:
        try:
            if filesize(xc)>50:
                if len(isencrypted(xc))>0:
                    idinfo=isencrypted(xc)
                    print("[✔️"+path.basename(xc).upper()+"]")
                    print("■📄Original Filename:",idinfo["file"])
                    print("■📐Size:",byteme(idinfo["size"]))
                    print("■⚙️Hash SHA256:",idinfo["integrity"].upper()) 
                    print("■📆Date Encrypted:",idinfo["date"])
                    print("■💻OS:",idinfo["os"],"\n")        
                else:
                    print("[❌"+path.basename(xc)+"] ", "is not encrypted.\n")
        except IOError as errz:
            print(f"[🚫{errz}\n")
            
    if len(targets)==0:exit("***<Files not found>***")

if optionx=="-e":
    intro() 
    print("\n║TARGET'S LIST╠"+"═"*100+"╣\n")
    
    for xc in targets:
        try:
            if filesize(xc)>50:
                if len(isencrypted(xc))>0:
                    filemsg=">>> Is already encrypted, removed from the target's list..."
                    banfilels+=[xc];emoj="🔐"
                else: filemsg="";emoj="✔️"
            else:
                filemsg=">>> File's size is low than 50 bytes, removed from the target's list..."
                emoj="😱";banfilels+=[xc]
            print("|FILE:["+emoj+ "📄 "+path.basename(xc)+"] "+filemsg)
        except IOError as errz:
            print(f"[🚫{errz}\n")
    for xc in banfilels:
        targets.remove(xc)
    if len(targets)==0:exit("***process canceled, no files to encrypt***")
    print("\n|",len(targets),"Files will be encrypted.\n")
    if len(Password)==0:
        print("Type a Password to encrypt the Target's List")
        print("Type 'a'+ [ENTER] to generate a Password")
        print("Type 'q'+ [ENTER] to CANCEL\n")   
        while state!=True:
            Password=input("|🗝️PASSWORD:")
            state=ValidPass(Password)      
            if state==False:
                print("""🚩  Must have at least:
                >>>🔠 One Uppercase
                >>>🔢 One Number
                >>>🔣 One Special character:#%&!$
                >>>⛓  8 Characters
                """)
        if Password.lower()=="q":exit("***process canceled...***")
        if Password.lower()=="a":
            Password=genpass()
            while ValidPass(Password)!=True:
                Password=genpass()
            print(f"-> Password generated: {Password}")
            print("Please write it down before the encryption start." )
            print("Press [ENTER] to continue...")
            keypress('enter')    
    else:
        if ValidPass(Password)==False:
            exit("""🚩Password must have at least:
    >>>🔠 One Uppercase
    >>>🔢 One Number
    >>>🔣 One Special character:#%&!$
    >>>⛓  8 Characters
Terminated...""")
        else:
            print("Press [ENTER] to start...[ESC] to cancel...")
            while True:
                if keyboard.is_pressed('enter'): break
                if keyboard.is_pressed('esc'): exit("Canceled...") 
    Password=inter(Password)
    lp=len(Password)
    Salt=gensalt(16).hex()
    Pass_hashed=Salt+passhash(Password.encode() ,Salt.encode(),100,32).hex()
    lentarg=len(targets) 
    warning() 
    print("| Starting...")
    timeprocess=datetime.now().strftime("%H:%M:%S")
    rootprocess=path.dirname(targets[0])
    for Filename in targets:  
        try:
            Fsize=filesize(Filename);bitscv=byteme(str(Fsize))
            print(f"\n| Hashing File's integrity: {Filename.upper()} | Size: {bitscv}....")
            if "GB" in bitscv:print(f"It may take longer")  
            
            fragbyte=isZipmp3rarother(Filename)


            if fragbyte==0.03:
                posbyte=Fsize-int((Fsize*fragbyte))
                fragdata=Filehandle(Filename,posbyte,int(Fsize*fragbyte))
                ldata=len(fragdata)
                Type_file="Binary/Compressed"                     
            else:
                posbyte=0        
                fragdata=Filehandle(Filename,posbyte,int(Fsize*fragbyte))
                if is_binary(fragdata)==True:
                    ldata=len(fragdata)
                    Type_file="Binary"            
                else:     
                    ldata=(Fsize)
                    fragdata=Filehandle(Filename,posbyte,Fsize)
                    Type_file="Plain Text"
            F_hashed=sha256(Filehandle(Filename,posbyte,int(Fsize*fragbyte))).hexdigest() 
           
            intro()
            print("\n║ENCRYPTION PROCESS╠"+"═"*80+"╣[CTRL+C] Cancel the Process ║")  
            print("\n| Total Files Encrypted:",lensuc,"/",lentarg)
            print('\r[%s%s] ' % ('█' * int(lensuc*65/lentarg), '░'*(65-int(lensuc*65/lentarg))),  end='\n')
            print(f"\n| Target: 📝{path.basename(Filename)}")
            print(f"| Size: {byteme(str(Fsize))}  | Type: [{Type_file}]") 
            n=0
            bar=tqdm(range(ldata),colour='red',ncols=114,unit_scale=1,unit='bit')

            for b in fragdata:
                bar.update(1)
                encryptdata+=bytes([(b^int(256-ord(Password[n])))])
                n+=1   
                if(n == lp):
                    n=0;
            bar.close()        
            FTarget=open(Filename,"rb+")
            FTarget.seek(posbyte)
            FTarget.write(encryptdata)
            FTarget.seek(Fsize)
            FTarget.write(bytes(list(map(ord,xor('{"tox":"!CDXY","file":"'+Fn_clear(path.basename(Filename))+'","posbytes":"'+str(posbyte)+'","tarbytes":"'+str(ldata)+'","date":"'+str(date.today())+'","pass":"'+Pass_hashed+'","integrity":"'+F_hashed+'","os":"'+platform.system()+'","size":"'+str(Fsize)+'"}')))))  
            FTarget.close
            fragdata=b"";encryptdata=bytearray()
            sucessed+=[{"Filename":path.basename(Filename), "integrity":F_hashed}]
            lensuc=len(sucessed)
        except IOError as errz:
            print(f"\n[🚫{errz}")
            print("Press [ENTER] to Continue...")
            notsucessed+=[{"Filename":path.basename(Filename), "error":str(errz)}]
            FTarget="";fragdata=b"";encryptdata=bytearray()
            keypress('enter')
        except KeyboardInterrupt as kk:
                intro()
                print("\n|ENCRYPTION PROCESS CANCELED...🙄\n")
                print("✔️Encrypted:",len(sucessed),"Files ")
                if len(notsucessed)>0 :print(f"❌ {len(notsucessed)} Failed to encrypt...\n")
                report("1",sucessed,notsucessed)
                print("Would you like to see the report now? Y / N:")
                while True:
                    if keyboard.is_pressed('n'): break
                    if keyboard.is_pressed('y'): 
                        if len(sucessed)>0:
                            print("***Encrypted List\n")
                            for r in sucessed:
                                print(f"--File: {r['Filename']}   --CheckSum:{r['integrity']}")
                        if len(notsucessed)>0:
                            print("***Failed to encrypt\n")
                            for r in notsucessed:
                                print(f"--File: {r['Filename']}  --Reason:{r['error']}")          
                    exit("Done!")
                exit("Done!")
    intro()        
    if len(sucessed)>0:
        print("\n|DONE ENCRYPTING...😃\n")
        print("✔️Encrypted:",len(sucessed),"Files ")
        if len(notsucessed)>0 :print(f"❌ {len(notsucessed)} Failed to encrypt...\n")
        report("1",sucessed,notsucessed)
        print("Would you like to see the report now? Y / N:")
        while True:
            if keyboard.is_pressed('n'): break
            if keyboard.is_pressed('y'): 
                if len(sucessed)>0:
                    print("***Encrypted List\n")
                    for r in sucessed:
                        print(f"--File: {r['Filename']}   --CheckSum:{r['integrity']}")
                if len(notsucessed)>0:
                    print("***Failed to encrypt\n")
                    for r in notsucessed:
                        print(f"--File: {r['Filename']}  --Reason:{r['error']}")          
                exit("Done!")
        exit("Done!")
    elif len(notsucessed)>0:
         print("\n|DONE ENCRYPTING...😱\n")
         print(f"❌ {len(notsucessed)} Failed to encrypt...\n")
         report("1",sucessed,notsucessed)
         exit("Done!")

if optionx=="-d":
    intro()  
    print("\n║TARGET'S LIST╠"+"═"*100+"╣\n") 
    
    for xc in targets:
        try:
            if filesize(xc) > 50:
                if len(isencrypted(xc))>0:
                    filemsg="";emoj="🔐"
                else: 
                    filemsg=">>> Is not encrypted & removed from the target's list"
                    emoj="❌";banfilels+=[xc]
            else:
                filemsg=">>> File's size is low than 50 bytes, removed from the target's list..."
                emoj="😱";banfilels+=[xc]     
            print("|FILE:["+emoj+ "📄 "+path.basename(xc)+"] "+filemsg)
        except IOError as errz:
            print(f"[🚫{errz}\n")
    for xc in banfilels:
        targets.remove(xc) 
    if len(targets)==0:exit("***process canceled, no files to decrypt***") 
    print("\n|",len(targets),"Files will be decrypted.\n")
    if len(Password)==0:
        print("Type a password to decrypt the Target's List")
        print("Type 'q'+[ENTER] to CANCEL\n")
        while state!=True:
            Password=input("|🗝️PASSWORD:")
            state=ValidPass(Password)      
            if state==False:
                print("""🚩  Must have at least:
            >>>🔠 One Uppercase
            >>>🔢 One Number
            >>>🔣 One Special character:#%&!$
            >>>⛓  8 Characters
                """)
        if Password.lower()=="q" or Password.lower()=="a":exit("***process canceled...***")      
    else:
        if ValidPass(Password)==False:
            print("""🚩Password must have at least:
>>>🔠 One Uppercase
>>>🔢 One Number
>>>🔣 One Special character:#%&!$
>>>⛓  8 Characters
Terminated...""")
        else:
            print("Press [ENTER] to start...[ESC] to cancel...")
            while True:
                if keyboard.is_pressed('enter'): break
                if keyboard.is_pressed('esc'): exit("Canceled...")
    Password=inter(Password)
    lp=len(Password)
    lentarg=len(targets)
    timeprocess=datetime.now().strftime("%H:%M:%S")
    rootprocess=path.dirname(targets[0])
    for Filename in targets:
        print(f"\n| Reading file: {path.basename(Filename.upper())}....")
        headinfo=isencrypted(Filename) 
        passhashed=headinfo["pass"][32:]
        Salted=headinfo["pass"][:32]
        if checkpass(Password.encode(),passhashed,Salted.encode(),100,32):
            try:       
                AFsize=filesize(Filename) 
                Fsize=int(headinfo["size"])
                BytesTarget=int(headinfo["tarbytes"]) 
                BytesPosition=int(headinfo["posbytes"])
                F_hashed=headinfo["integrity"]  
                fragdata=Filehandle(Filename,BytesPosition,BytesTarget)                     
                intro()    
                print("\n║DECRYPTION PROCESS╠"+"═"*80+"╣[CTRL+C] Cancel the Process ║")  
                print(f"\n| Total Files Decrypted: {lensuc}/{lentarg}")
                print(f"| Integrity: ✅ {N_integrity}  ⛔ {X_integrity}")
                print('\r[%s%s] ' % ('█' * int(lensuc*65/lentarg), '░'*(65-int(lensuc*65/lentarg))),  end='\n')
                print(f"\n| Target: 📝{path.basename(Filename)}")
                print(f"| Size: {byteme(str(AFsize))}") 
                bar=tqdm(range(BytesTarget),colour='green',ncols=114,unit_scale=1,unit='bit')
                n=0
                for b in fragdata:
                    bar.update(1)
                    decryptdata+=bytes([(b^int(256-ord(Password[n])))])
                    n+=1
                    if(n == lp):
                        n=0;          
                bar.close()
                print("\n| Checking File's Integrity.....",end="")
                integrity=sha256(decryptdata).hexdigest()== F_hashed
                if integrity==True:
                    N_integrity+=1
                    print("✅")
                else:
                    X_integrity+=1
                    print("⛔")
                    print("☢️|CheckSum didn't match...")
                    print("[I]gnore the warning, try to decrypt the file and keep the original.")
                    print("[S]kip this file and continue to the next....")
                    while k!='I' and k!= 'S':
                        k=keyboard.read_key().upper()
                    if k=="S":
                        notsucessed+=[{"Filename": path.basename(Filename),"error" : "CheckSUM Didn't match"}]
                        FTarget="";decryptdata=bytearray();fragdata=b""
                        continue
                    elif k=="I":
                        print("Copying....Please wait")
                        copy2(Filename,"CopyByFIXOR-"+Filename)
                FTarget=open(Filename,"rb+")
                FTarget.seek(BytesPosition)
                FTarget.write(decryptdata)
                FTarget.seek(0)
                FTarget.truncate(Fsize)
                FTarget.close             
                fragdata=b"";decryptdata=bytearray()
                sucessed+=[{"Filename": path.basename(Filename),"integrity" : str(integrity)}]
                lensuc=len(sucessed)
            except IOError as errz:
                print(f"\n[🚫{errz}")
                print("Press [ENTER] to Continue...")
                keypress('enter')
                notsucessed+=[{"Filename": path.basename(Filename),"error" : str(errz)}]
                FTarget="";decryptdata=bytearray();fragdata=b""
            except KeyboardInterrupt as kk:
                print("\n|DECRYPTION PROCESS CANCELED...🙄\n")
                print(f"✔️Decrypted: {len(sucessed)} Files with %{int(100*(N_integrity/len(sucessed)))} Data verified!\n")
                if len(notsucessed)>0 :print(f"❌ {len(notsucessed)} Failed to decrypt...\n")
                report("0",sucessed,notsucessed)
                print("Would you like to see the report now? Y / N:")
                while True:
                    if keyboard.is_pressed('n'): break
                    if keyboard.is_pressed('y'): 
                        if len(sucessed)>0:
                            print("***Decrypted List\n")
                            for r in sucessed:
                                print(f"--File: {r['Filename']}    --CheckSum:",end="")
                                if r["integrity"]=='True': 
                                    print("✅")
                                elif r["integrity"]=='False':
                                    print("⛔")
                        if len(notsucessed)>0:
                            print("***Failed to decrypt\n")
                            for r in notsucessed:
                                print(f"--File: {r['Filename']}  --Reason:{r['error']}")          
                        exit("Done!")
                exit("Done!") 
        else:
            print("❌Your password is invalid for this file:",path.basename(Filename))
            print("Press [ENTER] to Continue...")
            keypress('enter')
            notsucessed+=[{"Filename":path.basename( Filename),"error" : "Invalid password!"}]
    intro()
    if len(sucessed)>0: 
        print("\n|DONE DECRYPTING...😃\n")  
        print(f"✔️Decrypted: {len(sucessed)} Files with %{int(100*(len(sucessed)/N_integrity))} Data verified!\n")
        if len(notsucessed)>0 :print(f"❌ {len(notsucessed)} Failed to decrypt...\n")
        report("0",sucessed,notsucessed)
        print("Would you like to see the report now? Y / N:")
        while True:
            if keyboard.is_pressed('n'): break
            if keyboard.is_pressed('y'): 
                if len(sucessed)>0:
                    print("***List decrypted\n")
                    for r in sucessed:
                        print(f"--File: {r['Filename']}    --CheckSum:",end="")
                        if r["integrity"]=='True': 
                            print("✅")
                        elif r["integrity"]=='False':
                            print("⛔")
                if len(notsucessed)>0:
                    print("***Failed to decrypt\n")
                    for r in notsucessed:
                        print(f"--File: {r['Filename']}  --Reason:{r['error']}")          
                exit("Done!")
        exit("Done!") 
    else:
         print("\n|NO DECRYPTION DONE...😱\n")
         print(f"❌ {len(notsucessed)} Failed to decrypt...\n")
         report("0",sucessed,notsucessed)
         exit("Done!") 

#Developed by Jheff Mat(iCODEXYS) 8/3/2021