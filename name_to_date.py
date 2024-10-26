# -----------------------------------------------
# WA EXIF Writer 1.0
# This script takes the date from a WA image's
# file name and adds it to the image's EXIF data.
# PmXa Jul-2024
# -----------------------------------------------

from exif import Image

import datetime as dt
import os
import re

if not os.path.exists("./original_files"):
    os.mkdir("./original_files")

if not os.path.exists("./saved_files"):
    os.mkdir("./saved_files")

# -----------
# Entry point
# -----------

if __name__ == "__main__":

    directory = "original_files"

    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)

        # Format #1 WhatsApp Image yyyy-mm-dd at h.mm.ss XM
        if (date := re.match(r"WhatsApp Image ([\d-]+) at ([\d\.]+) ([AP]M)", filename)):
            file_date = date.group(1).replace("-",":")
            file_time = date.group(2).replace(".",":")

            if date.group(3) == "PM":
                corrected_time = file_time.split(":")
                corrected_hh = str(int(corrected_time[0]) + 12)
                corrected_time[0] = corrected_hh
                file_time = ":".join(corrected_time)

            print(f"Format WA found! -> {file_date} @ {file_time}")

        # Format #2 IMG-YYYYMMDD-WAXXXX
        if (date := re.match(r"IMG-(\d{4})(\d{2})(\d{2})-WA\d+", filename)):
            file_date = f"{date.group(1)}:{date.group(2)}:{date.group(3)}"
            file_time = os.path.getmtime(full_path)
            file_time = dt.datetime.fromtimestamp(file_time)
            file_time = file_time.strftime('%H:%M:%S')
            print(f"Format IMG-WA found! -> {file_date} @ {file_time}")

        # Format #3 IMG_YYYYMMDD_HHMMSS
        if (date := re.match(r"IMG_(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})", filename)):
            file_date = f"{date.group(1)}:{date.group(2)}:{date.group(3)}"
            file_time = f"{date.group(4)}:{date.group(5)}:{date.group(6)}"
            print(f"Format IMG found! -> {file_date} @ {file_time}")

        # Format #4 NAME - DDMMYYYY
        if (date := re.match(r"\w+ - (\d{2})(\d{2})(\d{4})", filename)):
            file_date = f"{date.group(3)}:{date.group(2)}:{date.group(1)}"
            file_time = os.path.getmtime(full_path)
            file_time = dt.datetime.fromtimestamp(file_time)
            file_time = file_time.strftime('%H:%M:%S')
            print(f"Format NAME found! -> {file_date} @ {file_time}")

        # Write the EXIF data to a new file
        with open(full_path,"rb") as image_file:
            image = Image(image_file)
            image.datetime_original = " ".join((file_date, file_time))
            image.list_all()
            image.get_all()

        with open(f"./saved_files/{filename}","wb") as new_image:
            new_image.write(image.get_file())