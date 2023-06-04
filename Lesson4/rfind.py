import getopt
import sys
import os

def findFile(folder, name):
    for file in os.listdir(folder):
        try:
            if os.path.isdir(folder + "\\" + file) is True:
                findFile(str(folder) + "\\" + file, name)
        except:
            continue
    
    for file in os.listdir(folder):
        if name in file:
            print(folder + "\\" + file)

def main(argv):
    try:
        folder = None
        name = None
        opts, args = getopt.getopt(argv, "hf:n:", ["folder=", "name="])
        for opt, arg in opts:
            if opt == "-h":
                print("\nScript optins:\n-f --folder - path to folder\n-n --name - name of target")
                sys.exit()
            elif opt in ('-f', '--folder'):
                folder = arg.replace('/', '\\')
            elif opt in ('-n', '--name'):
                name = arg
    except Exception as e:
        print("Something went wrong: ", e)
        folder, name = None, None

    if folder is None or name is None:
        print("Missing one of two neccessery option. Type -h to help.")

    if os.path.exists(folder):
        findFile(folder, name)
    else:
        print("Folder isn't exists.")

if __name__ == "__main__":
    main(sys.argv[1:])
