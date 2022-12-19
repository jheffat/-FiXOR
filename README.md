# FiXOR 

![Screenshot (5)](https://user-images.githubusercontent.com/18588201/208356258-1c7a7002-d7d1-45df-b8ad-96419743b9b6.png)

>is a file encryptor based on Command Line interface, it can be executed as a script to be used in Windows and Linux/MacosX (requires privileged user). To accomplish that task you need to install certain modules listed in [requirements.txt](https://github.com/icodexys/FiXOR-project/files/6921962/requirements.txt) and install python 3.8.9 or earlier. FiXOR project is also written in C# (Still in Development).... Is also available as a standalone executable for windows at [http://icodexys.com](http://icodexys.com/) .

As soon as the file is encrypted, a metadata is stored inside the file, in which it contains original information such as size, name, date, and hashed password (difficult to apply brute force). Its execution must be with parameters listed below:

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
> - In Executable mode:
>
>   ```
>   fixor -e *.exe
>   fixor -e mydiary.txt
>   fixor -d *.* -p G0dl!k334#
>   ```
>
> - In Scripting mode:
>  
>    **Windows**
>   ```powershell
>      python fixor.py -e *.exe
>      python fixor.py -e mydiary.txt
>      python fixor.py -d *.* -p G0dl!k334#
>   ```
>    **Linux/MacOSX**
>   ```powershell
>      python fixor.py -e "*.exe"
>      python fixor.py -e "mydiary.txt"
>      python fixor.py -d "*.*" -p G0dl!k334#
>   ```

**NOTE**: *FIXOR 1.0  I keep it here since is my firstversion made in python*

## -----IN ACTION

#### *encryption*

https://user-images.githubusercontent.com/18588201/178131667-2c39deb0-dfa5-41b4-b7c5-0d602b758b1c.mp4


#### *scanning  encrypted files*

https://user-images.githubusercontent.com/18588201/178131811-15ff836a-5878-447d-9ffe-b65a5810c93b.mp4


#### *during the decryption* 

https://user-images.githubusercontent.com/18588201/178131826-ec91ff2a-a114-4a42-bd84-3f9a0a5f1447.mp4

