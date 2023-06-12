# clean_output
# © 2023 Roel Roscam Abbing, released as AGPLv3
# see https://www.gnu.org/licenses/agpl-3.0.html
# Support your local low-tech magazine: https://solar.lowtechmagazine.com/donate.html 

import os
import argparse
import logging


parser = argparse.ArgumentParser(
    """
    This script recursively traverses folders and deletes files not in "dithers" or containing hugos resizing pattern in the filname.
    This catches media in your content repository which is not used but still copied over to the final site. 
    Use with caution and adjust the pattern to your own situation!
    """
)

parser.add_argument(
    '-d', '--directory', help="Set the directory to traverse", default="." 
    )
parser.add_argument(
    '-v', '--verbose', help="Print out more detailed information about what this script is doing", action="store_true" 
    )

args = parser.parse_args()

content_dir = args.directory

def get_printable_size(byte_size):
    """
    Pretty file sizes.
    Thanks Pobux!
    https://gist.github.com/Pobux/0c474672b3acd4473d459d3219675ad8
    """
    BASE_SIZE = 1024.00
    MEASURE = ["B", "KB", "MB", "GB", "TB", "PB"]

    def _fix_size(size, size_index):
        if not size:
            return "0"
        elif size_index == 0:
            return str(size)
        else:
            return "{:.2f}".format(size)

    current_size = byte_size
    size_index = 0

    while current_size >= BASE_SIZE and len(MEASURE) != size_index:
        current_size = current_size / BASE_SIZE
        size_index = size_index + 1

    size = _fix_size(current_size, size_index)
    measure = MEASURE[size_index]
    return size + measure

def calculate_dir_size(content_dir):
    size = 0
    for path, dirs, files in os.walk(os.path.abspath(content_dir)):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)

    return(size)

exclude_dirs = set(["dithers"])
image_ext = [".jpg", ".JPG", ".jpeg", ".png", ".gif", ".webp", ".tiff", ".bmp"]

pattern = "_800x800_fit_q90"

if args.verbose:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

logging.info("Deleting images in {} and lower".format(os.path.abspath(content_dir)))

count = 0

size = calculate_dir_size(content_dir)

logging.info("Directory is {} before cleanup".format(get_printable_size(size)))
for root, dirs, files in os.walk(os.path.abspath(content_dir), topdown=True):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for fname in files:
        if fname.endswith(tuple(image_ext)):
            if pattern not in fname:
                f = os.path.join(root, fname)
                count+=1
                os.remove(f)
                logging.debug("🗑 {}".format(fname))
                
logging.info("Deleted {} original images".format(count))
size = calculate_dir_size(content_dir)
logging.info("Directory is {} after cleanup".format(get_printable_size(size)))
