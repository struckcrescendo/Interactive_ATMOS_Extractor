import os
import subprocess
import re # Import regex for path validation

def extract_dolby_digital_plus_channels(input_directory, output_root_directory, output_format):
    """
    Extracts individual channels from Dolby Digital Plus 5.1 m4a files.
    Each channel will be saved as a separate mono file in the specified format
    within a new folder structure:
    [Output Root]/[Album Folder Name]/[Song Name]/[Song Name]_[Channel Name].[Format]

    Args:
        input_directory (str): The path to the directory containing the m4a files (e.g., /Users/ace/Music/BWU_ATMOS/Serotonin).
        output_root_directory (str): The base directory where all extracted files will be placed.
        output_format (str): The desired output audio format (e.g., 'wav', 'flac', 'aac', 'mp3').
    """
    print(f"\nStarting channel extraction process...")
    print(f"Input Directory: {input_directory}")
    print(f"Output Root Directory: {output_root_directory}")
    print(f"Output Format: {output_format.upper()}")

    # Define the standard 5.1 channel names and their corresponding FFmpeg map_name for channelsplit
    channels_info = [
        {"name": "Front Left", "map_name": "FL"},
        {"name": "Front Right", "map_name": "FR"},
        {"name": "Center", "map_name": "C"},
        {"name": "LFE", "map_name": "LFE"},
        {"name": "Surround Left", "map_name": "SL"},
        {"name": "Surround Right", "map_name": "SR"},
    ]

    # Determine FFmpeg audio codec arguments based on the desired output format
    audio_codec_args = []
    if output_format == 'wav':
        audio_codec_args = ["-acodec", "pcm_s16le"] # Standard uncompressed WAV
    elif output_format == 'flac':
        audio_codec_args = ["-acodec", "flac"] # Lossless FLAC
    elif output_format == 'aac':
        audio_codec_args = ["-acodec", "aac", "-b:a", "256k"] # AAC with 256kbps bitrate
    elif output_format == 'mp3':
        audio_codec_args = ["-acodec", "libmp3lame", "-q:a", "2"] # MP3 with quality 2 (VBR, high quality)
        print("NOTE: For MP3 output, ensure FFmpeg was compiled with 'libmp3lame' support (e.g., `brew install ffmpeg --with-lame` on macOS).")
    else:
        print(f"WARNING: Unknown output format '{output_format}'. Defaulting to WAV (PCM S16LE).")
        audio_codec_args = ["-acodec", "pcm_s16le"]
        output_format = 'wav' # Update format for consistent file naming

    try:
        # Get the name of the album folder from the input_directory
        album_folder_name = os.path.basename(os.path.normpath(input_directory))
        print(f"Detected album folder name: '{album_folder_name}'")

        # Iterate through all files in the specified input directory
        for filename in os.listdir(input_directory):
            if filename.endswith(".m4a"):
                input_filepath = os.path.join(input_directory, filename)
                # Create a folder name based on the m4a file's name (without extension)
                song_folder_name = os.path.splitext(filename)[0]

                # Construct the full output path: [Output Root]/[Album]/[Song]/
                output_folder_path = os.path.join(output_root_directory, album_folder_name, song_folder_name)

                # Create the output folder if it doesn't exist
                os.makedirs(output_folder_path, exist_ok=True)

                print(f"\n--- Processing '{filename}' ---")
                print(f"Output will be saved in: '{output_folder_path}'")

                # Build the filter_complex string for channelsplit
                filter_complex_str = "channelsplit=channel_layout=5.1"
                for channel in channels_info:
                    filter_complex_str += f"[{channel['map_name']}]"

                # Build the list of output mappings and file paths
                output_map_args = []
                for channel in channels_info:
                    channel_name_formatted = channel["name"].replace(" ", "_")
                    output_filename = f"{song_folder_name}_{channel_name_formatted}.{output_format}"
                    output_filepath = os.path.join(output_folder_path, output_filename)
                    output_map_args.extend(["-map", f"[{channel['map_name']}]", output_filepath])

                # FFmpeg command using channelsplit filter
                ffmpeg_command = [
                    "ffmpeg",
                    "-i", input_filepath,
                    "-filter_complex", filter_complex_str,
                    "-ac", "1", # Ensure each output stream is mono
                    "-y",      # Overwrite output files without asking
                ]
                ffmpeg_command.extend(audio_codec_args) # Add the chosen audio codec arguments
                ffmpeg_command.extend(output_map_args) # Add all the -map and output file arguments

                print(f"  Extracting all channels...")
                try:
                    # Run the FFmpeg command
                    subprocess.run(ffmpeg_command, check=True, capture_output=True, text=True)
                    print(f"    Successfully extracted all channels to '{output_folder_path}'")
                except subprocess.CalledProcessError as e:
                    print(f"    ERROR extracting channels from '{filename}':")
                    print(f"    FFmpeg command failed with error code {e.returncode}")
                    print(f"    Stderr:\n{e.stderr}")
                except FileNotFoundError:
                    print(f"    ERROR: FFmpeg not found. Please ensure FFmpeg is installed and in your system's PATH.")
                    print(f"    On macOS, you can install it via Homebrew: 'brew install ffmpeg'")
                    return # Exit if ffmpeg is not found

    except FileNotFoundError:
        print(f"\nERROR: Input directory not found: '{input_directory}'")
        print("Please ensure the path is correct and accessible.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

    print("\n--- All processing complete! ---")

if __name__ == "__main__":
    # --- Step 1: Ask for file location of m4a files ---
    while True:
        input_dir_raw = input("Enter the full path to the folder containing your M4A files (e.g., /Users/ace/Music/BWU_ATMOS/Serotonin): ").strip()
        input_directory = os.path.expanduser(input_dir_raw) # Handles '~' for home directory
        if os.path.isdir(input_directory):
            break
        else:
            print("Invalid input directory. Please enter a valid path to an existing folder.")

    # --- Step 2: Ask what format you want extracted ATMOS channels to be in ---
    available_formats = ['wav', 'flac', 'aac', 'mp3']
    while True:
        output_fmt = input(f"Enter the desired output format for extracted channels ({', '.join(available_formats)}) [default: wav]: ").strip().lower()
        if not output_fmt: # Default to wav if empty
            output_format = 'wav'
            break
        elif output_fmt in available_formats:
            output_format = output_fmt
            break
        else:
            print(f"Invalid format. Please choose from: {', '.join(available_formats)}.")

    # --- Step 3: Ask where you want the extraction to be ---
    while True:
        output_root_raw = input("Enter the full path to the *base folder* where you want the extracted channels to be saved (e.g., /Users/ace/ExtractedAudio): ").strip()
        output_root_directory = os.path.expanduser(output_root_raw) # Handles '~' for home directory
        try:
            # Attempt to create the directory to check if the path is valid/writable
            os.makedirs(output_root_directory, exist_ok=True)
            if not os.path.isdir(output_root_directory):
                raise ValueError("Could not create the specified output directory.")
            break
        except Exception as e:
            print(f"Invalid output directory or permissions issue: {e}. Please enter a valid and writable path.")


    # Call the function with user-provided arguments
    extract_dolby_digital_plus_channels(input_directory, output_root_directory, output_format)
