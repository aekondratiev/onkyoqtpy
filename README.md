## onkyoqt - GUI for onkyo recivers
### Python2 only :( , But QT5

![Screenshot of onkyoqt](https://github.com/massdest/onkyoqtpy/raw/master/onkyoqt_screenshot.png)

### Install deps, for Ununtu
```
sudo apt-get install python-pyqt5 pyqt5-dev-tools qttools5-dev-tools python-pip python
sudo pip2 install onkyo-eiscp
```
### Change IP in file: 

`onkyoqt/onkyoqt.py`

`host = "192.168.1.9"` (mine is 192.168.1.9, use your own ip of reciver)

### Install

`git clone https://github.com/massdest/onkyoqtpy.git ; cd onkyoqtpy ; sudo python2 setup.py install`

### Run

`/usr/local/bin/onkyoqt`

or from application menu Multimedia

### Known issues

`__settings.ini` dont work for now, dont edit it. 


