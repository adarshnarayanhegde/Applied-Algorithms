import heapq
#http://www.gutenberg.org/cache/epub/29444/pg29444.txt

# Class to construct huffman tree
class Node:
    def __init__(self,frequency,character=None):
        self.left=None
        self.right=None
        self.charater=character
        self.frequency=frequency
    def __lt__(self, other_node):
        return self.frequency < other_node.frequency

# Reading input text
fd=open("huffman_text.txt","r")
txt=fd.read().replace('\n','')

# Calculating frequencies of the characters within the input text- frequencies are calculated only if the input character is within the given ASCII range (32-127)
char_frequency={}
for ch in txt:
    if(ord(ch)>31 and ord(ch)<128):
        if char_frequency.get(ch):
            char_frequency[ch]+=1
        else:
            char_frequency[ch]=1

input_txt=[]
for i in char_frequency:
    input_txt.append((i,char_frequency.get(i)))


# Creating an array of nodes for Huffman Tree
chars=[]
for i in input_txt:
    chars.append(Node(i[1],i[0]))


# Huffman Algorithm
# Maintaining a priority queue for characters along with their frequencies
heapq.heapify(chars)
ch1=chars
while(len(ch1)>1):
    a=heapq.heappop(ch1)
    b=heapq.heappop(ch1)
    z=Node(a.frequency+b.frequency)
    z.left=a
    z.right=b
    heapq.heappush(ch1,z)


# Huffman Encoding for each each ASCII character within the input text
huff_codes = {}
def huff_encode(code, node):
    if node.charater:
        huff_codes[node.charater] = code
    else:
        huff_encode(code+"0", node.left)
        huff_encode(code+"1", node.right)

huff_encode("",ch1[0])

#printing Huffman codes
print("Character : Huffman-Code")
for i in huff_codes:
    print("\t"+i,":",huff_codes[i])

#Calculating the number of bits with 7 bit encoding
fix=0
for i in char_frequency:
    fix+=7*(char_frequency.get(i))
print("Total number of bits with 7-bit encoding:",fix)

#Calculating the number of bits with Huffman encoding
huf=0
for i in huff_codes:
    huf+=(len((huff_codes.get(i))))*(char_frequency.get(i))

print("Total number of bits with Huffman Encoding:",huf)
print("Number of Bits Saved with Huffman Encoding:",fix-huf)

