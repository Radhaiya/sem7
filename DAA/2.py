import heapq

# Creating Huffman tree node
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq  # frequency of symbol
        self.symbol = symbol  # symbol name (character)
        self.left = left  # node left of current node
        self.right = right  # node right of current node
        self.huff = ""  # tree direction (0/1)

    def __lt__(self, nxt):  # Check if curr frequency less than next nodes freq
        return self.freq < nxt.freq

    def printnodes(self, val=""):
        newval = val + str(self.huff)

        # if node is not an edge node then traverse inside it
        if self.left:
            self.left.printnodes(newval)
        if self.right:
            self.right.printnodes(newval)

        # if it's a leaf node, print the symbol
        if not self.left and not self.right:
            print("{} -> {}".format(self.symbol, newval))

if __name__ == "__main__":
    chars = ['a', 'b', 'c', 'd', 'e', 'f']
    freq = [5, 9, 12, 13, 16, 45]

    nodes = []

    for i in range(len(chars)):  # converting characters and frequencies into huffman tree nodes
        heapq.heappush(nodes, node(freq[i], chars[i]))

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.huff = 0
        right.huff = 1

        # Combining the 2 smallest nodes to create a new node as their parent
        newnode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, newnode)

    nodes[0].printnodes()
