import angr
binary = input("Enter your binary path or name :")
project = angr.Project(binary)
entry = project.factory.entry_state()
manager = project.factory.simg(entry)