def read_ppm_binary(filename):
    with open(filename, 'rb') as f:
        # Lê o cabeçalho
        magic_number = f.readline().strip()
        if magic_number != b'P6':
            raise ValueError("Esperado formato P6 (binário).")

        # Pula comentários
        def read_line():
            line = f.readline()
            while line.startswith(b'#'):
                line = f.readline()
            return line

        dims = read_line()
        while dims.strip() == b'':
            dims = read_line()
        width, height = map(int, dims.strip().split())

        max_val = int(read_line().strip())
        if max_val != 255:
            raise ValueError("Este código só suporta imagens com max_val = 255.")

        # Lê os dados binários RGB
        data = f.read(width * height * 3)
        image = []
        idx = 0
        for y in range(height):
            row = []
            for x in range(width):
                r = data[idx]
                g = data[idx + 1]
                b = data[idx + 2]
                row.append((r, g, b))
                idx += 3
            image.append(row)
    return image, width, height, max_val

def write_ppm_binary(filename, image, width, height):
    with open(filename, 'wb') as f:
        f.write(b'P6\n')
        f.write(f"{width} {height}\n".encode())
        f.write(b'255\n')
        for row in image:
            for r, g, b in row:
                f.write(bytes([r, g, b]))

def to_grayscale(image):
    gray_image = []
    for row in image:
        gray_row = []
        for r, g, b in row:
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            gray_row.append((gray, gray, gray))
        gray_image.append(gray_row)
    return gray_image

def to_binary(image, threshold=128):
    binary_image = []
    for row in image:
        binary_row = []
        for r, g, b in row:
            val = r  # já está em escala de cinza
            binary_pixel = 255 if val >= threshold else 0
            binary_row.append((binary_pixel, binary_pixel, binary_pixel))
        binary_image.append(binary_row)
    return binary_image

# Caminho do arquivo original
input_file = "debinha_coberta.ppm"

# Leitura da imagem P6
img, w, h, max_val = read_ppm_binary(input_file)

# Gera imagem em tons de cinza
gray_img = to_grayscale(img)
write_ppm_binary("debinha_cinza.ppm", gray_img, w, h)

# Gera imagem binária (preto e branco)
binary_img = to_binary(gray_img)
write_ppm_binary("debinha_binaria.ppm", binary_img, w, h)

print("Imagens geradas: debinha_cinza.ppm e debinha_binaria.ppm")
