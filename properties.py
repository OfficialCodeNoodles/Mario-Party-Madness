from os.path import exists

class Properties(object):
    def __init__(self):
        self.filename = "properties.txt"
        self.mainScreenRegion = [ 0, 182, 960, 720 ]
        self.mainScreenScale = 3.75
        self.subScreenRegion = [ 960, 182, 960, 720 ]
        self.subScreenScale = 3.75
    def loadFile(self):
        if not exists(self.filename):
            self.saveFile()
            return 
        
        with open(self.filename, 'r') as file:
            for line in file.readlines():
                attribute, value = Properties.seperate(line)

                if attribute == "mainScreenScale":
                    self.mainScreenScale = float(value)
                elif "mainScreen" in line:
                    for varIndex in range(len(self.mainScreenRegion)):
                        variableName = Properties.getScreenVariableName(
                            "mainScreen", varIndex
                        )

                        if attribute == variableName[:-1]:
                            self.mainScreenRegion[varIndex] = int(value)
                elif attribute == "subScreenScale":
                    self.subScreenScale = float(value)
                elif "subScreen" in line:
                    for varIndex in range(len(self.subScreenRegion)):
                        variableName = Properties.getScreenVariableName(
                            "subScreen", varIndex
                        )

                        if (attribute == variableName[:-1]):
                            self.subScreenRegion[varIndex] = int(value)
    def saveFile(self):
        with open(self.filename, 'w') as file:
            file.write("# Variables that refer to the top screen of the DS\n")
            file.write(f"mainScreenScale={self.mainScreenScale}\n")
            for varIndex, value in enumerate(self.mainScreenRegion):
                file.write(
                    Properties.getScreenVariableName('mainScreen', varIndex)
                        + repr(value) + '\n'
                )

            file.write("\n# Variables that refer to the bottom screen of the DS\n")
            file.write(f"subScreenScale={self.subScreenScale}\n")
            for varIndex, value in enumerate(self.subScreenRegion):
                file.write(
                    Properties.getScreenVariableName('subScreen', varIndex)
                        + repr(value) + '\n'
                )
    @staticmethod
    def getScreenVariableName(name: str, index: int) -> str:
        if index < 2:
            return f"{name}{'Xpos' if index & 1 == 0 else 'Ypos'}="
        return f"{name}{'Width' if index == 2 else 'Height'}="
    @staticmethod
    def seperate(string: str, symbol: chr = '=') -> tuple:
        symbolIndex = string.find(symbol)
        return ( string[:symbolIndex if symbolIndex != -1 else len(string)], 
            string[symbolIndex+1:] if symbolIndex != -1 else "")
            
properties = Properties()