#!/bin/sh

# compile
pyinstaller -F dd-gui.py

# copy the libs
if [ `uname` == "FreeBSD" ]
then
	mkdir -p dist/platforms
	cp -fv /usr/local/lib/qt5/plugins/platforms/* dist/platforms/
fi

# clean
rm -rf build
rm -rf *.spec
