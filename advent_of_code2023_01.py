file = open("input.txt", "r")

#prva cast 
alist = file.readlines()

def take_numbers(text):
    x = []
    result = []
    for i in text:
        if i.isnumeric():
           x.append(i)
    return int(x[0] + x[-1])


result = sum(list(map(take_numbers,alist)))

#print(result)

#druhá čast
thisdict = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
   "six": 6,
   "seven": 7,
   "eight":8, 
   "nine":9
}

#print(thisdict.keys())
#prejst slovnik a z toho nahradit hodnoty 

keys = list(thisdict.keys())
def replace_number(test):
    for  i  in range(len(keys)):
        test = test.replace(keys[i],str(thisdict[keys[i]]))
    return test 


#preparing data for calculation
prep_data = list(map(replace_number,alist))
result2 = list(map(take_numbers,prep_data))
print(sum(result2))


with open('subor.txt', 'w') as file:
    file.write(str(prep_data))