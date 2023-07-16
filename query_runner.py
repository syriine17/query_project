import typing as tg


class QueryRunner:
    def get_number(self, configuration: tg.Dict) -> tg.Union[int, float]:
        """Abstract method to get a number from a query runner.
        
        Args:
            configuration (dict): Configuration data for the query.

        Returns:
            Union[int, float]: The retrieved number.
        """
        pass


class MongoDBQueryRunner(QueryRunner):
    def get_number(self, configuration: tg.Dict) -> tg.Union[int, float]:
        """Implementation of get_number for MongoDB query runner.
        
        Args:
            configuration (dict): Configuration data for the query.

        Returns:
            Union[int, float]: The retrieved number.
        """
        return 1


class BigQueryQueryRunner(QueryRunner):
    def get_number(self, configuration: tg.Dict) -> tg.Union[int, float]:
        """Implementation of get_number for BigQuery query runner.
        
        Args:
            configuration (dict): Configuration data for the query.

        Returns:
            Union[int, float]: The retrieved number.
        """
        return 2


class MySQLQueryRunner(QueryRunner):
    def get_number(self, configuration: tg.Dict) -> tg.Union[int, float]:
        """Implementation of get_number for MySQL query runner.
        
        Args:
            configuration (dict): Configuration data for the query.

        Returns:
            Union[int, float]: The retrieved number.
        """
        return 3


class QueryRunnerFactory:
    def __init__(self, query_runners: tg.Dict[str, QueryRunner]):
        """Initialize the QueryRunnerFactory.

        Args:
            query_runners (dict): A dictionary mapping query runner names to instances of QueryRunner.
        """
        self.query_runners = query_runners

    def get_dao(self, query_runner_name: str) -> QueryRunner:
        """Retrieve an instance of a specific QueryRunner based on the provided query_runner_name.

        Args:
            query_runner_name (str): The name of the desired query runner.

        Returns:
            QueryRunner: An instance of the requested query runner.

        Raises:
            ValueError: If the requested query runner is not supported.
        """
        query_runner = self.query_runners.get(query_runner_name)
        if query_runner is None:
            raise ValueError(f"Unsupported query runner: {query_runner_name}")
        return query_runner


def configure_query_runners() -> tg.Dict[str, QueryRunner]:
    """Configure the available query runners.

    Returns:
        dict: A dictionary mapping query runner names to instances of QueryRunner.
    """
    query_runners = {
        "mongodb": MongoDBQueryRunner(),
        "mysql": MySQLQueryRunner(),
        "bigquery": BigQueryQueryRunner(),
    }
    return query_runners


def create_query_runner_factory() -> QueryRunnerFactory:
    """Create an instance of QueryRunnerFactory with the configured query runners.

    Returns:
        QueryRunnerFactory: An instance of QueryRunnerFactory.
    """
    query_runners = configure_query_runners()
    factory = QueryRunnerFactory(query_runners)
    return factory


def main(query_runner_name: str):
    # Create the QueryRunnerFactory
    factory = create_query_runner_factory()

    # Example usage
    query_options = {
        "sql_statemant": "select count(*) as the_number from `orders`",
        "return_value": "the_number"
    }

    query_runner = factory.get_dao(query_runner_name)
    result = query_runner.get_number(query_options)

    print(result)  # Output: The retrieved number


if __name__ == "__main__":
    # Get query_runner_name from user input or request it through a web framework
    query_runner_name = input("Enter the query runner name: ")
    main(query_runner_name)
