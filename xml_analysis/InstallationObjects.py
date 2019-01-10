import xml_analysis.XmlAnalysis

class InstallationObjects:
    def __init__(self, file):
        self._root = xml_analysis.XmlAnalysis.XmlAnalysis(file).getInstallationObjects()

    def getAllProperty(self):
        list = []
        for i in self._root.iter('property'):
            print("key:", i.get('name'))
            for j in i.iter():
                if j.findtext("string") != None:
                    print("value:", j.findtext("string"))
            #print(i.itertext())

    #com.zerog.ia.installer.actions.EditVariableTable
    def getVariableList(self):
        for pEle in self._root.iter("property"):
            if pEle.get("name") == "preInstallActions":
                for i in pEle.iter():
                    if i.get("class") == "com.zerog.ia.installer.actions.EditVariableTable":
                        print("■EditVariableTable")
                        for j in i.iter("property"):
                            if j.get("name") == "name":
                                for k in j:
                                    print("name:", k.text)
                            if j.get("name") == "value":
                                for k in j:
                                    print("value", k.text)

    #com.zerog.ia.installer.actions.EditMultipleVariables
    def getMultipleVariables(self):
        for pEle in self._root.iter("property"):
            if pEle.get("name") == "preInstallActions":
                for i in pEle.iter():
                    if i.get("class") == "com.zerog.ia.installer.actions.EditMultipleVariables":
                        print("■EditMultipleVariables")
                        for j in i.iter("property"):
                            if j.get("name") == "propertyList":
                                for k in j.iter():
                                    if k.get("class") == "com.zerog.ia.installer.util.EditMultipleVariablePropertyData":
                                        for l in k.iter("property"):
                                            if l.get("name") == "propertyName":
                                                for m in l:
                                                    print("name:", m.text)
                                            if l.get("name") == "propertyValue":
                                                for m in l:
                                                    print("value", m.text)

    def getVariableNameList(self):
        pass