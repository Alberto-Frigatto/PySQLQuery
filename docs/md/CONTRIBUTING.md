<h1 align="center">
    <img src="../img/logo.png" width="200"/>
    <br/>
    <p style="font-size: 30px">PySQLQuery</p>
</h1>

# Contributing to PySQLQuery

You can contributing in several ways like:

- Creating new features
- Fixing bugs
- Improving documentation and examples
- Translating any document here to your language

# Developing PySQLQuery

The development must be in ```src/pysqlquery``` folder and, at the moment, PySQLQuery only offers DDL SQL commands. So you can develop more features for DDL, DML and DQL commands doing a pull request.

## Running tests

The project uses [Pytest](https://docs.pytest.org/en/7.4.x/) for runing the tests.

You can install it via pip:

```
pip install pytest
```

And running tests with the command below:

```
pytest
```

## Commit messages

Commit messages should follow the following form:

```
prefix: Imperative message
```

The allowed prefixes are:

| Prefix | Description |
| --- | --- |
| feat | a new feature is introduced with the changes |
| fix | a bug fix has occurred |
| chore | changes that don't relate to a fix or feature and don't modify src or test files (for example updating dependencies) |
| refactor | refactored code that neither fixes a bug nor adds a feature |
| docs | updates to documentation such as a the README or other markdown files |
| style | changes that do not affect the meaning of the code, likely related to code formatting such as white-space, missing semi-colons, and so on |
| test | including new or correcting previous tests |
| performance | performance improvements |
| revert | reverts a previous commit |

# Reporting a bug

Use the [GitHub issue tracker](https://github.com/Alberto-Frigatto/PySQLQuery/issues) to report any bug that you find. Bugs description should include:

- The bug label
- How to reproduce the bug
- Easy to understand title

# Request a feature

Use the [GitHub issue tracker](https://github.com/Alberto-Frigatto/PySQLQuery/issues) to request a new feature. Keep in mind that PySQLQuery is a simple way to generate SQL commands throw python for programmers without several knowledges in SQL language.

# Code style

The code style will must follow the [Black Formatter](https://black.readthedocs.io/en/stable/).

<br/>

Give this repo a star and/or share it with your friends 😀!
