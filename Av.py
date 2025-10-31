import angr
binary = input("Enter your binary path or name :")
project = angr.Project(binary)
entry = project.factory.entry_state()
manager = project.factory.simg(entry)
this_addr = input("Enter ur ADDR to find :")
avoid_addr = input("Enter avoid Addr :") 
manager.explore(find=this_addr,avoid= avoid_addr)

if manager.found:
   print(manager.found[0].posix.dump(0)) # std input
else:
   print("Not found!")