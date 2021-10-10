result = {}
user_input = input(f'"Введите предложение":\n>>>')
user_input = user_input.split(" ")
user_count = len(user_input)

n = 0
m = 1
while n < user_count:
    data = user_input.pop(0)
    a = "".join(data)
    result = ("{}".format(m) + "." + "{}".format(a).center(10))
    n+=1
    m+=1
    print(result)