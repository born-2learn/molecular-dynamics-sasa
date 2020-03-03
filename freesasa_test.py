import freesasa

savedData = open('SASA.txt', 'w+')
structure = freesasa.Structure("3lau.pdb")

result = freesasa.calc(structure,
                       freesasa.Parameters({'algorithm' : freesasa.LeeRichards,
                                            'n-slices' : 100}))
print(result.nAtoms())

for i in range(1,result.nAtoms()+1):
    details = '('+structure.atomName(i)+','+str(result.atomArea(i))+' )'
    print(details)
    savedData.writelines(details+'\n')

area_classes = freesasa.classifyResults(result, structure)
print(area_classes)
print ("Total : %.2f A2" % result.totalArea())
for key in area_classes:
    print(key, ": %.2f A2" % area_classes[key])