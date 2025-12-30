# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import urllib.request
import urllib.parse
import urllib.error

class URLShortener:
    API_URL = "http://tinyurl.com/api-create.php"

    def shorten(self, long_url):
        if not long_url.startswith(("http://", "https://")):
            long_url = "http://" + long_url
            
        params = {"url": long_url}
        query_string = urllib.parse.urlencode(params)
        full_url = f"{self.API_URL}?{query_string}"
        
        try:
            with urllib.request.urlopen(full_url) as response:
                return response.read().decode("utf-8")
        except urllib.error.URLError as e:
            return f"Error: {e}"

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
