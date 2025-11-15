# Unit Testing and Integration Testing Project

## Project Overview
This project focuses on implementing comprehensive unit tests and integration tests for Python code using the `unittest` framework. The project demonstrates best practices for testing, including mocking external dependencies, parameterized testing, and integration testing.

## Learning Objectives
By completing this project, you will be able to:
- Explain the difference between unit and integration tests
- Implement common testing patterns such as mocking, parametrization, and fixtures
- Write comprehensive test suites for Python applications
- Mock external dependencies like HTTP requests and database calls
- Use parameterized testing to test multiple inputs with the same test code

## Key Concepts

### Unit Testing
- Tests individual functions or methods in isolation
- Mocks all external dependencies
- Answers: "If everything outside this function works, does this function work?"
- Fast execution
- Tests both standard inputs and corner cases

### Integration Testing
- Tests multiple components working together
- Mocks only external systems (HTTP, databases, file I/O)
- Tests code paths end-to-end
- Slower execution but validates system integration

### Testing Patterns
- **Mocking**: Replacing real objects with test doubles
- **Parametrization**: Running the same test with different inputs
- **Fixtures**: Reusable test data and setup
- **Memoization**: Caching expensive function calls

## Project Structure
```
0x03-Unittests_and_integration_tests/
├── utils.py
├── client.py
├── fixtures.py
├── test_utils.py
├── test_client.py
└── README.md
```

## Files Description

### `utils.py`
Contains utility functions:
- `access_nested_map`: Safely access nested dictionary values
- `get_json`: Fetch JSON from a remote URL
- `memoize`: Decorator to cache method results

### `client.py`
Contains `GithubOrgClient` class for interacting with GitHub API:
- Fetches organization information
- Retrieves public repositories
- Filters repositories by license

### `test_utils.py`
Unit tests for utility functions:
- `TestAccessNestedMap`: Tests nested dictionary access
- `TestGetJson`: Tests JSON fetching with mocked HTTP calls
- `TestMemoize`: Tests memoization decorator

### `test_client.py`
Tests for GitHub client:
- `TestGithubOrgClient`: Unit tests with mocked dependencies
- `TestIntegrationGithubOrgClient`: Integration tests with real data flow

## Testing Commands

```bash
# Run all tests
python -m unittest discover

# Run specific test files
python -m unittest test_utils.py
python -m unittest test_client.py

# Run with verbose output
python -m unittest discover -v

# Run specific test classes
python -m unittest test_utils.TestAccessNestedMap
python -m unittest test_client.TestGithubOrgClient
```

## Testing Features Implemented

### 1. Parameterized Unit Tests
- Multiple test inputs using `@parameterized.expand`
- Tests for both success and exception cases

### 2. Mocking HTTP Calls
- Mocked `requests.get` to prevent actual HTTP requests
- Verified correct URL calls and response handling

### 3. Property Mocking
- Mocked properties using `PropertyMock`
- Tested computed properties without executing dependencies

### 4. Integration Testing
- Used fixtures for realistic test data
- Minimal mocking of only external systems
- Tested complete code paths

### 5. Memoization Testing
- Verified that expensive operations are cached
- Ensured methods are called only once when memoized

## Dependencies
- Python 3.7+
- `unittest` (standard library)
- `unittest.mock` (standard library)
- `parameterized` (for parameterized testing)

## Best Practices Demonstrated

1. **Isolation**: Each test is independent
2. **Comprehensive Coverage**: Tests normal cases, edge cases, and error conditions
3. **Readable Tests**: Clear test names and structure
4. **Fast Execution**: Mocked external dependencies for quick tests
5. **Maintainable**: Easy to update when code changes

## Example Test Output
```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
```

## Author
This project is part of the ALX Backend Python curriculum, focusing on software testing methodologies and best practices.

## License
This project is for educational purposes as part of the ALX Software Engineering program.