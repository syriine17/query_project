# Query_Project

This is a sample project that demonstrates the usage of query runners for different databases.

## Project Structure

The project structure is as follows:

```shell
query_project/
├── query_runner.py
├── tests/
│ └── test_query_runner.py
└── README.md
```



- `query_runner.py`: Contains the implementation of the query runners and the query runner factory.
- `tests/`: Directory containing the test files for the query runners and the query runner factory.
- `README.md`: This file, providing project information and instructions.

## How to Run

Follow these steps to run the project and execute the tests:

1. Clone the project repository:

```shell
git clone https://github.com/syriine17/query_project.git
```


2. Navigate to the project directory:

```shell
cd query_project
```


3. (Optional) Set up a virtual environment to isolate the project dependencies:

python3 -m venv venv
source venv/bin/activate

4. execute the query runner code

```shell
python query_runner.py
```


4. Install the project dependencies (unittest is used for testing):

```shell
pip install unittest
```


5. Run the tests using the following command:

```shell
python -m unittest discover tests
```


This command will execute all the test cases in the `tests/` directory and display the test results in the terminal.

6. Code Coverage

To generate a code coverage report, follow these steps:

Make sure you have installed the `coverage` package:

```shell
pip install coverage
```

Run the tests with coverage:

```shell
coverage run -m unittest discover tests
```

Generate the coverage report:

```shell
coverage report
coverage report --show-missing
```

## License

This project is licensed under the [MIT License](LICENSE).






