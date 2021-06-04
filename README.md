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
