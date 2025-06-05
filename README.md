# Interactive_ATMOS_Extractor
Python script that extracts Dolby ATMOS channels into your liking

This Python script allows you to extract individual audio channels from Dolby Digital Plus 5.1 .m4a files. It will convert each channel into a separate mono audio file (e.g., WAV, FLAC, AAC, MP3) and organize them into folders based on your album and song names.
Prerequisites: FFmpeg

This script relies on FFmpeg, a powerful command-line tool for audio and video processing. You must have FFmpeg installed on your system before running this script.
macOS and Linux Guide

# ***WARNING***
This has ***NOT*** been tested on Linux and Windows only on MacOS Sonoma, though it will most likely work either way if you follow installation ***correctly***
If theres a problem with installation guide, then email me at ace@struckcrescendo.band
I will try and fix it in a reasonable time (you will be the first to have it), and if you have any question you can email me.

# **INSTALLATION**

## MacOS and Linux

### **PYTHON**

Go to [this page](https://www.python.org/downloads/)
Download 3.13.4 and run the installer.
Once done test that your Terminal has python installed by running the 
```
python3
```
command, if it works, then you will be sent to the python command line, you want to exit using the command
```
exit
```

### **HOMEBREW INSTALL**

If you already have Homebrew you can skip this, but follow the instructions on the Homebrew website to install it. https://brew.sh/

### **FFMPEG**

Again, skip if you already have FFMPEG installed
In your terminal run the command 
```
brew install ffmpeg
```

### **Actual Program**

Go to this page and download the atmos_extractor.py file, you can put it where you want
Then in your terminal, you want to enter the folder you put the atmos_extractor.py file in, then run
```
python3 atmos_extractor.py
```
After this follow the instructions and you have used it!

## Windows

### **Python**

Go to [this page](https://www.python.org/downloads/)
Download 3.13.4 and run the installer.
Once done test that your Terminal has python installed by running the 
```
python3
```
command, if it works, then you will be sent to the python command line, you want to exit using the command
```
exit
```

### **FFMPEG**

Follow [this guide](https://phoenixnap.com/kb/ffmpeg-windows) to install FFMPEG

### **Actual Program**

Go to this page and download the atmos_extractor.py file, you can put it where you want
Then in your command prompt, you want to enter the folder you put the atmos_extractor.py file in, then run
```
python3 atmos_extractor.py
```
After this follow the instructions and you have used it!
