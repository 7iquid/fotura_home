import json

# dict_ko =({1:{"a":123}})
# dict_ko =({2:{"a":123}})
dict_ko ={}
list_ko =[]

dict_ko = {"first":"name"}
list_ko.append(dict_ko)
dict_ko = {"first":"tamina"}
list_ko.append(dict_ko)
dict_ko = {"first":"popo"}
list_ko.append(dict_ko)
dict_ko = {"first":"papaa"}
list_ko.append(dict_ko)

# print(type(dict_ko),dict_ko)


# dict_ko["b"]={
# 	"aaaa":"sdcf",
# 	"cccc":"asdf",
# }
# print(dict_ko)
print(json.dumps(list_ko, indent=4, sort_keys=True))

# for idx, val in enumerate(dict_ko):
#     print(idx, val)