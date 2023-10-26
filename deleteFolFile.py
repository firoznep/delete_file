import shutil
import os

print('-' * 50, '\nWARNING\n','Once deleted, data will be removed permanently.\nDelete at your own risk!\nTo delete: Place this file to the same file you want to delete.\n','_' * 50)

print('*' * 10, 'To close type: "exit" or "e"', '*' * 10, '\n')


def delAnyThing():
    getCurrentDir = os.getcwd()
    while True:
        fileName = input('Give the folder or file name: ')
        
        getFilePath = f'{getCurrentDir}\\{fileName}'

        if fileName == '':
                print('Name should not be empty!\n')
                continue
        if fileName == 'exit' or fileName == 'e':
             exit()

        try:
            print(getFilePath) 
            os.chmod(fileName, 0o777)
            shutil.rmtree(getFilePath)
            print(f'{fileName} is deleted\n')
        except FileNotFoundError:
            print('Error.... File not found\n')
        except NotADirectoryError:
            os.chmod(fileName, 0o777)
            os.remove(getFilePath)
            print(f'{fileName} is deleted\n')
        except PermissionError:
             print('Error... Access Denied!')


delAnyThing()
