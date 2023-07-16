import unittest
from query_runner import *


class QueryRunnerTests(unittest.TestCase):
    def test_mongodb_query_runner(self):
        query_runner = MongoDBQueryRunner()
        configuration = {}
        result = query_runner.get_number(configuration)
        self.assertEqual(result, 1)

    def test_bigquery_query_runner(self):
        query_runner = BigQueryQueryRunner()
        configuration = {}
        result = query_runner.get_number(configuration)
        self.assertEqual(result, 2)

    def test_mysql_query_runner(self):
        query_runner = MySQLQueryRunner()
        configuration = {}
        result = query_runner.get_number(configuration)
        self.assertEqual(result, 3)


class QueryRunnerFactoryTests(unittest.TestCase):
    def test_get_dao_with_valid_query_runner(self):
        query_runners = {
            "mongodb": MongoDBQueryRunner(),
            "mysql": MySQLQueryRunner(),
            "bigquery": BigQueryQueryRunner(),
        }
        factory = QueryRunnerFactory(query_runners)

        query_runner = factory.get_dao("bigquery")
        self.assertIsInstance(query_runner, BigQueryQueryRunner)

    def test_get_dao_with_invalid_query_runner(self):
        query_runners = {
            "mongodb": MongoDBQueryRunner(),
            "mysql": MySQLQueryRunner(),
            "bigquery": BigQueryQueryRunner(),
        }
        factory = QueryRunnerFactory(query_runners)

        with self.assertRaises(ValueError):
            factory.get_dao("invalid_query_runner")


if __name__ == "__main__":
    unittest.main()
