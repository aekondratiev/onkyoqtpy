## onkyoqt - GUI for [Onkyo](http://www.onkyo.com/) receivers
### Python2 only :( , But QT5

![Screenshot of onkyoqt](https://github.com/massdest/onkyoqtpy/raw/master/screenshot1.png)

![Screenshot of onkyoqt](https://github.com/massdest/onkyoqtpy/raw/master/screenshot2.png)

### Install deps, for Debian/Ubuntu
```
sudo apt-get install python-pyqt5 pyqt5-dev-tools qttools5-dev-tools python-pip python git
sudo pip2 install onkyo-eiscp
```
### Set IP in settings and restart application: 

**File->Settings->Receiver IP**

### Install

#### From Git

`git clone https://github.com/massdest/onkyoqtpy.git ; cd onkyoqtpy ; sudo python2 setup.py install`

#### From Pip

`sudo pip2 install onkyoqt`

### Run

`/usr/local/bin/onkyoqt`

or from application menu Multimedia


