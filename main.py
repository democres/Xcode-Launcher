import os

print("Creating folder structure...")

project_path = os.getcwd()
print(" - Your current project path is : " + project_path)

folders = ["Application","Base","Config","Docs","Frameworks","Resources","Tests","Vendors","UITests"]
for folder in folders:
    if not os.path.exists(os.path.join(project_path,folder)):
        os.mkdir(os.path.join(project_path,folder))

print("Folder structure created successfully")
