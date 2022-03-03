# Write a python program which accept one input 
# input : "hii" --- output : "bye"
# input : "bye" --- output : "hii"
i = input()
dict = { 'hii':'bye','bye':'hii'}
print(dict.get(i))