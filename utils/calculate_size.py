# Page Metadata
# © 2022 Roel Roscam Abbing, released as AGPLv3
# see https://www.gnu.org/licenses/agpl-3.0.html
# Support your local low-tech magazine: https://solar.lowtechmagazine.com/donate.html 

import os
import argparse
import shutil
from bs4 import BeautifulSoup
import logging
import sys


parser = argparse.ArgumentParser(
    """
    This script recursively traverses folders and enumerates the file size of all html pages and associated media.
    The calculated total file size is then added to the HTML page.
    """
)

parser.add_argument(
    '-d', '--directory', help="Set the directory to traverse", default="." 
    )

parser.add_argument(
    '-rm', '--remove', help="Removes all the folders with dithers and their contents", action="store_true" 
    )

parser.add_argument(
    '-b', '--baseURL', help="hostname (and path) to the root, e.g. https://solar.lowtechmagazine.com"
)

parser.add_argument(
    '-v', '--verbose', help="Print out more detailed information about what this script is doing", action="store_true" 
    )

args = parser.parse_args()

if args.verbose:
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
else:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

content_dir = args.directory
base_url = args.baseURL

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

def get_assets(soup):
    """
    Lists all the page assets such as scripts and icons in a given HMTL page.
    """
    assets = []
    for a in soup.findAll('link', {'rel':['apple-touch-icon','icon','stylesheet']}):
        a = a['href'].split('?')[0]
        if a not in assets:
            assets.append(a)
    for s in soup.findAll('script'):
        if ['src'] in s:
            s = s['src']
            if s not in assets:
                assets.append(s)

    return assets

def get_media(html_file):
    """
    Lists all the images on a given HTML page.
    """
    html_file = open(html_file).read()
    soup = BeautifulSoup(html_file, 'html.parser')
    media = []

    for img in soup(['img', 'object']):
        media.append(img['src'])

    featured_images = soup.findAll('div', {'class':'featured-img'})
    for fi in featured_images:
        fi = fi['style']
        start = fi.find("url('")
        end = fi.find("');")
        url = fi[start+len("url('"):end]
        media.append(url)

    assets = get_assets(soup)
    #assets = list(set(assets))
    media = list(set(media+assets))  # duplicate media don't increase page size
    return media, soup

def insert_metadata(output_file, metadata, soup):
    """
    Adds page metadata to a given HTML page and saves it.
    """
    tag = soup.find('div', {'id':'page-size'})
    if tag:
            with open(output_file,'w') as f:
                tag.string = '{}'.format(metadata)
                f.write(str(soup))

logging.info("Checking file sizes for '{}'".format(content_dir))

for root, dirs, files in os.walk(os.path.abspath(content_dir), topdown=True):
    for fname in files:
        if fname.endswith(".html"):
                logging.debug("Checking file size for '{}'".format(os.path.join(root, fname)))
                media_size = 0
                media, soup = get_media(os.path.join(root, fname))

                for m in media:
                    file_name = m.replace(base_url, '')

                    # current problematic with pagebundles is images are in the same folder as html file
                    # but html file might link to images in other page bundles so we need to determine
                    # whether the image is in this page bundle or another:

                    media_this_page = os.path.join(root, file_name.strip('/'))
                    media_other_page = os.path.join(content_dir, file_name.strip('/'))

                    try:
                        if os.path.exists(media_this_page):
                            m = media_this_page
                    except:
                        pass
                    
                    try:
                        if os.path.exists(media_other_page):
                            m = media_other_page
                    except:
                        pass

                    if os.path.exists(m):
                        item_size = os.path.getsize(m)
                        media_size = media_size + item_size
                        logging.debug("Found {} {}".format(m, get_printable_size(item_size)))
                    else:
                        # if the file path can't be found it might actually not be there at all..
                        logging.debug("❌ {} not found!".format(m))


                current_file = os.path.join(root, fname)
                file_size = os.path.getsize(current_file)

                file_size = file_size + media_size
                metadata = get_printable_size(file_size)
                metadata = get_printable_size(file_size+len(metadata))  # count the extra metadata as well

                insert_metadata(os.path.join(root, fname), metadata, soup)
                logging.debug("{} is {}".format(os.path.join(root,fname), metadata))

logging.info("Done checking filesizes")
