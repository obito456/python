import copy
org=["adhar",["Name","iris","pic"]]
web=copy.deepcopy(org)
web[1][2]="newpic"
print(org)
print(web)
