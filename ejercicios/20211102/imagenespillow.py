from PIL import Image

tamaño= (128,43)
ubicacion= "C://Users//Campus FP//Downloads//alcocer.png"
imagen=Image.open(ubicacion)
imagen.thumbnail(tamaño)
imagen.save("C://Users//Campus FP//Downloads//alcocer2.png")
imagen.show()
