for num_bottles in range(99,0,-1):
 print(f"{num_bottles} bottles of beer on the wall")
 print(f"{num_bottles} bottles of beer")

 if num_bottles ==1:
    print("take one down, pass it around, no more bottles of beer on the wall")
 else:
    print(f"take one down, pass it around, {num_bottles - 1} bottles of beer on the wall")
 print("*****************************")
 