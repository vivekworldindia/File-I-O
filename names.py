# names = []

# for _ in range(3):
#  name = input("what's your names? ")
#  names.append(name)
 
# for name in sorted(names):
#     print(f"name,{name}")



# name = input("what's your name? ")
# with open("names.txt","a") as file:
#     file.write(f"{name}\n")
    
    
# with open("names.txt" ,"r") as file:
    
#     lines = file.readlines()
# for line in sorted(lines):
#     print(f"hello,{line.rstrip()}")


# with open("names.txt" , "r") as file:
    # for line in file:
    #     print("hello," , line.rstrip())
    
# names = []

# with open("names.txt" ,"r") as file:
#     for line in file:
#         names.append(line.rstrip())
        
# for name in sorted(names):
#     print(f"hello,{name}")

 
     

names = []

with open("names.txt" ,"r") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names,reverse=True):
    print(f"hello,{name}")

     
