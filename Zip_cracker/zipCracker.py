<<<<<<< HEAD

import zipfile

zipFilePath = rf"{input('Zip folder: ')}"
passFilePath = r"passList.txt"

with zipfile.ZipFile(zipFilePath, "r") as zFile:
    with open(passFilePath, "r") as pFile:

        for line in pFile.readlines():
            try:
                password = bytes(line, encoding='utf-8')
                zFile.extractall(pwd=password)
            
            except:
=======

import zipfile

zipFilePath = rf"{input('Zip folder: ')}"
passFilePath = r"passList.txt"

with zipfile.ZipFile(zipFilePath, "r") as zFile:
    with open(passFilePath, "r") as pFile:

        for line in pFile.readlines():
            try:
                password = bytes(line, encoding='utf-8')
                zFile.extractall(pwd=password)
            
            except:
>>>>>>> cfcb7be9398a4df0a743e67c98abf03da234c2e5
                pass