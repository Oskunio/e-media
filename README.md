# e-media

## 1.Dodawanie metadanych

# Pliki

Plik squareWithExif.png został uzupełniony o metadane przy użyciu strony:
https://www.thexifer.net/

# Metadane

Do odczytu metadanych z plików png użyte zostały biblioteki: PLI (Pillow), cv2, hachoir.
Przy wizualizacji oraz transformacie Fouriera korzystano z matplotlib oraz numpy

# Sprawdzenie poprawności

Do sprawdzenia poprawności ekstrakcji danych przez program korzystano z edytora obrazów GIMP (od wersji 2.10 wyświetla on metadane pliku) oraz online-owy program odczytujący metadane z pliku: http://exif.regex.info/exif.cgi

# Wnioski
Dodanie metadanych znacząco zwiekszyło rozmiar pliku, gdyż plik wynikowy zajmuje 8,57 KB, gdzie obraz orginalny zajmuje zaledwie 269 B

## 2.Usuwanie ancillary chunks

# Pliki
Plik wejsciowy: square.png 
Plik wynikowy: newSquare.png

# Działanie
Na początku zostaje wyświetlony orginalny obraz square.png. Funkcja findAndRemoveAncillaryChunk usuwa ancillary chunks przeszukując szesnastkowy kod pliku. Następnie zostaje wyswietlony obraz wynikowy newSquare.png.
# Wnioski
Rozmiar pliku orginalnego to 269 B, a pliku wynikowego (po usunieciu chunk'ów) 219 B. Poprawność została sprawdzona poprzez uzycie funkcji printFileInHex i programu Hex Editior.

# 3. Interpretacja IHDR
## Działanie
Funkcja IHDRinterpretation dokonuje analizy IHDR i interpretuje otrzymane dane.
