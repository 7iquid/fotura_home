import json
list_ko=[]
a = {"id":1,"id":2,"id":3}


b={1:"name",2:"page",3:"gender"}
b.update({1:"tinapay",2:"page",3:"gender"})
c={1:"name",2:"page",3:"gender"}
d={1:"name",2:"page",3:"gender"}
		# 	print(json.dumps(user_list, indent=4))

list_ko.append(b)
list_ko.append(c)
list_ko.append(d)

for i in list_ko:
	print(i)
print(json.dumps(list_ko, indent=4))