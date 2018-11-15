import xml.etree.cElementTree as ET

tree = ET.ElementTree(file='dy_Report_2017.xml')
root = tree.getroot()

# print(root)
# for child in root:
# 	print(child.tag, child.attrib)

# print(root[7])
dataset = root[7]
# for child in dataset:
# 	print(child.tag, child.attrib)

# print(dataset[0])
# for child in dataset[0]:
# 	print(child.tag, child.attrib)

print(dataset[0][0].text)
print(dataset[0][1].text)
# print(dataset[0][2])
# for child in dataset[0][2]:
# 	print(child.tag, child.attrib)
print(dataset[0][2][0].text)
# print(dataset[0][2][1])
# for child in dataset[0][2][1]:
# 	print(child.tag, child.attrib)
print(dataset[0][2][1][0].text)
# print(type(dataset[0][2][1][0].text))
# for child in dataset[0][2][1][1]:
# 	print(child.tag, child.attrib)
print(dataset[0][2][1][1][0].text)
