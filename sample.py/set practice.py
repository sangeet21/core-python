#set={ "python","java","c++","python","javascript","java","python","java","c++","c"}

#print(len(set))


marks={}
a=input("enter first subject mark:")
b=input("enter seconnd subject mark:")
c=input("enter third subject mark:")
marks.update({"math":a})
marks.update({"eng":b})
marks.update({"ben":c})
print(marks)
