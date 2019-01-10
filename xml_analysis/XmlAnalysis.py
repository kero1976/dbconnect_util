import xml.etree.ElementTree as ET

class XmlAnalysis:
    def __init__(self, file):
        self._xml_file = file
        tree = ET.ElementTree(file=self._xml_file)
        self._root = tree.getroot()

    def getEssentialScriptInfo(self):
        for element in self._root:
            if element.tag == "essentialScriptInfo":
                return element

    def getInstallationObjects(self):
        for element in self._root:
            if element.tag == "installationObjects":
                return element

