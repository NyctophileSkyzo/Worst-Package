# Worst-Package
Best Obfuscation file Python3

## Introduction
This Python script provides functionality to encrypt and obfuscate Python code using various techniques such as compression, marshaling, and obfuscation. It includes a class `Encrypt` with methods to input code from a file, execute encryption in a loop, and save the encrypted code to another file. Additionally, there's a `Menu` function to execute the encryption process.

## Components

### Function `clear()`:
- Clears the terminal screen depending on the operating system. It checks if the platform is Linux or Windows and clears the screen accordingly.

### Class `Encrypt`:
- **Constructor (`__init__`)**: Initializes an empty list `code_list` to store the input code.
- **Method `InputCode(file_path)`**: Reads the input code from a file specified by `file_path` in binary mode and decodes it to a UTF-8 string stored in `code_string`.
- **Method `AskLoop()`**: Prompts the user to specify the number of encryption layers (`loop`). It then iterates through the encryption process (`ExeCrypt`) `loop` times and saves the result to a new file.
- **Method `ExeCrypt(code)`**: Encrypts the provided `code` using various techniques such as compression (`zlib`, `bz2`, `lzma`) and obfuscation. It returns the encrypted result.

### Function `Menu()`:
- Displays the Python version, prompts the user to input the file path containing the code to be encrypted.
- Creates an instance of the `Encrypt` class and measures the execution time of the encryption process.
- Exits the program after encryption is complete.

## Usage
1. Clone or download the repository containing this script.
2. Run the script using Python 3.x.
3. Follow the prompts to input the file path and specify the encryption layers.
4. Encrypted code will be saved to the specified output file path.

## Notes
- Ensure Python 3.x is installed on your system.
- The script includes mechanisms to prevent unauthorized access (`AntiSkid` block) and provides information about the encryption process (`__CodeObjectData__`).
- Use this script responsibly and ensure compliance with legal and ethical guidelines when encrypting code.

## Contributors
- [Nath Vaskylo Clearesta](https://www.facebook.com/freya.xyz)

## License
[MIT License](https://github.com/NathVaskyloClearesta/Worst-Package/blob/main/LICENSE)

# - MIT License
- MIT License

Copyright (c) 2024 Nathanael Vaskylo Clearesta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Support
- [X]

## Disclaimer
- [X]

## Installation
To install Python and Git, run the following commands:

```bash
# Install Python
pkg install python

# Install Git
pkg install git

# Clone the repository
git clone https://github.com/NathVaskyloClearesta/Worst-Package.git

# Navigate to the directory
cd Worst-Package

# Run the script
python Run.cpython-311.pyc
```
