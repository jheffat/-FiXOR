# FiXOR 

> Is a file encryptor based on command line interface CLI. It is available for Windows, MacOSX and Linux. It can also be used as a script for any platform(for efficient operation, make sure you have python installed and the modules listed in requirements.txt here: [requirements.txt](https://github.com/icodexys/FiXOR-project/files/6921962/requirements.txt). Fixor was developed with python 3.8.7, so you should have that version or higher....For Windows users I recommend to install **Windows Terminal** from Microsoft store, it supports UNICODE.

**For Binary download go to** [http://icodexys.com](http://icodexys.com/)

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
> ### Example:
>
> - In binary mode:
>
>   - Windows platform:		
>
>   ```powershell
>   fixor -e *.exe
>   fixor -e mydiary.txt
>   fixor -d *.* -p G0dl!k334#
>   ```
>
>   

> * In Scripting mode:
>   * Windows platform:
>
>   ```powershell
>   python fixor.py -e *.exe
>   python fixor.py -e mydiary.txt
>   python fixor.py -d *.* -p G0dl!k334#
>   ```
> 

## -----Screenshots

#### *encryption*

`Ex: fixor -e *.mp3 -p D0y0ul0v3m3?` [![encrypt](https://user-images.githubusercontent.com/18588201/127971916-15df22f8-7d7f-47e2-85d3-d3f7a126dcb9.jpg)](https://user-images.githubusercontent.com/18588201/127971916-15df22f8-7d7f-47e2-85d3-d3f7a126dcb9.jpg)

#### *scanning files encrypted*

`Ex: fixor -s *.mp3` [![scanned](https://user-images.githubusercontent.com/18588201/127971964-467490ac-1ce1-454e-bfa1-6d9d504bbc75.jpg)](https://user-images.githubusercontent.com/18588201/127971964-467490ac-1ce1-454e-bfa1-6d9d504bbc75.jpg)

#### *List of files encrypted to be decrypted*

`Ex: fixor -d *.mp3 -p D0y0ul0v3m3?` [![tarlisttodecry](https://user-images.githubusercontent.com/18588201/127972065-6f2f6958-fb1e-4430-bb18-1c8bd977184d.jpg)](https://user-images.githubusercontent.com/18588201/127972065-6f2f6958-fb1e-4430-bb18-1c8bd977184d.jpg)

#### *during the decryption* [![decryp](https://user-images.githubusercontent.com/18588201/127972115-140c8f99-3f15-4fb5-a189-3510596bfe32.jpg)](https://user-images.githubusercontent.com/18588201/127972115-140c8f99-3f15-4fb5-a189-3510596bfe32.jpg)

#### *results with Checksum verified* [![resultdecryp](https://user-images.githubusercontent.com/18588201/127972248-e02b6add-b43e-4579-ac35-7d5cd28028f1.jpg)](https://user-images.githubusercontent.com/18588201/127972248-e02b6add-b43e-4579-ac35-7d5cd28028f1.jpg)
