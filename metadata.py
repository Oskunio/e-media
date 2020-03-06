import png

filename = "square.png"
r = png.Reader(filename=filename)
data = r.read()
print(data)
