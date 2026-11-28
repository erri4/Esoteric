import sys
from fissix.refactor import RefactoringTool, get_fixers_from_package

if len(sys.argv) < 2:
	print('Command use:' + sys.argv[0] + ' <program>')
	exit(1)

with open(sys.argv[1]) as openfile:
    theFile = openfile.read()

    if theFile.find("<rant>")==-1:
        print("Syntax error: missing <rant>")
        exit(1)
    if theFile.find("</rant>")==-1:
        print("Syntax error: missing </rant>")
        exit(1)
    if theFile.find("</rant>") <= theFile.find("<rant>"):
        print("Syntax error: </rant> before <rant>")
        exit(1)

    array = theFile.split("\n")
    array2 = theFile.split("!!!")

    if len(array2) < len(array)-2:
        print("Syntax error: unterminated command")
        exit(1)

    theFile = theFile.replace("<rant>","## START OF RAGE PROGRAM")
    theFile = theFile.replace("</rant>","## END OF RAGE PROGRAM")
    theFile = theFile.replace("SCREAM","print")
    theFile = theFile.replace("WHY DOES ","")
    theFile = theFile.replace("MEAN THE SAME THING AS","=")
    theFile = theFile.replace("WHAT YOU'RE ABOUT TO TELL ME","input()")
    theFile = theFile.replace("!!!","")
    theFile = theFile.replace("WHY WOULD YOU CREATE A FUNCTION CALLED","def")
    theFile = theFile.replace("BUT WHAT IF","elif")
    theFile = theFile.replace("WHAT IF","if")
    theFile = theFile.replace("HAPPENS","")
    theFile = theFile.replace("WELL THEN I WILL","else")
    theFile = theFile.replace("AS LONG AS","while")
    theFile = theFile.replace("MEANS THE SAME THING AS","==")

refactor = RefactoringTool(
    get_fixers_from_package("fissix.fixes")
)
if not theFile.endswith("\n"):
    theFile += "\n"

converted = str(refactor.refactor_string(theFile, str(sys.argv[1])))
exec(converted)