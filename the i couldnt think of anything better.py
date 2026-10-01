# the i couldnt think of anything better to make so im just doing the conduct mark checker idea because im actually really bad with coming up with idea on what i could create with python project
class record:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def display (self):
        print(self.name)
        print(self.grade)


# database
a = record('Alpha','A')
b = record('Beta','B')
c = record('Charlie','C')
d = record('Delta','D')
f = record('Foxtrot','F')

print("temp code remove later 1 Alpha 2 Beta 3 Charlie 4 Delta 5 Foxtrot")
print("S.D.B. Students Conduct Grade Viewer")
sid = int(input("Student ID: "))
sname = input("Name: ")

if sid == 1:
    if sname == 'Alpha':
        a.display()
    else:
        print("Student grade not found")
elif sid == 2:
    if sname == 'Beta':
        b.display()
    else:
        print("Student grade not found")
elif sid == 3:
    if sname == 'Charlie':
        c.display()
    else:
        print("Student grade not found")
elif sid == 4:
    if sname == 'Delta':
        d.display()
    else:
        print("Student grade not found")
elif sid == 5:
    if sname == 'Foxtrot':
        f.display()
    else:
        print("Student grade not found")
else:
    print("Student grade not found")
