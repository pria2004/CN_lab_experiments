def text_to_binary(text):
    """Convert text string to binary representation."""
    return ''.join(format(ord(char), '08b') for char in text)

def calculate_redundant_bits(m):
    """Calculate the number of redundant bits (parity bits) needed for a message of length m."""
    for i in range(m):
        if 2**i >= m + i + 1:
            return i

def position_redundant_bits(data, r):
    """Place redundant (parity) bits in the binary data at positions which are powers of two."""
    n = len(data) + r
    arr = ['0'] * n  # Initialize with 0s to place both data and redundant bits

    # Place data bits in the array
    j = 0
    for i in range(1, n + 1):
        if i & (i - 1) == 0:  # Power of two positions for parity bits
            continue
        arr[i - 1] = data[j]
        j += 1

    return arr

def calculate_parity_bits(arr, r):
    """Calculate the parity bits and insert them in the appropriate positions."""
    n = len(arr)
    for i in range(r):
        parity_pos = 2**i
        count = 0
        for j in range(1, n + 1):
            if j & parity_pos == parity_pos:
                count += int(arr[j - 1])
        arr[parity_pos - 1] = str(count % 2)
    
    return ''.join(arr)

def hamming_code(data):
    """Encode the binary data using Hamming Code by adding parity bits."""
    m = len(data)
    r = calculate_redundant_bits(m)
    arr = position_redundant_bits(data, r)
    arr = calculate_parity_bits(arr, r)
    return arr

def sender(text):
    """Convert text to binary, encode with Hamming Code, and save to Channel.txt."""
    binary_data = text_to_binary(text)
    hamming_data = hamming_code(binary_data)
    
    with open("Channel.txt", "w") as f:
        f.write(hamming_data)
    
    print(f"Data sent: {hamming_data}")

# Example usage
text = "Message Received"
sender(text)
