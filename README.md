# Reverse Shell Attack
## References
- [TesKill - Trojan (#1) (Series)](https://www.youtube.com/watch?v=WLHlOg-ly2U)
- [axju](https://axju.de/posts/2021/02/a-reverse-shell-with-python/)
- [Rietesh Amminabhavi](https://medium.com/@rietesh/python-reverse-shell-hack-your-neighbours-552561336ca8)

## client.py
Executes a shell on the target machine. Need to be executed on the target machine to open the connection.
## server.py
Execute this file on the attacker machine. Acts as a listener. Obtains remote access while connected to `client.py`.
## Setup Environment
- Both files are safe to install and run (given that you're using it only for testing purposes), Windows Defender does not classify these files as a threat.
- You can also push both files to an isolated network and test it there.<br />

Find this line in `client.py` and comment it in: 
```python
print(f'[*] Receive: {cmd}')
```
```python
#print(f'[*] Receive: {cmd}')
```
Do this only if you don't want to receive the output of the commands being used by the server. 
## Objective
The objective of this program is to execute a reverse shell attack on vulnerable machines by establishing
a remote interactive shell. The incremental changes I will be adding to this repo will focus more on
writing scripts to automate payloads, as well as add minor changes/fix bugs. 
