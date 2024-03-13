# Non-Destructive Text Codecs

## Introduction
This project explores various lossless text compression methods, detailing their functionality and effectiveness across different types of text, such as literary texts, programming code, and random characters. Our goal is to deepen our understanding of non-destructive text codecs and determine the most suitable codecs for our use.

## Algorithms
### Transformations
- **Burrows-Wheeler Transform**: A pre-processing method that enhances redundancy patterns to reduce entropy.
- **Move-to-Front**: Efficient for texts where certain character sets frequently appear together.

### Dictionary-Based Compression Techniques
- **LZ77**: Utilizes a moving window technique for pattern matching.
- **LZW**: Compares symbols against a dictionary and encodes the longest match.

### Entropy-Based Compression Techniques
- **Huffman Coding**: Builds a binary tree based on symbol occurrence probabilities to generate optimal codes.
- **Arithmetic Coding**: Assigns fixed-size binary codes based on symbol occurrence order.

### Others
- **RLE (Run-Length Encoding)**: Encodes sequences of repeated characters to reduce file size.

### Complex Algorithms
- **Deflate**: Used in ZIP files, combines LZ77 with Huffman coding.
- **bzip2**: Employs multiple algorithms including Burrows-Wheeler Transform and Huffman coding.
- **LZMA**: An enhanced LZ77 variant with additional optimizations.

## Developed Algorithms
### Our Variant Compress
A LZW-inspired algorithm that simulates a real dictionary to encode text efficiently.

### Myhuffman
A Huffman coding variant designed for texts consisting solely of numbers (0-9).

## Selected Algorithms for File Compression
- **Random.txt**: Encoded using Huffman coding due to the randomness of characters.
- **Jquery-3.6.0.js**: Compressed using LZW followed by Huffman coding to exploit code redundancies.
- **Bible.txt**: Utilizes the 'Variant Compress' algorithm followed by Huffman coding to leverage word repetitions.
- **Finance.csv**: Employs 'Variant Compress' with a focus on comma-separated sequences, followed by Huffman coding.

## Results
The compression factors achieved for each file type are detailed, demonstrating the effectiveness of the selected algorithms.
