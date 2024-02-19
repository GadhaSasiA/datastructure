# def happy(name,age):
#     print("happy birthday ",name)
#     print("you are ",age," years old")
#     print("")
# happy("nima",20)


# def bank(name,amount,duedate):
#     print("hello",name)
#     print("your bill of amount",amount,"is due on",duedate)
#     print("")
# bank("roy",50000,12/2/2024)
# bank("sanju",25000,12/2/2024)


# def calculate_grade(exam_score,project_score):
#     total_score=exam_score+project_score
#     if total_score>=90:
#        return "A"
#     elif total_score<=80:
#         return "B"
#     elif total_score<=70:
#         return "c"
#     elif total_score<=60:
#         return "D"
#     else:
#         return "failed"
    
# calculate_grade(50,26)

row=5
i=1
while i<=row:
  print("*"*i)
  i+=1

row=5
i=1
for i in range(1,row+1):
  for j in range(row,i-1):
    print("*",end="")


