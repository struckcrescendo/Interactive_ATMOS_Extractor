# Interactive_ATMOS_Extractor
Python script that extracts Dolby ATMOS channels into your liking

This Python script allows you to extract individual audio channels from Dolby Digital Plus 5.1 .m4a files. It will convert each channel into a separate mono audio file (e.g., WAV, FLAC, AAC, MP3) and organize them into folders based on your album and song names.
Prerequisites: FFmpeg

This script relies on FFmpeg, a powerful command-line tool for audio and video processing. You must have FFmpeg installed on your system before running this script.
macOS and Linux Guide

The easiest way to install FFmpeg on macOS and most Linux distributions is using a package manager.

    Install Homebrew (macOS) or your system's package manager (Linux):

        macOS (Homebrew): If you don't have Homebrew, open your Terminal and run:

        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

        Follow any on-screen instructions.

        Linux (apt, dnf, pacman, etc.): Use your distribution's package manager. For example, on Debian/Ubuntu:

        sudo apt update
        sudo apt install ffmpeg

        On Fedora/CentOS:

        sudo dnf install ffmpeg

        On Arch Linux:

        sudo pacman -S ffmpeg

    Install FFmpeg:

        macOS (with Homebrew):

        brew install ffmpeg

        Optional for MP3 output: If you want to extract to MP3, ensure FFmpeg has libmp3lame support. Homebrew usually includes this, but if you encounter issues, you might need to reinstall FFmpeg with specific options (though this is less common now):

        brew reinstall ffmpeg --with-lame # This command might vary based on ffmpeg versions

    Verify Installation:
    Open a new Terminal window and run:

    ffmpeg -version

    You should see information about your FFmpeg installation.

Windows Guide

Installing FFmpeg on Windows typically involves downloading the binaries.

    Download FFmpeg:

        Go to the official FFmpeg download page: https://ffmpeg.org/download.html

        Under the "Get the packages" section, click the Windows icon.

        Choose a link from a reputable source (e.g., "Gyan" or "BtbN"). Download the release build (not a git master build). A .zip or .7z file will be downloaded.

    Extract FFmpeg:

        Create a new folder on your C: drive, for example, C:\ffmpeg.

        Extract the contents of the downloaded .zip (or .7z) file into this C:\ffmpeg folder. You should see bin, doc, licenses, and presets folders inside C:\ffmpeg. The ffmpeg.exe file will be in the bin folder (e.g., C:\ffmpeg\bin).

    Add FFmpeg to your System PATH:
    This step allows you to run ffmpeg commands from any directory in Command Prompt or PowerShell.

        Search for "Environment Variables" in the Windows search bar and select "Edit the system environment variables."

        In the System Properties window, click "Environment Variables...".

        Under "System variables," find and select the Path variable, then click "Edit...".

        Click "New" and add the path to your ffmpeg.exe's bin folder (e.g., C:\ffmpeg\bin).

        Click "OK" on all open windows to save the changes.

    Verify Installation:
    Open a new Command Prompt or PowerShell window (it won't work in existing ones before the Path update) and run:

    ffmpeg -version

    You should see information about your FFmpeg installation.

How to Use the Python Script

    Save the Script:

        Copy the Python code provided in the "Interactive M4A Dolby Digital Plus Channel Extractor" Canvas document.

        Save it as a Python file (e.g., extract_audio.py) on your computer (e.g., on your Desktop or in your Documents folder).

    Run the Script:

        Open your Terminal (macOS/Linux) or Command Prompt/PowerShell (Windows).

        Navigate to the directory where you saved extract_audio.py using the cd command. For example:

            If saved on Desktop: cd ~/Desktop (macOS/Linux) or cd %USERPROFILE%\Desktop (Windows)

            If saved in Documents: cd ~/Documents (macOS/Linux) or cd %USERPROFILE%\Documents (Windows)

        Run the script using python3 (macOS/Linux) or python (Windows, if python3 doesn't work):

        python3 extract_audio.py

        or

        python extract_audio.py

    Follow the Prompts:
    The script will guide you through the process by asking three questions:

        "Enter the full path to the folder containing your M4A files (e.g., /Users/ace/Music/BWU_ATMOS/Serotonin):"

            Enter the complete path to the folder that contains the .m4a files for a specific album (e.g., /Users/ace/Music/BWU_ATMOS/Serotonin or C:\Users\YourUser\Music\URBAN_ATMOS\ThrillSeeker).

        "Enter the desired output format for extracted channels (wav, flac, aac, mp3) [default: wav]:"

            Type your preferred output format.

            wav: Uncompressed, high quality (default if you press Enter without typing).

            flac: Lossless compressed, good for archiving.

            aac: Compressed (lossy), good for general use.

            mp3: Compressed (lossy), widely compatible.

            Press Enter to accept the default (wav), or type one of the other options and press Enter.

        "Enter the full path to the base folder where you want the extracted channels to be saved (e.g., /Users/ace/ExtractedAudio):"

            Enter the complete path to a new or existing folder where you want all your extracted albums to be organized.

            For example, if you enter /Users/ace/ExtractedAudio (macOS/Linux) or C:\ExtractedMusic (Windows), the script will create a subfolder for the album (e.g., Serotonin), and then subfolders for each song within that.

Output Folder Structure

After extraction, your files will be organized as follows:

[Your Chosen Base Output Folder]/
└── [Album Folder Name (from your input)]/
    ├── [Song Name 1]/
    │   ├── [Song Name 1]_Front_Left.[Format]
    │   ├── [Song Name 1]_Front_Right.[Format]
    │   ├── [Song Name 1]_Center.[Format]
    │   ├── [Song Name 1]_LFE.[Format]
    │   ├── [Song Name 1]_Surround_Left.[Format]
    │   └── [Song Name 1]_Surround_Right.[Format]
    └── [Song Name 2]/
        ├── [Song Name 2]_Front_Left.[Format]
        └── ... (and so on)

Troubleshooting

    FileNotFoundError: [Errno 2] No such file or directory:

        This means the script can't find the input folder you provided. Double-check the path you entered. Ensure it's the full, absolute path to the directory containing your .m4a files.

        Ensure there are no typos in the path.

    ERROR: FFmpeg not found.

        This means FFmpeg is either not installed or not correctly added to your system's PATH. Revisit the "Prerequisites: FFmpeg" section for your operating system.

    FFmpeg command failed with error code X

        This indicates an issue with the FFmpeg command itself. The Stderr output (printed in the terminal) often contains more specific details about why FFmpeg failed. Common reasons include:

            Corrupted input .m4a files.

            Permissions issues writing to the output directory (ensure the Python script has write access to the chosen output folder).

            Missing libmp3lame for MP3 output (if applicable).

        Review the Stderr output for clues.
