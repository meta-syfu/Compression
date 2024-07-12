import zlib

def compress_file(input_file, output_file):
    try:
        with open(input_file, 'rb') as f:
            data = f.read()

        compressed_data = zlib.compress(data, level=9)
        with open(output_file, 'wb') as f:
            f.write(compressed_data)
    except Exception as e:
        print(f"Error during zlib compression: {e}")

def decompress_file(input_file, output_file):
    try:
        with open(input_file, 'rb') as f:
            compressed_data = f.read()

        data = zlib.decompress(compressed_data)
        with open(output_file, 'wb') as f:
            f.write(data)
    except Exception as e:
        print(f"Error during zlib decompression: {e}")
