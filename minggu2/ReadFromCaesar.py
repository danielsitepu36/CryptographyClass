secret = input("What's the secret?: ")
direction = input("Left/Right?: ")
retry = int(input("How much do you want to try?: "))

charlist = "abcdefghijklmnopqrstuvwxyz "
dictionary = {}
index = 0
for e in charlist:
    dictionary[e] = index
    index += 1

jump = 1
if direction == "Right":
    for cycle in range(retry):
        notsecret = ""
        for char in secret:
            index = dictionary[char]
            notsecret += charlist[index - jump]
        jump += 1
        print(notsecret)
else:
    for cycle in range(retry):
        notsecret = ""
        for char in secret:
            index = dictionary[char]
            notsecret += charlist[(index + jump) % len(dictionary)]
        jump += 1
        print(notsecret)
colnLies