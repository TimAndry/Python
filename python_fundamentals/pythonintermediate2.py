x = [ [5,2,3], [10,8,9] ] 

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]
x[1][0] = 15
print(x)

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory['soccer'][0] = "Andres"
print(sports_directory)

z[0]['y'] = 30
print(z)


def iterateDictionary():
  students =[
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ]

  for i in range(len(students)):
    # print(students[i]['first_name'] + " "+ students[i]['last_name'])
    # print(students[i].keys())
    for key in students[i].keys():
      print(key)
      print(students[i][key])


iterateDictionary()


def iterateDictionary2():
  locations = ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank']

  instructors = ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'mihn', 'Devon']
  count1 = 0
  count2 = 0
  for i in range(len(locations)):
    print(locations[i])
    count1=count1+1
    
  print(count1, ' Locations')

  for j in range(len(instructors)):
    print(instructors[j])
    count2 = count2+1

  print(count2, ' Instructors')

iterateDictionary2()


dojo = {
   'location': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
  }

def iterateDictionary3(dict):
  
  for key in dict:
    print(len(dict[key]))
    print(key)
    for i in dict[key]:
      print(i)#for j in range(len(dojo[i]))


iterateDictionary3(dojo)








