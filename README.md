Complex If Else
===============

This repository contains complex if-else chains and their corresponding simplified versions
-------------------------------------------------------------------------------------------

To install all the dependencies
```bash
poetry install
```

To run tests without coverage
```bash
poetry run pytest
```

To run tests with notifying watcher (for linux)
```bash
./ptw-linux.sh
```

To run tests with coverage
```bash
poetry run pytest --cov=src --cov=test --cov-report=html
```

To run the cyclomatic complexity
```bash
poetry run radon cc -s src
```
