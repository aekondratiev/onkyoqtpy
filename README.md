## onkyotq - GUI for onkyo recivers
### Python2 only :(
### Install deps, for Ununtu
```
sudo aptitude install python-pyqt5 pyqt5-dev-tools qttools5-dev-tools python-pip python
sudo pip2 install onkyo-eiscp
```
### Change IP in file: 

`onkyoqt/onkyoqt.py`

host = "192.168.1.9" (mine is 192.168.1.9, use your own ip of reciver)

### Install

`git clone https://github.com/massdest/onkyoqtpy.git ; cd onkyoqtpy ; sudo python2 setup.py install`

### Run

`/usr/local/bin/onkyoqt`

or from application menu Multimedia

