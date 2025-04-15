# FiXOR 

```text
#       /$$ /$$                                           /$$     /$$                                     /$$
#      | $$|__/                                          | $$    |__/                                    | $$
#  /$$$$$$$ /$$  /$$$$$$$  /$$$$$$$  /$$$$$$  /$$$$$$$  /$$$$$$   /$$ /$$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$$
# /$$__  $$| $$ /$$_____/ /$$_____/ /$$__  $$| $$__  $$|_  $$_/  | $$| $$__  $$| $$  | $$ /$$__  $$ /$$__  $$
#| $$  | $$| $$|  $$$$$$ | $$      | $$  \ $$| $$  \ $$  | $$    | $$| $$  \ $$| $$  | $$| $$$$$$$$| $$  | $$
#| $$  | $$| $$ \____  $$| $$      | $$  | $$| $$  | $$  | $$ /$$| $$| $$  | $$| $$  | $$| $$_____/| $$  | $$
#|  $$$$$$$| $$ /$$$$$$$/|  $$$$$$$|  $$$$$$/| $$  | $$  |  $$$$/| $$| $$  | $$|  $$$$$$/|  $$$$$$$|  $$$$$$$
# \_______/|__/|_______/  \_______/ \______/ |__/  |__/   \___/  |__/|__/  |__/ \______/  \_______/ \_______/````

![Screenshot (5)](https://user-images.githubusercontent.com/18588201/208356258-1c7a7002-d7d1-45df-b8ad-96419743b9b6.png)

>It is a script written in Python that encrypts any type of file. The new version comes with a more sophisticated AES-128 encryption. The previous version 2.50 only worked with a simple XOR encryption, in the new version you can choose to encrypt a file with AES or XOR. Executable Download([http://icodexys.com](http://icodexys.com/)).

When the file is encrypted, metadata is stored inside the file. The metadata contains original information such as the size, name, date, password(hashed by BCrypt) etc... Parameters detailed below:

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

**NOTE**: *FIXOR 1.0  I'll keep it here since is my first version made in python*

**NOTE 2**: *FIXOR 2.50  Discontinued since new innovation has made but source code still available.*

## -----IN ACTION

#### *encryption*

https://user-images.githubusercontent.com/18588201/178131667-2c39deb0-dfa5-41b4-b7c5-0d602b758b1c.mp4


#### *scanning  encrypted files*

https://user-images.githubusercontent.com/18588201/178131811-15ff836a-5878-447d-9ffe-b65a5810c93b.mp4


#### *during the decryption* 

https://user-images.githubusercontent.com/18588201/178131826-ec91ff2a-a114-4a42-bd84-3f9a0a5f1447.mp4

