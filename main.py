from pyscript import display

x = "Year" #string
y = 2025 #integer
z = 3.14 #float
a = True #bool
b = ['Ako', 'Ay', 'May', 'Lobo'] #list
c = (1,2,3) #tuple
d = {1,2,3} #set with int
e = {'emerald', 'ruby', 'sapphire'} #set with string
f = {
    "name": "Raph",
    "age": 15,
    "description": "pogi"

}

display('The data type of x is ', type(x), target="div1") #display output in div
display(type(y), target="div1") 
display(type(z), target="div1")
display(type(a), target="div1")
display(type(b), target="div1")
display(type(c), target="div1")
display(type(d), target="div1")
display(type(e), target="div1")
display(type(f), target="div1")