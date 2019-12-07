class Layer():
    def __init__(self, pixels, length, breadth):
        self.pixels = pixels
        self.length = length
        self.breadth = breadth
        self.rows = [self.pixels[i:i+breadth] for i in range(0, len(pixels), breadth)]

def build_layers(data, length, breadth):
    data = str(int(data))
    image_pixels = [data[i:i+length*breadth] for i in range(0, len(data), length*breadth)]
    return [Layer(pixels, length, breadth) for pixels in image_pixels]
data = open('day08_input.txt').read()

image = build_layers(data, 6, 25)

def build_image(layers):
    length = layers[0].length
    breadth = layers[0].breadth
    pixels = []
    for i in range(length):
        ith_rows = [layer.rows[i] for layer in layers]
        row = ''
        for j in range(breadth):
            row += decode([row[j] for row in ith_rows])
        pixels.append(row)
    return pixels

def decode(pixel_input):
    for pixel in pixel_input:
        if pixel=='0':
            return '0'
        if pixel=='1':
            return '1'



###################### PART-1 ######################
zeros_dict = {layer: str(''.join(layer.pixels)).count('0')
              for layer in image}

corrupted_image = [layer for layer, zeros in zeros_dict.items()
                   if zeros==min(zeros_dict.values())][0]

corrupted_pixels =  ''.join(corrupted_image.pixels)
print corrupted_pixels.count('2') * corrupted_pixels.count('1')


###################### PART-1 ######################
image = build_image(image)
for row in image:
    print row

######## OUTPUT #########
'''
0110011110100101001001100
1001010000101001001010010
1000011100110001001010010
1000010000101001001011110
1001010000101001001010010
0110011110100100110010010
'''
