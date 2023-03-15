"""
Oracle is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
either version 3 of the License, or (at your option) any later version.

Oracle is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this code. 
If not, see <https://www.gnu.org/licenses/>. 
"""

import requests, json, signal, csv

from bs4 import BeautifulSoup
from datetime import datetime
from threading import Thread, Event

from src.util import *

session = requests.session()
exit_event = Event()
threads = 20
threadbox = []

timestamp = datetime.now().strftime("%H-%M-%S_%d-%m-%y")
csvfile = open(f"output_{timestamp}.csv", "w+")
csvwriter = csv.writer(
    csvfile,
    delimiter="|"
) 

# title rows
csvwriter.writerow([
    "id",
    "url",
    "title",
    "description",
    "views",
    "likes",
    "dislikes",
    "comment_count",
    "created",
    "last updated",
    "posted_from",
    "username",
    "user id",
    "user avatar",
])

def signal_handler(
    *_, **__ # discards everything
    ) -> None:
    """
    Handles the shutdown signal

    Returns:
        nothing.
    """

    exit_event.set()

    for thread in threadbox:
        thread.join()

    csvfile.close()

def get(
    img_id: str
    ) -> tuple[bool, str] | tuple[bool, dict]:
    """
    Fetches the metadata for @img_id

    Args:
        img_id str: Image ID
    
    Returns:
        tuple[bool, str] or tuple[bool, dict]: Status, metadata or error message
    """

    try:
        r = session.get(
            f"https://imgur.com/gallery/{img_id}",
            headers=random_headers()
        )
    
    except Exception:
        return False, "error while requesting"

    if r.status_code != 200:
        return False, "not found"

    s = BeautifulSoup(r.text, "html.parser")
    if not s.title:
        return False, "not found"

    # double json load needed
    # no idea why!
    try:
        metadata = json.loads(json.loads(
            s.findAll("script")[0].text.split("=")[1]
        ))

    except Exception:
        return False, "exception while parsing metadata"

    return True, metadata

def generator() -> None:
    """
    Generates random ID's, and fetches the metadata

    Returns:
        nothing.
    """

    while not exit_event.is_set():
        _id = make_id()

        status, metadata = get(_id)
        if status and isinstance(metadata, dict):

            print(f">> {_id} valid: {metadata['url']}")

            csvwriter.writerow([
                _id,
                metadata["url"],
                metadata["title"], 
                metadata["description"] if len(metadata["description"]) != 0 else "No Description",
                metadata["view_count"],
                metadata["upvote_count"],
                metadata["downvote_count"],
                metadata["comment_count"],
                metadata["created_at"],
                metadata["updated_at"],
                metadata["platform"],
                metadata["account"]["username"],
                metadata["account"]["id"],
                metadata["account"]["avatar_url"]
            ])

if __name__ == "__main__":

    print("""
    ...    :::::::..    :::.       .,-:::::   :::    .,::::::  
 .;;;;;;;. ;;;;``;;;;   ;;`;;    ,;;;'````'   ;;;    ;;;;''''  
,[[     \\[[,[[[,/[[['  ,[[ '[[,  [[[          [[[     [[cccc   
$$$,     $$$$$$$$$c   c$$$cc$$$c $$$          $$'     $$\"\"\"\"   
"888,_ _,88P888b "88bo,888   888,`88bo,__,o, o88oo,.__888oo,__ 
  "YMMMMMP" MMMM   "W" YMM   ""`   "YUMMMMMP\"\"\"\"\"YUMMM\"\"\"\"YUMMM
""")

    print("Hooking signal handler...")
    signal.signal(signal.SIGINT, signal_handler)

    print("Starting threads...")
    try:
        for _ in range(threads):
            t = Thread(
                target=generator
            )

            threadbox.append(t)

            t.start()
        
        print("All threads launched\n")

    except KeyboardInterrupt:
        pass