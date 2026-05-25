from pathlib import Path
import os

def createfile():
    try:
        print('the files which exists are:')
        path=Path('')
        it=list(path.rglob('*'))
        for i, it in enumerate(it):
            print(f"{i+1} : {it}")
        name=input("enter new file name:")
        p=Path(name)
        if not p.exists():
            with open (p,"w") as fs:
                data = input("write here....")
                fs.write(data)
                print("file created")
        else:
            print("file already exists")
    except Exception as err:
        print(f"error occurerred {err}")
  

def readfile():
        try:
            print("existing files are: ")
            path=Path('')
            it=list(path.rglob('*'))
            for i, it in enumerate(it):
                print(f"{i+1} : {it}")
            new=input("enter file name to read: ")
            p=Path(new)
            if p.exists() and p.is_file():
                with open(p,'r') as fs:
                    data=fs.read()
                    print(data)
                print("file read successfully")
            else:
                print("file doesn't exist")        
        except Exception as err:
            print(f"error : {err}")
def updatefile():
    try:
        print("existing files are: ")
        path=Path('')
        it=list(path.rglob('*'))
        for i, it in enumerate(it):
            print(f"{i+1} : {it}")
        name=input("enter filename to edit: ")
        p=Path(name)
        if p.exists() and p.is_file():
            print("1--> rename file")
            print("2--> overrite file")
            print("3--> append to file")
        cho=int(input("enter your choice "))
        
        
        if cho == 1:
            name2=input(f"enter new name for file {name} :")
            p2=Path(name2)
            p.rename(p2)
            print(f"file {name} canged to {name2}")
        
        if cho == 2:
            over=input("enter name of file to overwrite: ")
            p=Path(over)
            with open(p,"w") as fs:
                content=input(("enter the contents to overwrite: "))
                fs.write(content)

        if cho==3:
            with open(p,'a') as fs:
                a_content=input("enter contents to apppend: ")
                fs.write(" "+a_content)
    except Exception as err:
        print(f" error: {err}")
        
def deletefile():
    try:
        print("existing files are: ")
        path=Path('')
        list_file=list(path.rglob('*'))
        for i, file in enumerate(list_file):
            print(f"{i+1} : {file}")
        p=input("enter file name to delte file : ")
        path=Path(p)  
        if path.exists() and path.is_file():
            os.remove(path)
            print( f" {path} deleted")
        else:
            print("no such file exist")
    except Exception as err:
        print(f"error: {err}")
            
    

    


print("1-->Create")
print("2-->Read")
print("3-->Update")
print("4-->Delete")


inp=int(input("enter your choice: "))

if inp==1:
    createfile()
elif inp==2:
    readfile()
elif inp==3:
    updatefile()
elif inp==4:
    deletefile()