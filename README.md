# Prestashop API Autotesting with Pytest

This repository includes automated tests to check REST API of the online store MyShop, running on CMS Prestashop. Tests were designed for CRUD operations of six endpoints and for each endpoint check there is a separate .py file.

## Download
Before executing tests you have to download the py.file from this repository or the whole repository.

If you want to download the repository, click the small arrow on the green ```Code``` button at the top right of the repo contents. From here, select ```Download Zip```. This will download the entire GitHub repository as a zipped folder.

If you need a single file, start by clicking the ```Go to file``` button at the top of the repo contents. From the list of all files in the repository choose the one you need, right-click the ```Raw``` button at the top of the file, select ```Save Link As…```, choose the location on your computer where you want to save the file, and select ```Save```.

We recommend saving py.files, either downloaded or unzipped, under their original names. If you want to change the file's name, make sure it matches the pattern ```test_*.py``` or ```*_test.py```.
  
Besides, make sure that the folder you have saved downloaded tests contains only Pytest-executable files.

## Pytest and Requests installation
Python, Pytest and HTTP library Requests are needed to run tests from this directory.

If your Python version is 3.7+, you can start with Pytest installation and run in your command line ```pip install -U pytest```. After installation check that you have installed the correct version: ```pytest --version pytest```

To install Requests, run in your command line ```pip install requests``` (or ```python -m pip install requests```).

If you have any problems installing the software, we recommend referring to the official documentation at https://docs.pytest.org/ and https://requests.readthedocs.io/ to resolve this issue.

## Test execution
The general way to execute tests is to run ```pytest``` in your command line while being in the directory where you have saved downloaded files.
If it doesn't work, try calling Pytest through ```python
python -m pytest
```.

By default, Pytest runs all files of the form test_*.py or *_test.py in the current directory and its subdirectories. To execute a specific file in the directory, run ```pytest –v .\test_name``` in the command line where ```test_name``` stands for the actual name of the file. To execute a single test in the file, run ```pytest –v .\test_file_name::test_name``` in the command line, where ```test_file_name``` stands for the actual name of the file and ```test_name```stands for the actual name of the test. 

As а result of the test run the number of passed items is displayed, as well as the number of failures if any occurred and а failure report.
To display the status of each test during execution, call Pytest through ```pytest -v```.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
