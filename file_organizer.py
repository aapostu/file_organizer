# Input data:
#     -Path to folder
# const:
#     -DIR_NAMES
#     -FILE EXTESION

# output:
#     - Move files in the specific folder
import os
import shutil

def menu():
    path = input("Insert the path or press q to exit the program: ")
    while not path_validation(path): #daca nu trece validarea cere din nou inserarea pathului
        if path =='q':
            exit()
        path = input("Insert the path or press q to exit the program: ")
    print('The path is valid')
    return path

def path_validation(path: str) -> bool:#primeste variabila path si returneaza true sau false
    return os.path.isdir(path)#daca este sau nu un folder

def create_dirs(path: str):
    for dir in DIR_TYPES:
        if not os.path.isdir(path + '\\' + dir):
            os.mkdir(path + '\\' + dir)

#listdir(path) - o lista de toate files din path dat 
#pentru fiecare file din lista listdir, daca acel file este un fisier il pune in lista 
def list_of_files(path:str) -> list:
    files = [file for file in os.listdir(path) if os.path.isfile(path + '\\' + file)]
    return files 

def extract_file_extension(file: str) -> str:
    indexes = [i for i, ch in enumerate(file) if ch == '.']#gasim indecele unde se afla punctului
    if indexes:#daca sunt elemente 
        file_extension = file[indexes[-1]::]#alegem ultimul indice al punctului si facem trunchere pana la final
        return file_extension
    else:
        return 'no extension'

def map_extension_to_folder(path:str) -> dict:#returneaza un dinctionar in care cheile sunt calea catre foldere din DIR_TYPES iar valorile sunt extensiile specifice din FILE_EXT_TYPES
    extension_mapping = {path + '\\' + dir:FILE_EXT_TYPES[i] for i,dir in enumerate(DIR_TYPES)}
    return extension_mapping

if __name__ == '__main__':
    DIR_TYPES = ['Pictures', 'Videos', 'PDF_files', 'Music',
                 'TXT_files', 'Python_files', 'Word_files',
                 'Excel_files', 'Archived_files', 'Install']
    FILE_EXT_TYPES = [['.jpg','.jpeg', '.png', '.JPG'], ['.mp4', '.mov',
                       '.avi', '.MOV'], ['.pdf', '.PDF'], '.mp3', '.txt',
                       '.py', ['.doc', '.docx'], ['.csv', '.xls', '.xlsx'],
                       ['.7z', '.zip', '.rar'], ['.exe', '.msi', '.iso']]
    path = menu()
    mapping = map_extension_to_folder(path)
    # print(mapping)
    create_dirs(path)
    files = list_of_files(path)
    #acuma trebuie sa iteram prin lista ca sa extragem extensia si in functie de ea le mut in folderul specific
    for file in files:
        file_extension = extract_file_extension(file)
        # print(file_extension)
        for k,v in mapping.items():#pentru fiecare keye si valoare din dictionar
            if file_extension in v:#daca extensia mea se afla in valoare dictionarului
                try:
                    shutil.move(path + '\\' + file, k)#mutam fisierul in k adica keia dictionarului care contine extensia data
                except:
                    print(file + ' cannot be moved!')
