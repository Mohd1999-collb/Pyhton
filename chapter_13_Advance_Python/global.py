
a = 15;
def val() :
    global a;  # use global keyword to modify global variable
    a = 20;
    print (a);

val();
print (a);