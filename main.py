from dbconnect_util import DBManager
from dbconnect_util import View
import xml_analysis.InstallationObjects

print("START")

xml = xml_analysis.InstallationObjects.InstallationObjects("Test_Linux.iap_xml")
xml.getMultipleVariables()
xml.getVariableList()
print("=========================")


print('END')
