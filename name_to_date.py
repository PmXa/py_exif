# -----------------------------------------------
# WA EXIF Writer 1.0
# This script takes the date from a WA image's
# file name and adds it to the image's EXIF data.
# PmXa Nov-2022
# -----------------------------------------------

from exif import Image
import os 

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
        file_info = filename.split(" ")
        file_date = file_info[2].replace("-",":")
        file_time = file_info[4].replace(".",":")
        file_PM = "PM" in file_info[5]

        if file_PM:
            corrected_time = file_time.split(":")
            corrected_hh = str(int(corrected_time[0]) + 12)
            corrected_time[0] = corrected_hh
            file_time = ":".join(corrected_time)

        with open(os.path.join(directory, filename),"rb") as image_file:
            image = Image(image_file)
            image.datetime_original = " ".join([file_date, file_time])
            print(image.get_all())

        with open(f"./saved_files/{filename}","wb") as new_image:
            new_image.write(image.get_file())