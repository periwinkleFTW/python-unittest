# Python Unittest 

This is a repo for the unittest course from udemy


#Projects

Project 1: Testing functions

Project 2: Testing classes

Project 3: Testing console output

Project 4: Testing efficiency/performance

Project 5: TDD - Wealth Management Calculator


# Notes

- Run all tests within a directory:
```bash
python -m unittest discover
```

- Run all tests in a specific module:
```bash
python -m unittest tests.test_my_module
```

- Run specific testcase within a module:
```bash
python -m unittest tests.test_my_module.TestCalculate
```

- Run specific method within a testcase:
```bash
python -m unittest tests.test_my_module.TestCalculate.test_calculate_easy
```

- Test suites are used to group tests for easier testing. 
You can select methods/classes to run thus making sure only the required
  tests are running.
  

#Preproduction checklist:
- Step 1:
Run all your tests, and ask yourself: did all my tests pass? If not, then what adjustments do I need
to make to pass all the tests?
Once you have all your tests pass and you think that your program is doing what it should, then
you are ready for the next step.
  

- Step 2:
Run all your tests in coverage mode, and ask yourself: is there any part of my program that is not
being tested? If so, why? Is it because I did not write enough tests? Or, is it because my
implementation of the program is poor? That is, I have a chunk of code that I use nowhere in my
program. If you did not write enough tests, then write a test to make sure that %100 of your code
is being tested. However, if your problem is having extra not needed code (meaning, dead code),
then simply delete the code that is not being used. Once your coverage tests cover %100 of your
code, then you’re ready to move to the next step.
  

- Step 3:
Run all your tests in debugging mode, and ask yourself: are the values of each of my variables
correct (that is, what I expect them to be)? Is each method returning, and executing each line of
code in the order you expect? If not, why? And what should you do to fix it? Finally, ask yourself
the following question: is my program behaving the same way I expected to behave? If not,
why? And what can I do to fix it?
Once you're done debugging, then you’re ready to move to the next step.


- Step 4:
Go to the file where the program is written, and ask yourself: is my code readable? That is, if
another programmer looked at my code, then how long will it take for them to understand my
implementation? Two minutes or one hour or a couple of days. What may seem clear to you may
not be so clear to others. Therefore, make sure that you're using the simplest yet most effective
methods to accomplish the needed tasks in your program, write comments next to each
complicated line of code, write one sentence above each method explicitly telling what the
method does, and finally, include a brief description on the top of your file stating what your
module does, it's author, date it was created, how to use it, and it's purpose. Once you're done
with this step, then you can move to the next one. 


- Step 5:
Run code inspection on your entire package, and ask yourself: are there any spelling errors? Are
there any todo’s that I need to do? Is there any incorrect spacing between my methods or my
classes? If there are any mistakes, correct them. Otherwise, you're all set. 