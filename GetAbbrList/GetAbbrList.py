import os
import re
from os.path import isfile, join
import pandas as pd
import sys

path = sys.argv[1]
onlyfiles = [f for f in os.listdir(path) if isfile(join(path, f))]

abbfs=list()
refs=list()
for f in os.listdir(path):
    with open(path+f,'r') as fc:
        print (f)
        contents = fc.read()
        abbf = list(re.findall(r'[A-Z]{2,}',contents))
        ref = list(re.findall(r'[\s\w-]+\s+\([A-Z]{2,}\)',contents))
        abbfs=abbfs+abbf
        refs = refs+ref
abb = list(set(abbfs)) #remove repeated strings
abb.sort()
df = pd.DataFrame(abb,columns=['Abbreviation'])
df['Meaning'] = ''
df.to_csv('./'+'csvOutput.csv',index=False)
df.to_latex('./'+'latexOutput.tex',index=False)
refdf=pd.DataFrame(refs,columns=['txt'])
refdf.to_csv('./'+'ref.csv',index=False)
