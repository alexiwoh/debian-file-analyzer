![Python CI](https://github.com/alexiwoh/debian-file-analyzer/actions/workflows/python-ci.yml/badge.svg)

# debian-file-analyzer
A python command line tool that takes the architecture (amd64, arm64, mips etc.) as an argument and downloads the compressed Contents file associated with it from a Debian mirror. The program parses the file and output the statistics of the top 10 packages that have the most files associated with them.

# Setup

## For running the tool
```bash
pip install -r requirements.txt
```

## For development/linting/testing
```bash
pip install -r requirements-dev.txt
```

## Make the script executable
```bash
chmod +x ./package_statistics.py
```

## 🚀 Run the app by typing this in the terminal

./package_statistics.py YOUR_ARCHITECTURE

### Examples:
```bash
./package_statistics.py amd64
```
```bash
./package_statistics.py arm64
```
```bash
./package_statistics.py mipsel
```
```bash
./package_statistics.py armel
```
```bash
./package_statistics.py i386
```

## 🧼 Code Quality

Before submitting, you can auto-format and lint your code with:

```bash
isort . && black . && flake8 .
```

## 🧪 Testing
To run the tests, you can use pytest. Make sure you have pytest installed in your environment. You can run the tests with the following command:

```bash
pytest tests/
```