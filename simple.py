import threading
import requests
from bs4 import BeautifulSoup


class Simple:
    def __init__(self, player=None):
        self.player = player        

    def search_thread(self, q):
        print("search thread begin")

        try:

            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            r = requests.get("https://nyaa.unblockit.uno", params={"f": "0", "c":"1_0", "q": q}, headers=headers)
            print(r.url)
            if r.status_code != 200:
                return
            
            result = []
            soup = BeautifulSoup(r.text, 'html.parser')
            rows = soup.select("body > div > div.table-responsive > table > tbody > tr")
            for row in rows:
                sname = row.select("td:nth-child(2) > a:nth-child(2)")
                smagnate = row.select("td:nth-child(3) > a:nth-child(2)")
                if sname and smagnate:
                    name = sname[0].string
                    magnate = smagnate[0].get('href')
                    result.append({"name": name, "url": magnate})

            print("search done")
            print(result)
            self.player.call('hot', result)       
        except:
            import traceback
            traceback.print_exc()
        print("search thread end")

    def on_search(self, *args, **kwargs):
        print(f'{args=} {kwargs=}')
        t = threading.Thread(target=self.search_thread, args=args)
        t.start()

if __name__ == "__main__":
    s = Simple()
    s.search_thread('one punch')
    
