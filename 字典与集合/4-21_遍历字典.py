#遍历zidianyuansu
print("方案1遍历key值")
meau={"101":("鱼香肉丝",38),
      "102":("红烧鲈鱼",48),
      "201":("红油鸡丝",36),
      "203":("芥末木耳",25)}
for key in meau.keys():
    print(key+":",meau[key])


print("方案2遍历value值")
for value in meau.values():
    print(value)


print("方案3遍历数字的元素")
for kv in meau.items():
    print(kv)

print("方案4遍历字典元素，但是把键-值分开获取")
for key,value in meau.items():
    print(key+":",value)