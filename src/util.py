"""
Oracle is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
either version 3 of the License, or (at your option) any later version.

Oracle is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this code. 
If not, see <https://www.gnu.org/licenses/>. 
"""

from random import choice, choices

referers = [
    "https://google.com/search?q=imgur",
    "https://imgur.com/",
    "https://imgur.com/search?q=%23funny"
]

# random useragents
useragents = [
    "Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1)",
    "Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1; .NET CLR 3.0.04506.30)",
    "Mozilla/4.0 (Windows; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.33 Safari/532.0",
    "Mozilla/4.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.59 Safari/525.19",
    "Mozilla/4.0 (compatible; MSIE 6.0; Linux i686 ; en) Opera 9.70",
    "Mozilla/4.0 (compatible; MSIE 6.0; Mac_PowerPC; en) Opera 9.24",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 9.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.24",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.26",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; es-la) Opera 9.27",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; ru) Opera 9.52",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; en) Opera 9.27",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; en) Opera 9.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 6.0; en) Opera 9.26",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 6.0; en) Opera 9.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 6.0; tr) Opera 10.10",
    "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; de) Opera 10.10",
    "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; en) Opera 9.22",
    "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; en) Opera 9.27",
    "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux x86_64; en) Opera 9.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux x86_64; en) Opera 9.60",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; YPC 3.2.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; YPC 3.2.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; InfoPath.2; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",
]

def make_id() -> str:
    """
    generates a Imgur id

    Returns:
         str: the code
    """

    chars = (
        "qwertyuiopasdfghjklzxcvbnm"
        "QWERTYUIOPASDFGHJKLZXCVBNM"
        "0123456789"
    )

    return "".join(choices(chars, k=5))

def random_headers() -> dict[str, str]:
    """
    generates random http headers

    Returns:
        dict[str, str]: the randomly generated headers
    """

    return {
        "accept": (
            "text/html,"
            "application/xhtml+xml,"
            "application/xml;q=0.9,"
            "image/avif,"
            "image/webp,"
            "image/apng,"
            "*/*;q=0.8,"
            "application/signed-exchange;v=b3;q=0.9"
        ),

        "accept-encoding": "gzip, deflate",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "cache-control": "max-age=0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "sec-gpc": "1",
        "dnt": "1",
        "upgrade-insecure-requests": "1",
        "user-agent": choice(useragents),
        "referer": choice(referers)
    }