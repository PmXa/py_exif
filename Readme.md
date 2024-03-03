# 🕰️ WA EXIF Writer

This is a simple script to parse the date from a WhatsApp picture’s file name and setting it as the “taken” date of a **copy** of the original picture. The purpose is to help a bit with sorting pictures.

## Setup

The only dependencies for the project are `exif` (v. > 1.4.0) and `plum-py` (v. > 0.8.5). As long as they are present, either in your Python installation or in a (recommended) virtual environment with `venv`, `conda` or the like, the script will work.

If using `conda`:

1. Create an environment with `conda create -n py_exif python` 
2. Activate the environment with `conda activate py_exif`
3. Install the `exif` package via `pip`, since it most likely won’t be available from `conda`'s repositories (`plum-py` will be resolved by automatically).
4. Done!

## Usage

To actually use the program place the pictures into the `original_files` folder and execute either the `run.ps1` or the `run.sh` file. The **copy** of your pictures with the adjusted date will be saved in the `saved_files` folder.

> [!important]
> The file name should follow the following syntax: `WhatsApp Image yyyy-mm-dd at h.mm.ss XM`, where `X` could be either `A` or `P`. For example: `WhatsApp Image 2023-11-01 at 9.22.45 PM`