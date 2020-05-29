import xml.etree.ElementTree as ET
from xml.dom import minidom
import random
import timeit

start = timeit.default_timer()
root = ET.Element("root")
sub = ET.SubElement(root, "sub")
sub_sub = ET.SubElement(sub, "sub_sub")

for i in range(1000):

    rn = random.randint(1, 3)
    if rn == 1:
        ET.SubElement(root, "item", name="number").text = str(i)

    if rn == 2:
        ET.SubElement(sub, "item", name="number").text = str(i)

    if rn == 3:
        ET.SubElement(sub_sub, "item", name="number").text = str(i)


tree = ET.ElementTree(root)
tree.write("test.xml")

print('Write time: ', (timeit.default_timer() - start) / 1000)

start = timeit.default_timer()

root = minidom.parse('test.xml')
number = 0

for elem in root.getElementsByTagName('item'):
    print(elem.firstChild.data)

print('Read time: ', (timeit.default_timer() - start) / 1000)