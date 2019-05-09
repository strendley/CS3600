# Programming assignment 2 (pa02) -- Binary One Time Pad

Binary XOR operations are all over modern crypto, and this is a fun version of "perfect" crypto using this method.
You are making a binary one-time-pad program, which has two parts:

1. A python3 script named and executed as follows `$ python3 bin_otp_key_gen.py keyfile.sec` should output a utf-8 unix delimited text file of 500 numbered OTP keys, 1-per-line, with each key 2048 characters (bits) long.
Make sure to use a cryptographically strong random key generation method (e.g., secrets, urandom, /dev/random)
Each line should have a 3-digit number with leading 0s, starting with 001, followed by a single space, and a 2048bit key.
For example:

    keyfile.sec would have 

    ```
    001 1010101101010101010...
    002 1010101001010100101...
    .
    .
    .
    500 1010101001010100111...
    ```

    The general format is:

    `$ ./bin_otp_key_gen.py <keyfiletowrite>`

    or

    `$ python3 bin_otp_key_gen.py <keyfiletowrite>`

2. A python3 script named and executed (for example) as follows `$ ./bin_otp.py keyfile.sec 3 inputfile.txt outputfile.txt` should turn the text in inputfile.txt into a bitstring, XOR it with the 3rd key in the keyfile.sec, translate back to readable utf-8 text, and write the converted data to outputfile.txt. 
Thus, the script should work symmetrically, encrypting or decrypting.
The encrypted message may look like ASCII junk, so don't worry if it does!
Input parameters could be named any valid filename, and the general format is: 

    `$ ./bin_otp.py <keyfile> <keynum> <inputfile> <outputfile>`
    
    or 

    `$ python3 bin_otp.py <keyfile> <keynum> <inputfile> <outputfile>`

## What to submit
* You could have testing files like messages and keys in the repository, but just the two python scripts are necessary.
* If you need any imports, do make sure to add them to your repos (within reason).

## General notes:
* Write this from scratch (without for example using a OTP library, or book code).
  Python standard library is ok.
* Read the syllabus procedures about file format and code running environment.
* The scripts are expected to run in an up-to-date Debian stable install, in Python3.

## Notes:
* The message length will always be the exact length of the key in binary, so you don't have to pad or un-pad the message. 
* You don't need to do anything special for UTF-8 and Linux/Unix newlines, which are default for Python's read/write, and just happen by default if you are using the VM (not copy-pasting from Windows host, which is NOT recommended). 
* You can use byte or byte array objects in python, but the easiest thing to do may be the simple low-level handling of characters to binary, and then back, e.g.,
    * Turn the first character into a ascii code, then that number into an 8-bit string, and appending the same for all following characters. 
    * If you use the byte objects, be careful, because the can ambiguously encode larger or smaller chunks as a character.
    * You don't need to read/write files in binary mode, the files should just be text characters!
* When you write the encrypted file, it should be in ascii (not the binary string), so that the operations are entirely symmetrical. 

