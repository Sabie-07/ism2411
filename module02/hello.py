print("sabie Conyers- marketing major")

Exercise 6- Deliberate Error Analysis:
-Error Type: NameError
-Line Number: Line 1
-Description: I deliberately changed the keyword "print" to "primt". Python gererated a NameError because "primt" isn't a recognized built-in function or defined variable. The traceback pointed directly to line 1 and suggested "print" as intened function.
Exercise 7- Directory Navigation Analysis: 
The first attempt failed because python looks for files in the current directory by default. When executing the parent "
ism2411" directory without specifying a folder, python couldn't locate "hello.py". The second attempt succeeded because providing the relative path "module02/hello.py" explicity directed python to navigate into the "module02" subfolder to find and run the scripts.
