[![intro](https://user-images.githubusercontent.com/18588201/127971655-56263ef3-140c-4e82-93e4-ee1f7940e0f8.jpg)](https://user-images.githubusercontent.com/18588201/127971655-56263ef3-140c-4e82-93e4-ee1f7940e0f8.jpg)

# FiXOR 

> Is a file encryptor based on command line interface CLI. It is available in binary for Windows, MacOSX and Linux. It can also be used as a script for any platform(for efficient operation, make sure you have python installed and the modules listed in requirements.txt here: [requirements.txt](https://github.com/icodexys/FiXOR-project/files/6921962/requirements.txt). Fixor was developed with python 3.8.7, so you should have that version or higher....For Windows users I recommend to install **Windows Terminal** from Microsoft store, it supports UNICODE.

**For Binary download go to** [http://icodexys.com](http://icodexys.com/)

> Fixor 2.11 has new improvements, one of them is:
>
> - Passwords are no longer encrypted and not saved for security reasons, only uses avanced Password hashing algorithm.
> - It also contains the verification of data integrity using the sha256 hash algorithm, with it we can ensure that the file has been successfully decrypted or not.
> - You can make the encryption or decryption process even faster.

**NOTE**: *FIXOR 1.0 no longer supported but still here for python learners.*

## ------USAGE:

> Fixor OPTION TARGET | PASSWORD
>
> TARGET---> Path\Filename*.*
>
> OPTION---> -e to encrypt, -d to decrypt and -s scan encrypted files.
>
> PASSWORD---> -p specify a quick password to encrypt/decrypt [OPTIONAL]
>
> ------Example:
>
> `fixor -e mydiary.txt`
>
> `fixor -d c:\my downloads\handrew.jpg`
>
> `fixor -e *.exe`
> 
> `fixor -d *.* -p G0dl!k334#`
> 
>  ![icon](https://user-images.githubusercontent.com/18588201/128962463-2cdac61e-2a66-41e9-9b1e-aeada84d443a.png)
>  Linux/Macosx users Attention!!!!, in orde to use fixor:

>  - The wildcards or target must have " " or  ' '
>  - Need to be root user or use SUDO
> 
> `sudo fixor -e "*.exe"`
> 
> `sudo fixor -e "mydiary.txt"`
> 
> `sudo fixor -d "*.*" -p G0dl!k334#`

## -----Screenshots from Windows platform

#### *encryption*

`Ex: fixor -e *.mp3 -p D0y0ul0v3m3?` [![encrypt](https://user-images.githubusercontent.com/18588201/127971916-15df22f8-7d7f-47e2-85d3-d3f7a126dcb9.jpg)](https://user-images.githubusercontent.com/18588201/127971916-15df22f8-7d7f-47e2-85d3-d3f7a126dcb9.jpg)

#### *scanning files encrypted*

`Ex: fixor -s *.mp3` [![scanned](https://user-images.githubusercontent.com/18588201/127971964-467490ac-1ce1-454e-bfa1-6d9d504bbc75.jpg)](https://user-images.githubusercontent.com/18588201/127971964-467490ac-1ce1-454e-bfa1-6d9d504bbc75.jpg)

#### *List of files encrypted to be decrypted*

`Ex: fixor -d *.mp3 -p D0y0ul0v3m3?` [![tarlisttodecry](https://user-images.githubusercontent.com/18588201/127972065-6f2f6958-fb1e-4430-bb18-1c8bd977184d.jpg)](https://user-images.githubusercontent.com/18588201/127972065-6f2f6958-fb1e-4430-bb18-1c8bd977184d.jpg)

#### *during the decryption* [![decryp](https://user-images.githubusercontent.com/18588201/127972115-140c8f99-3f15-4fb5-a189-3510596bfe32.jpg)](https://user-images.githubusercontent.com/18588201/127972115-140c8f99-3f15-4fb5-a189-3510596bfe32.jpg)

#### *results with Checksum verified* [![resultdecryp](https://user-images.githubusercontent.com/18588201/127972248-e02b6add-b43e-4579-ac35-7d5cd28028f1.jpg)](https://user-images.githubusercontent.com/18588201/127972248-e02b6add-b43e-4579-ac35-7d5cd28028f1.jpg)
