#!/bin/sh
# This script is used for downloading package source tarball under Archlinux,  just like apt-get source pkg in ubuntu.

#make sure abs is installed
pacman -Q abs >/dev/null 2>&1
if [ $? -ne 0 ];then
    echo "abs is not installed."
    echo "installing abs..."
    if [ `whoami` == "root" ];then
        pacman -S abs 
        abs -t
    else
        sudo pacman -S abs 
        if [ $? -ne 0 ];then
            exit
        fi  
        sudo abs -t
    fi  
fi

#geting source through the PKGBUILD file
find /var/abs -type d -name $1 -exec cp -a {} /tmp/ \;
if [  -d /tmp/$1 ];then
    echo package found.
else
    echo package not found.
    exit
fi
pushd /tmp/$1 >/dev/null 2>&1
sed -i 's:\./configure.*$:exit:' PKGBUILD
if [ `whoami` == "root" ];then
	makepkg --asroot
else
	makepkg
fi
popd >/dev/null 2>&1
cp -a /tmp/$1/src ./$1 >/dev/null 2>&1
