import sys

from lib.fileHelper import FileHelper
from lib.pathConfig import *

from lib.buildProject import *

# how to compile the main.c with external compiler and linker from C:\_SoftwareBuildSetup

# Build_Project().tempBuild()

def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "-i":
            Build_Project().run("increment")
        elif command == "-c":
            Build_Project().run("complete")       
        else:
            print("Error, invalid args")
            print("args: -i for increment build")
            print("args: -c for complete  build")
            print()
    else:
        print("You need input an args:")
        print("args: -i for increment build")
        print("args: -c for complete  build")
        print()

if __name__ == "__main__":
    main()



