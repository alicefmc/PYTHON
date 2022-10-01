
from importlib.resources import path
import os 
import shutil


from_dir = "/Users/aliceferreiradamotacosta/Downloads/PRO_1-1_C102_AtividadeDoAluno1"
to_dir = "/Users/aliceferreiradamotacosta/Downloads/PYTHON/c102"
list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)
    if extension == "" :
        continue
    if extension in [".jpg",".png",".jpeg",".gif",".jfif"] :
        path1 = f'{from_dir}/{file_name}'
        path2 = f'{to_dir}/imagens'
        path3 = f'{to_dir}/imagens/{file_name}'
        if os.path.exists(path2) :
            print(f"movendo {file_name}...")
            shutil.move(path1,path3)    
        else: 
            os.makedirs(path2)    
            print(f"movendo {file_name}...")
            shutil.move(path1,path3)    
   