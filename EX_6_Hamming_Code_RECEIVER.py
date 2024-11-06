def calculate_redundant_bits_length(n):
    """Calculate the number of redundant bits required for a Hamming code of length n."""
    for i in range(n):
        if 2**i >= n + 1:
            return i

def detect_and_correct_error(hamming_data):
    """Detect and correct a single-bit error in the Hamming code if present."""
    n = len(hamming_data)
    r = calculate_redundant_bits_length(n)

    # Calculate the syndrome (error position)
    error_position = 0
    for i in range(r):
        parity_pos = 2**i
        count = 0
        for j in range(1, n + 1):
            if j & parity_pos == parity_pos:
                count += int(hamming_data[j - 1])
        if count % 2 != 0:
            error_position += parity_pos

    # Correct the error if error_position is non-zero
    if error_position != 0:
        print(f"Error detected at position: {error_position}")
        hamming_data = list(hamming_data)
        # Flip the bit at error_position
        hamming_data[error_position - 1] = '1' if hamming_data[error_position - 1] == '0' else '0'
        hamming_data = ''.join(hamming_data)
        print(f"Corrected Hamming Code: {hamming_data}")
    else:
        print("No error detected.")
    
    return hamming_data

def extract_original_data(hamming_data):
    """Extract the original data bits from Hamming code (excluding parity bits)."""
    n = len(hamming_data)
    original_data = []
    for i in range(1, n + 1):
        if i & (i - 1) != 0:  # Not a power of two position (i.e., not a parity bit)
            original_data.append(hamming_data[i - 1])
    
    return ''.join(original_data)

def binary_to_text(binary_data):
    """Convert binary string to ASCII text."""
    chars = [chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8)]
    return ''.join(chars)

def receiver():
    """Read Hamming code from Channel.txt, correct errors if any, and decode the data."""
    with open("Channel.txt", "r") as f:
        hamming_data = f.read().strip()

    print(f"Received Hamming Code: {hamming_data}")

    # Step 1: Detect and correct any single-bit error
    corrected_hamming_data = detect_and_correct_error(hamming_data)

    # Step 2: Extract original data (excluding parity bits)
    original_binary_data = extract_original_data(corrected_hamming_data)
    print(f"Extracted Binary Data: {original_binary_data}")

    # Step 3: Convert binary data back to text
    original_text = binary_to_text(original_binary_data)
    print(f"Decoded Text: {original_text}")

# Run the receiver
receiver()
