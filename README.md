# Caesar Cipher Tool (GUI)

A professional and user-friendly Python application for encrypting and decrypting text using the Caesar cipher algorithm, featuring a graphical user interface built with Tkinter.

---

## 🚀 Features

- **Encrypt/Decrypt** any text using the Caesar cipher
- **Intuitive GUI** built with Tkinter for ease of use
- Supports both upper and lower case letters
- Keeps non-alphabetic characters unchanged
- Cross-platform: Works on Windows, Linux, and macOS

---

## 📦 Repository

This project is hosted on GitHub:  
[https://github.com/SaifAlvi0/Ceaser-cipher-tool.git](https://github.com/SaifAlvi0/Ceaser-cipher-tool.git)

---

## 🛠️ Installation

### 1. Clone the repository

```sh
git clone https://github.com/SaifAlvi0/Ceaser-cipher-tool.git
cd Ceaser-cipher-tool
```

### 2. (Optional) Create a virtual environment

It is recommended to use a virtual environment for Python projects:

```sh
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install required libraries

This tool requires **Tkinter**.  
Tkinter is included with most standard Python installations. If you need to install it manually, use:

- **For Debian/Ubuntu/Linux:**
  ```sh
  sudo apt-get install python3-tk
  ```

- **For macOS (usually pre-installed):**
  If not available:
  ```sh
  brew install python-tk
  ```

- **For Windows:**  
  Tkinter is included by default with the official Python installer from python.org.

---

## 💻 Usage

Run the Caesar Cipher tool using:

```sh
python3 caesar_cipher_gui.py
```

### How to use:

1. Enter the text you wish to encrypt or decrypt.
2. Specify the shift value (0-25).
3. Select either "Encrypt" or "Decrypt".
4. Click the "Run Caesar Cipher" button to view the result.

---

## 🧩 How Caesar Cipher Works

The Caesar cipher is a classic substitution cipher in which each letter of the plaintext is shifted by a fixed number down the alphabet.  
For example, with a shift of 3:  
- "A" becomes "D"
- "B" becomes "E", etc.

Non-alphabetic characters (spaces, numbers, punctuation) remain unchanged.

---

## 📷 Screenshot

![Screenshot](screenshot.png) <!-- Add your own screenshot and replace this file if needed -->

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

**Made by [SaifAlvi0](https://github.com/SaifAlvi0) – for educational and professional use.**  
Feel free to contribute, suggest improvements, or report issues!
