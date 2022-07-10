# FiXOR 

> Is a file encryptor based on command line interface CLI. It is available for Windows, MacOSX and Linux. It can also be used as a script for any platform(for efficient operation, make sure you have python installed and the modules listed in requirements.txt here: [requirements.txt](https://github.com/icodexys/FiXOR-project/files/6921962/requirements.txt). Fixor was developed with python 3.8.7, so you should have that version or higher....For Windows users I recommend to install **Windows Terminal** from Microsoft store, it supports UNICODE.

**For executable download go to** [http://icodexys.com](http://icodexys.com/)

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
>   ```
>   fixor -e *.exe
>   fixor -e mydiary.txt
>   fixor -d *.* -p G0dl!k334#
>   ```
>
> * In Scripting mode:
>  
>  * >>>>Windows
>   ```powershell
>   python fixor.py -e *.exe
>   python fixor.py -e mydiary.txt
>   python fixor.py -d *.* -p G0dl!k334#
>   ```
>* >>>>Linux/MacOSX
>   ```powershell
>   python fixor.py -e "*.exe"
>   python fixor.py -e "mydiary.txt"
>   python fixor.py -d "*.*" -p G0dl!k334#
>   ```

## -----IN ACTION

#### *encryption*

https://user-images.githubusercontent.com/18588201/178131667-2c39deb0-dfa5-41b4-b7c5-0d602b758b1c.mp4


#### *scanning files encrypted*

https://user-images.githubusercontent.com/18588201/178131811-15ff836a-5878-447d-9ffe-b65a5810c93b.mp4


#### *during the decryption* 

https://user-images.githubusercontent.com/18588201/178131826-ec91ff2a-a114-4a42-bd84-3f9a0a5f1447.mp4

