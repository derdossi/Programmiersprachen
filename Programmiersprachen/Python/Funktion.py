
#! Funktion = Ein Codeblock der nur durchgeführt wird wenn er aufgerufen wird (invoking a function)

# !Parameter Anzahl muss den entsprechenden Parameter angepasst werden!

def hello(first_name, last_name, age):
    print("hello " + first_name+" "+last_name)
    print("you are "+str(age)+" years old!")
    print("Have a nice day!")


# my_name = "Bro"
# hello("Bro")
# hello("dude")
# hello(my_name)

hello("Bro", "Code", 21)
