import os

# "E:\\GIT\\Python\\testOSlib"


def renameFiles(pathStr, renameTxt):
    i = 0

    for f in os.listdir(pathStr):
        name = renameTxt + str(i)+".txt"
        os.rename(pathStr + f, pathStr + name)
        i += 1


renameFiles("E:\\GIT\\Python\\testOSlib\\", "done")
