import heapq
import pickle
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq = Counter(text)
    heap = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]

def build_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node.char is not None:
        codebook[node.char] = prefix
    else:
        build_codes(node.left, prefix + "0", codebook)
        build_codes(node.right, prefix + "1", codebook)

    return codebook

def huffman_compress(data):
    tree = build_huffman_tree(data)
    codebook = build_codes(tree)
    compressed_data = ''.join(codebook[char] for char in data)
    padding_length = 8 - len(compressed_data) % 8
    compressed_data += '0' * padding_length

    byte_array = bytearray()
    for i in range(0, len(compressed_data), 8):
        byte_array.append(int(compressed_data[i:i+8], 2))

    byte_array.append(padding_length)
    return byte_array, tree

def huffman_decompress(byte_array, tree):
    padding_length = byte_array[-1]
    bit_string = ''.join(f"{byte:08b}" for byte in byte_array[:-1])
    bit_string = bit_string[:-padding_length]

    current_node = tree
    decoded_data = bytearray()
    for bit in bit_string:
        current_node = current_node.left if bit == '0' else current_node.right

        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = tree

    return decoded_data

def compress_file(input_file, output_file):
    try:
        with open(input_file, 'rb') as f:
            data = f.read()

        compressed_data, tree = huffman_compress(data)
        
        # Serialize the tree and save it with compressed data
        with open(output_file, 'wb') as f:
            pickle.dump((compressed_data, tree), f)

        return tree
    except Exception as e:
        print(f"Error during Huffman compression: {e}")

def decompress_file(input_file, output_file):
    try:
        with open(input_file, 'rb') as f:
            compressed_data, tree = pickle.load(f)

        data = huffman_decompress(compressed_data, tree)
        with open(output_file, 'wb') as f:
            f.write(data)
    except Exception as e:
        print(f"Error during Huffman decompression: {e}")
