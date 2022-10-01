#要求一
def calculate(min, max, step):
    total=0
    for x in range(min, max+1, step):
        total+=x  #total=total+x
    print(total)

calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

#要求二
def avg(data):
    list=data["employees"]
    sum=0
    not_manager=0
    for item in list:
        if item["manager"]==False:
            sum+=int(item["salary"])
            not_manager+=1
            ans=sum/not_manager
    print(ans)

avg({
        "employees":[
            {
                    "name":"John",
                    "salary":30000,
                    "manager":False
            },
            {
                    "name":"Bob",
                    "salary":60000,
                    "manager":True
            },
            {
                    "name":"Jenny",
                    "salary":50000,
                    "manager":False
            },
            {
                    "name":"Tony",
                    "salary":40000,
                    "manager":False
            }
    ]
}) # 呼叫 avg 函式



#要求三
def func(a):
    def multiply(b,c):
        print(a+(b*c))
    return multiply

func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果


#要求四
def maxProduct(nums):
    list=[] #new list
    for a in range(0,len(nums)):
        for b in range(a+1, len(nums)):
            list.append(nums[a]*nums[b]) #add number to the new list
    max=list[0] 
    for c in list:
        if c>max:                
            max=c
    print(max)

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10


#要求五
def twoSum(nums, target):
    for a in nums:
        for b in nums:
            if a+b==target:
                return[nums.index(a),nums.index(b)]
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
