## onkyoqt - GUI for [Onkyo](http://www.onkyo.com/) receivers
### Python2 only :( , But QT5

# Index
1. [Install dependencies](#installdeps)
2. [Install](#install)
3. [Run](#run)
4. [Configure](#conf)
5. [Known issues](#issues)

![Screenshot of onkyoqt](https://github.com/massdest/onkyoqtpy/raw/master/screenshot1.png)

![Screenshot of onkyoqt](https://github.com/massdest/onkyoqtpy/raw/master/screenshot2.png)

### Install dependencies, for Debian/Ubuntu <a name="installdeps"></a>
```
sudo apt-get install python-pyqt5 pyqt5-dev-tools qttools5-dev-tools python-pip python git
sudo pip2 install onkyo-eiscp
```
### Install <a name="install"></a>

#### From Git

`git clone https://github.com/massdest/onkyoqtpy.git ; cd onkyoqtpy ; sudo python2 setup.py install`

#### From Pip

`sudo pip2 install onkyoqt`

### Run <a name="run"></a>

`/usr/local/bin/onkyoqt`

or from application menu Multimedia

### Set IP in settings and restart application: <a name="conf"></a> 

**File->Settings->Receiver IP**

### Known Issues <a name="issues"></a>

Application start work about 30-60 seconds after receiver powered on, so be patient. 
