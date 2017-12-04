#######################################################
### Please ignore the lines of code in this section.
### It loads the contents of a CSV file for you.
### The file's name should be a2_input.csv.
### You do not need to know how it works.
#######################################################

import csv

contents = []
with open("a2_input.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]

total = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
count_of_megacities = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
count_of_metropolises = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for j in range(1, 11):
    for i in range(1, 82):
        total[j - 1] += int(contents[i][j].replace(' ', ''))
        if int(contents[i][j].replace(' ', '')) >= 10000000:
            count_of_megacities[j-1] += 1
        elif int(contents[i][j].replace(' ', '')) >= 1000000:
            count_of_metropolises[j-1] += 1

print("""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <style>
      table, th, td {
        border: 1px solid black;
      }
    </style>
    <title>Output of my lovely algorithm</title>
  </head>
  <body>
    <table class="population">
      <tr>
""")
for j in range(11):
    print('        <th>', end='')
    print(contents[0][j], end='')
    print('        </th>', end='')
    print()
print('      </tr>')

for i in range (1, 82):
    print('      <tr>')
    print()
    for j in range (11):
        print('        <td>', end='')
        print(contents[i][j], end='')
        print('        </td>', end='')
        print()
    print('      </tr>')
    print()


print('      <tr>')
print()
print('        <td>', end='')
print('total', end='')
print('        </td>', end='')
print()
for j in range(10):
    print('        <td>', end='')
    print(total[j], end='')
    print('        </td>', end='')
    print()
print('      </tr>')
print()

print('      <tr>')
print()
print('        <td>', end='')
print('number of megacities', end='')
print('        </td>', end='')
print()
for j in range(10):
    print('        <td>', end='')
    print(count_of_megacities[j], end='')
    print('        </td>', end='')
    print()
print('      </tr>')
print()

print('      <tr>')
print()
print('        <td>', end='')
print('number of metropolises', end='')
print('        </td>', end='')
print()
for j in range(10):
    print('        <td>', end='')
    print(count_of_metropolises[j], end='')
    print('        </td>', end='')
    print()
print('      </tr>')
print()

print("""
      </table>
    </body>
</html>
""")


#######################################################
### Do your data processing below.
### The below code gives some examples
### of how to access the data.
### Print your results using the print function.
#######################################################

