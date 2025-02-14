names_tuple = 'Rod', 'Jane', 'Freddy'

#with open('newfile.txt, 'rt') as
append = open('newfile.txt', 'a')  # most common thing done with a log file is append

try:
    print("####### TRY #######")
    print("The TRY block attempts to run")
    print(f"Original Tuple: {names_tuple}")
    names_sorted_as_list = sorted(names_tuple) #sorting the list by alphabetical order. Converts the tuple to a list.
    print(names_sorted_as_list)
    names_sorted_as_list.append("Bungle")
    print("Added Bungle:", names_sorted_as_list) #Adds a new item to the start of the tuple
    print("Attempt to manipulate the tuple...")

    #for line in names_tuple:
            #print(line, sep=' ', end='') #We tried to separate the names, can you help?
            #people = names_tuple
    append.write (f"{names_tuple}")
    #append.writelines (names_tuple)

    names_tuple[0] = 'Zippy' #asking to change Rod with Zibby but it is not working as tuples are unmutable and cannot be changed
    print("Is this code reached?") #no, this line will not be executed because there was an error.
except FileNotFoundError as error:
    print("####### EXCEPT: FileNotFoundError #######")
    print("The EXCEPT /CATCH block only runs if this error happens")
    print(f"The following file can not be found: {error.filename}. Please try another file")
except TypeError as error: #except handles an error by returning a message.
    #This is the error that has been found and is being returned to the user. No other errors will be returned.
    print("####### EXCEPT: TypeError #######")
    print("Oh dear, that is not allowed on that type")
    print(error)
except Exception as error:
    print("######## Except: Exception ########")
    print("Generic catch-all except / catch block")
    print(error)
finally: #This always runs after an error message has been returned to the user
    # Always close file handle after use
    print("The FINALLY block ALWAYS runs")
    print("The finally block is used to tidy up")
    if names_tuple:
        names_tuple = None

print("After exception handling is finished... the program can continue")