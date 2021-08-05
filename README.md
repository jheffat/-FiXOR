![intro](https://user-images.githubusercontent.com/18588201/127971655-56263ef3-140c-4e82-93e4-ee1f7940e0f8.jpg)




#FiXOR
is a file encryptor that allows it not to be readable by human or by a specific program, it is based on command line interface CLI. It is available in binary for Windows, MacOX and Linux. It can also be used as a script for any platform(for efficient operation, make sure you have python installed and the modules listed in requirements.txt here: [requirements.txt](https://github.com/icodexys/FiXOR-project/files/6921962/requirements.txt). Fixor was developed with python 3.8.7....For Windows users I recommend to install Windows Terminal from Microsoft store, it has UNICODE supported.

For Binary download go to http://icodexys.com

Fixor 2.11 has new improvements, one of them is:

1-Passwords are no longer encrypted and not saved for security reasons, only uses avanced Password hashing algorithm.

2-It also contains the verification of data integrity using the sha256 hash algorithm, with it we can ensure that the file has been successfully decrypted or not.

3-You can make the encryption or decryption process even faster.


NOTE: FIXOR 1.0 no longer supported but still here for python learners.


------USAGE:

Fixor OPTION TARGET | PASSWORD

TARGET---> Path\Filename\*.*

OPTION---> -e to encrypt, -d to decrypt and -s scan encrypted files.

PASSWORD---> -p specify a quick password to encrypt/decrypt [OPTIONAL]

------Example: 

fixor -e mydiary.txt

fixor -d c:\my downloads\handrew.jpg

fixor -e *.exe

fixor -d  *.* -p G0dl!k334#


-----Screenshots

*encryption

Ex: fixor -e *.mp3 -p D0y0ul0v3m3?
![encrypt](https://user-images.githubusercontent.com/18588201/127971916-15df22f8-7d7f-47e2-85d3-d3f7a126dcb9.jpg)


*scanning files encrypted

Ex: fixor -s *.mp3
![scanned](https://user-images.githubusercontent.com/18588201/127971964-467490ac-1ce1-454e-bfa1-6d9d504bbc75.jpg)


*List of files encrypted to be decrypted

Ex: fixor -d *.mp3 -p D0y0ul0v3m3?
![tarlisttodecry](https://user-images.githubusercontent.com/18588201/127972065-6f2f6958-fb1e-4430-bb18-1c8bd977184d.jpg)


*during the decryption
![decryp](https://user-images.githubusercontent.com/18588201/127972115-140c8f99-3f15-4fb5-a189-3510596bfe32.jpg)


*results with Checksum verified
![resultdecryp](https://user-images.githubusercontent.com/18588201/127972248-e02b6add-b43e-4579-ac35-7d5cd28028f1.jpg)








