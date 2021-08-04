# Reverse Shell
## References
- [TesKill - Trojan (#1) (Series)](https://www.youtube.com/watch?v=WLHlOg-ly2U)
- [axju](https://axju.de/posts/2021/02/a-reverse-shell-with-python/)
- [Rietesh Amminabhavi](https://medium.com/@rietesh/python-reverse-shell-hack-your-neighbours-552561336ca8)

## server.py
Execute this file first. Must be on the attacker host. Acts as a listener. Obtains remote access while connected to `client.py`.
## client.py
Executes a shell on the target host. Need to be executed to open the connection. Will not work without the `server.py` running.
## Setup Environment
- Both files are safe to install and run (given that you're using it only for testing purposes), Windows Defender does not classify these files as a threat.
- You can also push both files to an isolated network and test it there.<br />

To test on two different hosts, (attacker vs. target) find this line in both files and change the server address `0.0.0.0` to your attacker's IP address.
```python
host = sys.argv[1] if len(sys.argv) > 1 else '0.0.0.0' #server IP
```
Find this line in `client.py` and comment it out: 
```python
print(f'[*] Receive: {cmd}')
```
```python
#print(f'[*] Receive: {cmd}')
```
Do this only if you don't want the client to receive the output of the commands being used by the server.<br />
Convert both scripts to `.exe` to run it on Windows.
## Objective
The objective of this program is to execute a reverse shell attack on vulnerable machines by establishing
a remote interactive shell. The incremental changes I will be adding to this repo will focus more on
writing scripts to automate payloads, as well as add minor changes/fix bugs. 
