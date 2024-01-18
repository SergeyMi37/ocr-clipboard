
# To install Tesseract OCR for Windows:

 1. Run the [installer](https://digi.bib.uni-mannheim.de/tesseract/)(find 2021) from UB Mannheim
 2. Configure your installation (choose installation path and language data to include)
 3. Add Tesseract OCR to your environment variables
- https://github.com/UB-Mannheim/tesseract/wiki

To install and use Pytesseract on Windows:
 1. Simply run `pip install pytesseract`
 2. You will also need to install [Pillow](https://pypi.org/project/Pillow/) with `pip install Pillow` to use Pytesseract. Import it in your Python document like so `from PIL import Image`.
 3. You will need to add the following line in your code in order to be able to call pytesseract on your machine: `pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'`

```
python -m venv env
source env/bin/activate
source env/Scripts/activate # for Windows
python -m pip install --upgrade pip
pip install -r requirements.txt
python ocr.py
```
```
python.exe ocr.py
```
```
 [INFO] Save a picture with text to the clipboard and recognize it with a hotkey:
     For Russian text <Alt + r>
     For English text <Alt + q>
 [INFO] Exit the program <Alt + z>
```
# My thanks

- https://ru.stackoverflow.com/questions/1397570/%D0%9A%D0%B0%D0%BA-%D0%B7%D0%B0%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BF%D0%B8%D1%82%D0%BE%D0%BD-%D0%BF%D0%BE%D0%B9%D0%BC%D0%B0%D1%82%D1%8C-%D0%BC%D0%BE%D0%BC%D0%B5%D0%BD%D1%82-%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0-%D0%B2-%D0%B1%D1%83%D1%84%D0%B5%D1%80%D0%B5-%D0%BE%D0%B1%D0%BC%D0%B5%D0%BD%D0%B0-%D0%BF%D0%BE%D1%8F%D0%B2%D0%BB%D1%8F%D0%B5%D1%82%D1%81%D1%8F-%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B0
- https://sourceforge.net/projects/tesseract-ocr-alt/files/
- https://stackoverflow.com/questions/46140485/tesseract-installation-in-windows
- https://github.com/tesseract-ocr/tesseract?tab=readme-ov-file#installing-tesseract
- https://dzen.ru/a/Y5CdY19xiA-YGKXy

# Convenient to use in conjunction with a program that places a screen fragment on the clipboard
https://app.prntscr.com/ru/index.html

