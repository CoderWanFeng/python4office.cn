---
title: "108 Curated Python Libraries — A Reference Worth Bookmarking!"
date: 2022-06-08 14:25:46
tags: [Python Libraries]
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
translation:
  source: article/108-lib-pip.md
  source_title: "108个Python精选库，建议收藏留用！"
  status: completed
  translator: ai-claude-gpt4
  date: 2026-06-14
---

# 108 Curated Python Libraries — A Reference Worth Bookmarking!

Hello, I'm Wanfeng, a Python programmer.

Why is Python so popular, and why do so many people learn it? Because it's simple to learn, powerful, has a very active community, and tons of resources. The language also spans a wide range of domains: automated testing, operations, web scraping, data analysis, machine learning, finance, backend development, cloud computing, and game development.

A towering building rises from the ground. What makes the Python ecosystem so powerful is the support of countless outstanding libraries—thousands of excellent "wheels" supporting this grand building. Today, let's take a bird's-eye view of the entire Python treasure trove.

I've roughly listed the application areas of the entire Python ecosystem, and there are more than 20 directions. The left side focuses on offense (external-facing), with each item standing as a flagship product in Python applications; the right side focuses on defense (internal-facing), dealing with low-level configuration and serving as the foundation of the entire building.

Below, I've picked the best libraries in each field. After reading this, you'll surely exclaim: "Wow, there are so many libraries I've never seen before!"

---

## 1. Infrastructure for the Python Building

### Environment Management

> Tools for managing Python versions and environments.

- **p**: A very simple interactive Python version management tool.
- **pyenv**: A simple Python version management tool.
- **Vex**: Run commands in a virtual environment.
- **virtualenv**: A tool for creating isolated Python environments.
- **buildout**: Declarative configuration management for use after initializing an isolated environment.

### Package Management

> Tools for managing packages and dependencies.

- **pip**: Python's package and dependency management tool.
- **pip-tools**: A set of tools to keep Python package dependencies up to date.
- **pipenv**: The officially recommended new-generation package management tool.
- **poetry**: A package management tool that can completely replace setup.py.
- **conda**: A cross-platform Python binary package management tool.
- **Curdling**: A command-line tool to manage Python packages.
- **wheel**: The new standard for Python distribution, intended to replace eggs.

### Distribution

> Packaged as executables for distribution.

- **PyInstaller**: Converts Python programs into standalone executables (cross-platform).
- **cx_Freeze**: Converts Python programs into executables with a dynamic link library.
- **dh-virtualenv**: Builds and publishes a virtualenv as a Debian package.
- **Nuitka**: Compiles scripts, modules, and packages into executables or extension modules.
- **py2app**: Turns Python scripts into standalone packages (macOS).
- **py2exe**: Turns Python scripts into standalone packages (Windows).
- **pynsist**: A tool for creating Windows installers that can bundle Python itself.

### Configuration

> Libraries for saving and parsing configuration.

- **config**: A hierarchical configuration module written by the author of the logging module.
- **ConfigObj**: An INI file parser with validation.
- **ConfigParser**: (Python standard library) INI file parser.
- **profig**: Configuration via multiple formats, with numerical conversion.
- **python-decouple**: Completely separates settings from code.

---

## 2. Management & Configuration of the Python Building

### Files

- **aiofiles**: Asynchronous file operations based on asyncio.
- **imghdr**: (Python standard library) Detects image types.
- **mimetypes**: (Python standard library) Maps filenames to MIME types.
- **path.py**: An encapsulation of os.path.
- **pathlib**: (Python 3.4+ standard library) A cross-platform, object-oriented path operation library.
- **python-magic**: Python interface to the third-party file type detection library libmagic.
- **Unipath**: An object-oriented way to operate on files and directories.
- **watchdog**: An API and shell tool for managing file system events.

### Date and Time

> Libraries for working with dates and times.

- **arrow**: A better Python date-time library.
- **Chronyk**: A Python 3 library for parsing handwritten time and date formats.
- **dateutil**: An extension of the Python datetime module.
- **delorean**: A library that solves tricky date-handling problems in Python.
- **maya**: A humanized time-handling library.
- **moment**: A Python library for handling time and dates, inspired by Moment.js.
- **pendulum**: A time-operation library with clearer, more predictable behavior than arrow.
- **PyTime**: An easy-to-use Python module for operating dates/times through strings.
- **pytz**: Modern and historical world time zone definitions, bringing the time zone database into Python.
- **when.py**: Provides user-friendly functions to help with common date and time operations.

### Text Processing

> Libraries for parsing and manipulating text.

**General**

- **chardet**: Character encoding detector, compatible with Python 2 and 3.
- **difflib**: (Python standard library) Helps with differential comparison.
- **ftfy**: Makes Unicode text more complete and consistent.
- **fuzzywuzzy**: Fuzzy string matching.
- **Levenshtein**: Quickly computes edit distance and string similarity.
- **pangu.py**: Adds spaces between CJK characters and digits/letters.
- **pypinyin**: A Python tool for converting Chinese characters to pinyin.
- **shortuuid**: A generator library for concise, clear, URL-safe UUIDs.
- **simplejson**: Python's JSON encoder/decoder.
- **unidecode**: ASCII transliteration of Unicode text.
- **uniout**: Prints readable characters instead of escaped strings.
- **xpinyin**: A library for converting Chinese characters to pinyin.
- **pyfiglet-figlet**: Python implementation of figlet.
- **flashtext**: An efficient text search-and-replace library.

**Slugify**

- **awesome-slugify**: A Python slugify library that preserves Unicode.
- **python-slugify**: A Python slugify library that converts Unicode to ASCII.
- **unicode-slugify**: A slug tool that can generate Unicode slugs (requires Django).

**Parsers**

- **phonenumbers**: Parses, formats, stores, and validates phone numbers.
- **PLY**: Python implementation of lex and yacc parsing tools.
- **Pygments**: A general-purpose syntax highlighter.
- **pyparsing**: A framework for generating general parsers.
- **python-nameparser**: Splits a person's name into independent parts.
- **python-user-agents**: Browser user agent parser.
- **sqlparse**: A non-validating SQL parser.

### Office Document Format Processing

**General**

- **tablib**: A module for processing tabular data.
- **python-office**: A third-party library for office automation. ([Learn more](https://mp.weixin.qq.com/s/d2m7xYCLXF8QUlr-5sSuPA))

**Office**

- **Marmir**: Converts input Python data structures into electronic spreadsheets.
- **openpyxl**: A library for reading and writing Excel 2010 xlsx/xlsm/xltx/xltm files.
- **pyexcel**: A library that provides a unified API for reading, writing, and operating Excel files.
- **python-docx**: Reads, queries, and modifies Microsoft Word 2007/2008 docx files.
- **relatorio**: Templated OpenDocument files.
- **unoconv**: Converts between any file formats supported by LibreOffice/OpenOffice.
- **XlsxWriter**: A Python module for creating Excel .xlsx files.
- **xlwings**: A library that makes it easy to call Python in Excel (and vice versa), BSD-licensed.
- **xlwt**: Reads and writes Excel file data and format information.

**PDF**

- **PDFMiner**: A tool for extracting information from PDF documents.
- **PyPDF2**: A library that can split, merge, and transform PDF pages.
- **ReportLab**: Quickly creates rich-text PDF documents.

**Markdown**

- **Mistune**: A fast and full-featured pure-Python Markdown parser.
- **Python-Markdown**: John Gruber's Markdown implementation in Python.
- **Python-Markdown2**: A pure Python Markdown parser, faster and more accurate than Python-Markdown.

**YAML**

- **PyYAML**: Python version of the YAML parser.

**CSV**

- **csvkit**: Tools for converting and manipulating CSV.

### Configuration

(Same as above: config, ConfigObj, ConfigParser, profig, python-decouple)

### Command Line Tools

> Libraries for creating command-line programs.

**Command-line Application Development**

- **asciimatics**: Cross-platform, full-screen terminal package (i.e., mouse/keyboard input and colored, positioned text output), with high-level APIs for complex animations and special effects.
- **cement**: A command-line application framework for Python.
- **click**: A package for creating beautiful command-line interfaces through composition.
- **cliff**: A framework for creating command-line programs with multi-level commands.
- **clint**: Python command-line application tools.
- **colorama**: Cross-platform colored terminal text.
- **docopt**: Python-style command-line argument parser.
- **Gooey**: One command turns a command-line program into a GUI program.
- **python-prompt-toolkit**: A library for building powerful interactive command-line programs.
- **python-fire**: A Google library for building command-line interfaces from Python classes.
- **Pythonpy**: Execute any Python instruction directly in the command line.

**Productivity Tools**

- **aws-cli**: Amazon Web Services' universal command-line interface.
- **bashplotlib**: Basic plotting in the terminal.
- **caniusepython3**: Determines which project is preventing you from porting to Python 3.
- **cookiecutter**: A command-line tool for creating projects from cookiecutters (project templates).
- **doitlive**: A tool for live presentations in the terminal.
- **pyftpdlib**: A very fast and scalable Python FTP server library.
- **howdoi**: Get instant answers to programming questions via the command line.
- **httpie**: A command-line HTTP client, a more user-friendly alternative to cURL.
- **PathPicker**: Pick files from bash output.
- **percol**: Adds interactive selection to the traditional UNIX shell pipe concept.
- **SAWS**: A reinforced AWS command line.
- **thefuck**: Corrects your previous command-line command.
- **mycli**: A MySQL command-line client with auto-completion and syntax highlighting.
- **pgcli**: A Postgres command-line tool with auto-completion and syntax highlighting.
- **try**: A simpler-than-ever command-line tool for trying out Python libraries.

---

## 3. The Warehouse of the Python Building

### Databases

> Databases implemented in Python.

- **pickleDB**: A simple, lightweight key-value store.
- **PipelineDB**: A streaming SQL database.
- **TinyDB**: A tiny, document-oriented database.
- **ZODB**: A native Python object database; a key-value and object-graph database.

### Database Drivers

> Libraries for connecting to and operating databases.

**MySQL: awesome-mysql series**

- **aiomysql**: An asynchronous MySQL library based on asyncio.
- **mysql-python**: Python's MySQL database connector.
- **mysqlclient**: A fork of mysql-python that supports Python 3.
- **oursql**: A better MySQL connector that supports native prepared statements and BLOBs.
- **PyMySQL**: A pure-Python MySQL driver, compatible with mysql-python.

**PostgreSQL**

- **psycopg2**: The most popular PostgreSQL adapter in Python.
- **queries**: A wrapper around psycopg2 for interacting with PostgreSQL.
- **txpostgres**: An asynchronous PostgreSQL driver based on Twisted.

**Other Relational Databases**

- **apsw**: Another Python SQLite wrapper.
- **dataset**: Stores Python dictionaries in a database.
- **pymssql**: A simple Microsoft SQL Server database interface.

**NoSQL Databases**

- **asyncio-redis**: A redis client based on asyncio (PEP 3156).
- **cassandra-python-driver**: Cassandra's Python driver.
- **HappyBase**: A developer-friendly library designed for Apache HBase.
- **Plyvel**: A fast and feature-rich Python interface to LevelDB.
- **py2neo**: A Python client wrapping Neo4j's RESTful interface.
- **pycassa**: Cassandra's Python Thrift driver.
- **PyMongo**: MongoDB's official Python client.
- **redis-py**: Redis's Python client.
- **telephus**: A Twisted-based Cassandra client.
- **txRedis**: A Twisted-based Redis client.

---

## Conclusion

This is just a curated list of 108 Python libraries across the most important domains. Bookmark it for future reference, and you'll never be at a loss when you need a tool for a particular job.

Happy coding!
