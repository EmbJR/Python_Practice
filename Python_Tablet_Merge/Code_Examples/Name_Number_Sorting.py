import sys as system
from colorama import init, Fore, Back, Style

HomeData = dict({1:"NameSample"})

HomeData[2] = "Name2"
'''
print(Fore.RED + 'This text is red')
print(Back.GREEN + 'This text has a green background')
print(Style.BRIGHT + Fore.CYAN + 'This text is bright cyan')
print("This text is normal again due to autoreset=True")
'''

def ReadAllData(DataForm):
     for key, values in DataForm.items():
          print( key, ":",  values)

def DeleteAllData(DataForm):
     DataForm.clear()
    
def Add_Data(DataForm, Number, Name):
     DataForm[Number] = Name
    
def Edit_Data(DataForm, Number, Name): 
    DataForm[Number] = Name 

while(True):
     option = int(input(Fore.RESET+'''Enter the Option 
                 1> Add New Entery
                 2> Delete the Entry
                 3> Read All Entry
                 4> Exit from App\n'''))
     match option:
          case 1:
               Nb = int(input(Fore.GREEN + "Enter Home Number:- "))
               NM = input("Enter name of Owner:- ")
               Add_Data(HomeData, Nb, NM)
          case 2:
               DeleteAllData(HomeData)
               print(Fore.GREEN + 'Deleted All entries')
          case 3:
               print(Fore.CYAN + '')
               ReadAllData(HomeData)
               print(Fore.GREEN + 'Read Completed')
          case 4:
               break
          case _:
                print("case None")
                break
                  

  