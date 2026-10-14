
from typing import Dict
import heapq


class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoder:
    def __init__(self):
        self.root = None
        self.codes = {}

    def build_tree(self, frequencies: Dict[str, int]) -> Node:
        if not frequencies:
            raise ValueError("Frequency dictionary cannot be empty")

        heap = []
        count = 0

        for char, freq in frequencies.items():
            if freq <= 0:
                raise ValueError("Frequencies must be positive")
            heapq.heappush(heap, (freq, count, Node(char, freq)))
            count += 1

        while len(heap) > 1:
            f1, _, left = heapq.heappop(heap)
            f2, _, right = heapq.heappop(heap)

            parent = Node(None, f1 + f2, left, right)
            heapq.heappush(heap, (parent.freq, count, parent))
            count += 1

        self.root = heap[0][2]
        return self.root

    def generate_codes(self) -> Dict[str, str]:
        if self.root is None:
            raise ValueError("Build the tree first")

        self.codes = {}

        def traverse(node, code):
            if node.char is not None:
                self.codes[node.char] = code or "0"
                return

            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

        traverse(self.root, "")
        return self.codes


# Main program
frequencies = {
    'A': 5,
    'B': 9,
    'C': 12,
    'D': 13,
    'E': 16,
    'F': 45
}

coder = HuffmanCoder()
coder.build_tree(frequencies)

codes = coder.generate_codes()

print("Huffman Codes:")
for char, code in sorted(codes.items()):
    print(char, ":", code)
