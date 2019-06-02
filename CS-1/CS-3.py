import base64
import os
import socket
import threading
import tkinter
import urllib.request
from tkinter import *
from tkinter import ttk

import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageTk

top=tkinter.Tk()
top.title("Pyridine")

global emp
global online
global offline
global refresh

top.initsize="top.geometry('430x700')"
top.finasize="top.geometry('830x700')"
top.size = top.initsize

s='''- structure, chemical names, physical and chemical properties, classification, patents, literature, biological activities, safety/hazards/toxicity information, supplier lists, and more.'''
ans="y"
snip1=["Search and explore chemical information in the world's largest freely accessible chemistry database."]

emp='''R0lGODlhLAEsAXAAACwAAAAALAEsAYH19fUAAAAAAAAAAAACfoSPqcvtD6OctNqLs968+w+G4kiW5omm6sq27gvH8kzX9o3n+s73/g8MCofEovGITCqXzKbzCY1Kp9Sq9YrNarfcrvcLDovH5LL5jE6r1+y2+w2Py+f0uv2Oz+v3/L7/DxgoOEhYaHiImKi4yNjo+AgZKTlJWWl5iZmpucnZ6UD5CRoqOkpaanqKmqq6ytrq+gobKztLW2t7i5uru8vb6/sLHCw8TFxsfIycrLzM3Oz8DB0tPU1dbX2Nna29zd3tM/0NHi4+Tl5ufo6err7O3u7+Dh8vP09fb3+Pn6+/z9/v/w8woMCBBAsaPIgwocKFDBs6fC8IMaLEiRQrWryIMaPGjRw7evwIMqTIkSRLmjyJMqXKlSxbunwJM6bMmTRr2ryJMymnzp08e/r8CTSo0KFEixo9ijSp0qVMmzp9CjWq1KlUq1q9ijWr1q1cuyV6/Qo2rNixZMuaPYs2rdq1bNu6fQs3rty5dOvavYs3r969fPv6I/0LOLDgwYQLGz6MOLHixYwbO34MObLkyZQrW76MObPmzZw7E3v+DDq06NGkS5s+jTq16tVICwAAOw=='''
sym='''R0lGODlhPgBHAHAAACH5BAEAAIsALAAAAAA+AEcAhwAAAH9/fyQkJCcnJxUVFWJiYv///3l5eREREQICAgEBATQ0NERERBgYGAsLCwcHBwkJCQUFBWxsbGZmZlNTUwwMDAMDA0VFRXNzcy8vLzo6OkhISAgICDMzM1VVVSsrK0xMTImJiRAQEAQEBBMTE3V1dVtbWx0dHTIyMmNjYyoqKh8fH1BQUBoaGhcXFzg4OE9PTyUlJVFRUUdHRxYWFjs7OwoKCklJSZmZmSgoKG1tbT4+Pj09PUFBQVRUVGFhYRISElZWVhsbG1hYWEpKSg4ODlxcXHFxcQ8PDzExMUZGRjU1NV1dXU5OTjY2NgYGBl5eXl9fXyEhIVJSUjk5OSwsLA0NDRwcHCYmJhQUFDc3N0NDQzAwMEtLSyIiIh4eHmBgYHh4eI2NjSkpKU1NTS4uLldXV2pqamlpaYuLiy0tLWhoaCsrJCMrO1VVqhMPDz8/PwABAhcXKRkZGQAABAIBAhYaHgEAAAQAAEVcXBcHBw8SHAYBAAAAAT8/Tzw8PBwODgYDACwbFgEBAgUAADIkHQIAACAgIBEUFyQdGSUrNgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAj/ABcJHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePHxGA3AigZMmRFhGUVGkSAMqILV0KbPmyYcyDLGXWPGhSpEKaOwcCZeil586hD3P6DGmUYk6PLZdaRHqxKUmTVVeCVDrx6cucOhl6DTr2Z0kvMGNatYnVbFq1MaUuLBqWZ12FZQtSdcuXYduFLB2e7GtW7sLBh+/qVVxQpWG/jAkiRjiZcmSFdBNrJpx2c8LKix8/BC358iLSQk1D5mwQ9UzREF27nnlZNdvPpmXbXm3Zc+vdvhcHL51R9/DUxSPPPq0cOGvkz2knx30c+tTm1aVfj27dblbu2qlTmNQqvjxCx+Nzq+fdOXt48HZhd/fOVn5p++/ps1UPAH/+37HdRNte8P0lGFwEnmcgTgmatSBkDyoYYUcCBjhhcsslRt5VG17XYUVRcQSWXWGBVmFHI5aG2GQnbmWSHqmtqFODHznQloCD0TgSVicBQId2GR7lEo/OCSldkEEBqWOS1i3JJHMxFlkTi0gmaRgC/j2p5ZZcdhQQADs='''
logo='''iVBORw0KGgoAAAANSUhEUgAAAJ4AAABHCAYAAAD2tP6cAAAgAElEQVR4Xu2dfYxd5Z3fz71zPR6Px8MwDIMZhontGOM44Bgw4Jg3x7yEEggsJYQ2bFo1u1tV7Sq7f6GV9p92FUVRVVWqtIqqarVV2+xu1abK2xaSEEIIEN4hYIwxxhhjGzPYxozH4/H1zL37+TznnOHcM+fOi2Nj451HejQz9z7nefk93+f3/pyJorkyR4E5CsxRYI4CcxSYo8BJpEDLSex7ruvZU6CPRy6kzqMemv3jn5wnSp+cqZ6xM21nZcupt1Gvo/ZSt1IfpP5f6uiZuPI54J3aXRV0d1P//dKlS5d99rOfjbq6uqIDBw5Ejz/+eDQ0NPQf+O7bZyL4ThbwuiFWB7UtqemprfL3CHXoTCTmbDBcKpW66vX63fz8q/Xr10cXX3xxw+OALvr+978/TJs7+eKphG6zGeK0bls5gbProq/V1Mupn6MOUBcnwHMYwTdI3Ul9hbo5qX4mGP/RFEGX0OlbV1999STQSYjOzs4ILtixffv2dbR/AQCeUTQ6EcBTXNxC/WpLS8t9F1xwQXT++edHvb290YIFC6K2trZofHw8Gh0djY4ePbpq37590bvvvhvt3bvXv3/Gc39P/QF13z8SAHaWSlFHrVb/40996lOLV61a1fTA9fX1RQDvCoDXC/A8uGeMvve7Ak8O92fz58+/7zOf+UxkFWz5UqlUItqEjwWkxB4bG4vefPPNWzZt2nTLhx9++BW++s8Q+BEInIrjM5EDtrPGtno9+jI0uUtuN1WR61GUHF08tzcB3xlBl+N1p8jlBMtfc2rX33LLLdHAwEA0b55egJmVcrkc9fT0RCtXrowg6MB77733VZ48BIFfTno4NrOePjmtWNtZrPtc1vtvMSQuQpROTF4J8KMf/ShavHhxtHDhwvD5sWPHoi1btgzzzC+iqP4+gD1jxG35OLZN0P1L6vfWrVvXf+ONNxZyuZn2KwCvuOKKSPDy+7fYlH9VLpc0TBznTCpwO42t+noAeNsll1zSsLYnnngiqCNatGlRUtC2Ipfks+PZq9OWfrNdjGD45xDiL7/whS8EkXmiSn9/f3TDDTfY3QOcbBVqxzpjwOd6OFhYstHVF154YcNhVedF3YgEGgdvgqSqI5QxAAv4yqpFAvCMKLPR8Vz0Wuq34XRaXIUE0HjYtm1btGfPnmhkZCSqVqtBBLe2tkbd3d3RueeeGy1fvjzq6JCpNRb73LlzZzcK9e+3tJS3jI/Xxk5Da05XUQ+1lao+uos6nQhsi7ldaaBer2389Kc/3bDwd955J2pvb49qtVqgU1oOHTokxxsFdLVSabyV31uhh4qfVnE6vl6CT5zRMRvg6VH/C3SyHo2IfMFCjX7zm99ohUWLFi0KhFRXgVhjEFQAVY4cORK9/vrrlRdeeCGAT+U6NTrS/hS7b7311j1YfX8Ph3gYi/h0MTbkvhuoN1OvokoPXUGPUf8PVfdQMwC0sRZP2loO4TK5e7Z4SOfPb42Ghw9P6Hd+nwAPHU93a7ljbGxcV5ViQQbg+Hupj1O/R900aVNO4w9mCryg18Glrr/yyisnLUdn589+9rPA3fr6zufUzh9GlxlBalTHx8eqnPYxdbnW1oWVhQvbWxct6ujilHfIHW+77bbgckmLnFA3AuLnUp55DtDqRJ2Oo5xsEstltET/5+WXXx4tWbIkzPnw4cPL4e7rf/vb336Z7/9FsvmTwCenUszCwS/CGAsiNS3STL1OaaAxcfbZZ098p/jluQPlcku5Wj12G899p2D8axn/dh76GtVQ2yeC+83EqhUVOoT/y8aNGxcY0skWFeIHH3wwiAms1BEI9R7cahAOeBBAjg0PD7ePjByed+zY2BHEJ2KhdAACHmLjqkNDH3byfcnNyBY3Y9euXYfwC77kwU9cLEHhOQVFo2AN4z5w0003DcipFYceJMHnIWHt52KVH9TRS7txanau7ayjm/YX0u73V69e3ZsFl4dvx44d9DlvjHblz31OUsfl+eeft++nWH8Zfe8rjH9+k/F7GX8/47/IY6f6kM5oi6Y1LhKL6vdwDHdL5HwxpuhJ7e4++yAE2gnAtgGmPRC0n1O8Ssv3+utv6EehXnXgwAddAHU7wEIs1bcsWtS5A19e4JTZctZZZ/lnH2P3sOlBt5nRak5Co9jIKa3kUF2bF5HpcAldsLTqRmoa5urcWUM7tFkBiC7RXZItcjsO4hgcrXreeedNfCVNP/jgg6Cq8Oz555xzzuXTjL+S8dU9PxFlOlGLs7POgqL716zx0DcWTyqcCd/TeQch6k5O5U443YEPPxzaiK7Wc+mll048oCWHr2oAg+OpBQva3h4fDyJEzjGwf//+itGOtCROaDz8JRynZTa+Nu0BOUnUltsJpM68LpodT1WDuVbRxSpwew2Aia8FHWuwj6VKi7yD/eDBg7bl7FUrWeDt3r07ggPuoo5C22nHp49ghGC8KKFOe3E75YbK7SDcOk5bX5YoUkrRqpEAd1K87pDTUXcArA5ESX8WdOkuAMxenhvh5x7q28eOVXfydy0PGg0VxhaUcotQTxKwpu1W0FCH33///b0aR/miy+PVV18FJOUdHCRFbJam6sYso9wBGJfkuZ19aUBY4HCtHs60eKjhhDvmzasMAb4qEuTgVOMzxuvQ7BMhZl3jdJykm8N7o3pFvugCQKSq5+yS01k5te8Bvr4iq1euAJEPQqD9gg9F+8CRI6O9ggtgN3RvW4g9LBdh06eb47Tg+V0bsPnbmfMzP/3pTwOHV69VPdAa/clPfiIdXpg/v+1ZxkklSGot6X/j0NShY71XAyJfpCGWe0UapC4mwYxbSeARJouqWLxar5uajX/o0NCjcOTHYn/fqVNLZkPnqUStp3UFdeOyZcsm9fnGG29AqIVDLHYXYBN4b1Pb2aAVJgrki6JDQqrP8F0rXO0KTvkGlO0G35XPubm0G4SL1MgvmE4dmM16j7ftWHv7ggdHR4+0/epXv1oFUAKCKpWWgy0tle3Q4UFlJR81GECpfqfKIPAS3bVhDomvszXrF5VW0HEf69+D6Dys5AaUTyoJHnvssWXQWQuvxqGFRi2bcFt9Pxn/eNf3sT/XdFOTk7OcU9qe10tUfAUHp3QQ39K+o0erVX11uE7OhgN2p7HG7GoSnUWf3sUQ8AaI92U56WWXXdawaMWJfdPPMBvcSf9LIDwO1FIzt4rcJbV69vB7kX5jmyXJdztyVNYf5kYKmu1NdgDdKRrhMGxuaQkHoZMNH+NvgFFHxahiWEXMryb4UtUh6IeKWfS+pay7P08XOVtqWGUPN35MD+MW1rxbdxJcUyAyXMsW+qvhCyQKUkIEV7Yx/huMz9hRlZoCX3roAlKBlFvmi4kH+hWNzxV9X0QGaSit/KnqY06lzuvjKlMAL/KUXlpkyWK6B0uM74cQFf0Qb4UuD091V9fkiIQz8xnarQJ0K8m6qOiPKuKk+KQUswB6rAeA/x7g01IzOvDX1P+XW+V6/k4dun71Q+r/oGbBJ7G+Sb0+IdR/Y0Of5Pcy8zXd3OfNstlB/XnyfNCVjJPyg3VGVQ7ElbS/nLqMz2sAYzsg2Mb8dqM27OXQHaBdOm45Prilfr7bwDP6+XikUVWVg1mUEKmY9eCp33HYtwo6qlKlzOdX8/sqAayli/g/uGBB+S3GH7RNAnpDbhvo0uRRpZV+ve/R/rmEbho+9/O7Tmi92CZk/G+q6WlFBR0/REt0WK+jmpovaC2C7hkqCQzBiT6r0gx4uhDY8Ppy05jyZXBwUI25igO1m8zZJStWrIjefvvtSL1PoyBf5JCGyuCeZRToct5QSdsbs3zttdcEXjs6C56YdZEuBAC78pFHHulDwWbY0k/kgBDjFv74K4LtnRdddFHwqZFitRHgwmVKfxNzoOBe+Mu1a9femqRirf3BD36w7MiRke/y/RfY3PuuuuqqsPGA4PJf//rXd7M29aT/lfgO1S8rjP8NDKY/0GDSQNDCffnll/swKvbCfZ6v1cb3xY7uwPGkge6T+6hfY4x1rkEdLg+8lNuZoZOWZP1bocHr9AugjDwe/ioW8b258ftZ71763OzYPs/Pa5nP31533XXBv4i34Foc++v4/AFotRmQ/le8BzcZHdLC5vu1v/jFL+5hHv+Mxx+hZg+sXFVu/aes598hnTqUUPog9WHi3F6F8/xWsmf+hHU+wLP/Pff8lEBsBjw/xxKLlhTpJfqe0D+q6HZtKsyeVu8LWIuKsVqzT6Yq+qwAl6Bz8zqMaBh6s7hhHIBVEAq/XpmkyJrOsL+gz84sR064xsWx/6+k0r6Bz241E0RiGTGgzzXs5Hf4vOtLX/rSRIhK4LohOMOv4cChqJf2KCrZtJto+we33357Q8TBsehfUTrKfBS16aZpSHwbwN0tV/dQOHZRUdQqflNr1r8JKRLbrmxhDkF8ciAuoc29ReMzt7YkpKi06aR+hUMWIisWXVTojqvwld5I228A/ptuvvnmiXX4PQ7rzmefffZG1vtM6gZKvBmsvf4fGfvrZiCZwpYtMhIr/Xdi9HyXecgBH6XOyLIuBF6i3znS4nTzs4PqAkC/GEWMDBeZ+FMirOBLdbpf/vKXJhO4eVU4AGG1GHQWN0S9x5gl4OmAg64HcCvzagAuD7lNDfBW2LTFcIwrjYpkN17iquwThWmIizqOmdIULO0WjQd0q6iVNV4mR8yGuWwk16cfs6b3yYHjmZZ6AOF34ejr7b8oKTa7fD1JSot0fq4R7jNIWHFrCmTme3Gz8R2bOcoVURtiQzCfvJHM4cuqCNdcc82kdSQSDSdtvVcR7vxivbT2dfbj6zKMbKQlv31KAMH+9NNPG7IzXjwjva+Zq8LPO5h0e57gDqwlxqSG+O6gJ1RRejxF0Br5ePjhh4OFDMEPaFDkOaebTFvEWqsBc7hd/TJPW77AESWsSnePjmk2Q4A2NFO8KdryJ9hGhq9UIeijAkcnzNWyhI/XZZ3baWe6UrQq+dvDi05nOnvtW4LOzcqCzjHZGG+NNcxFwGXFrP5AuPtWuDpJnyGxopM+1zQbnwP2ruM7Nj8HOKxd2bi3g+n6EXTq00VrTkDfwZidAs5189hanvnmhg0bpgRdupjk8Gzgb8E/o9StIo6n01gtuKtZRrFAY4IjsOFtiMgOfFkr1SuKFlYEyDR1SpcM+lKVU2f8dpDYbVcagM8+J0dkLtsQQRU4UD+AWp3XPeUeimv6KzM3HdWLOcGr8/qkHE8XTrN56T+U+HRXZqzlGhT5jTd4j1E1wibj/a1Lrw7abmTs292sLN3005lAYYTCDcqW7OFRP6bNKCJ8S6Kz6Vu/kPFXNRl/uK1t/pBgEfjw64ua+QkFl2K/qCRhOdesMUSkKGrDk3AnXLY369D2WQ/bk08+aXJEpPhNQ3iuF4OxD7rA8etiZ9rISRHwOL0hxNNWxO2cgJsXK9+1amfnokcOHx4Z+fGPf7xGw8FNzYNC6810KUWh3EuOCWhrEGofk96LSDwAmMdGR48uzi/W8bSIYw47r3N8/OhZjL0yz/ESbiIXRgSqn9aXuhF5hV4OU+TucZyYY7YQ+ip3SwMysi61jzwXESTMZ6eWPRyaja/1oA99Qx0x27cqgnprGp1IRHkhADBWPDSb4ej4Q8fduDLAG2g2PgcEA6SiPiWH0XUyUCQSpYvcLrm/MWls9XXWC4BbQmhQoDPurdlkBR8SoDqwU07ufhbEjlMruHCN2Q+LRG0Kxjjxv6CoR6mDJL6jUUTkUxghjwOQkYceemjSEwLOXL333x9UpGoZDiEWtnDKNgO4rYbbAOc+fu/Mh5VSTga3w5cXLYIwiyViPnYqYRJuFXQUJrGsyCJPxbhgsO9s8UAAbrJJKp5cHbW3FTnDEw6MiR3Celp+N2MlBus+W1RD5I7nntsTNiw/XtpWCcCB1D+3LXaN6JOrt/H78mbjG05jbLOTTaJAPOrKaswcEvhyp6LwZTq282Mf5HhtcnrGvZR+2IbGZAbDox4qD4KGW/aAKc4BOPpmaVpOl45bBLzgQqAeS1KvJwGJyaHM1nQGD+G/2m/4C06xleTP7UXuFE+6nEcLGT1tF89vAmQv43h+yUwVHKBvUas835ZXyBVVjFM1WC4X0o9VJNIVZcwBHbBFRXsR7fqmEv0vvvjiJJ1LzqZbhTldCTHNr+vPX7RWzfBijlEL5rMQbj3A+kyKaDBiBNkrr7zCmjurrj2xsgsP8ubNmz1I2+Riuk9ohJJfQr8bX5HnKh+NX9GwsbhXRIzq3Xmu5kFS1chywrwxKN04aIYy1fM8cKvzaWoCSy7v3tjeQ58Fsy4gysvQZAc/ZxTibGpcAGrcJcVGgzoDYDNaQXShdgCA7jbwz997ilwHKfAgqvHczUePjr5EfYXfXwVwbxjnhetVikSFogBOYNxWnceQXG+RYREnTbYQ25Ub11TKmwLPdemkzV6skXISk7noIDWqsuyee+6ZJKIEHWuEQ1QS31n9Irj3QH6z3CjWp6MZH18dyzeoJ5OAJ0D1gWpU8Ltx7NAvB/pTrGfSWh1fazoxbOB4+mrq52iI5D0QrjOr28mp1dPSknJEOLf94Lut9zP+yry6k4TwAr3cS42nVIWRMXjAODQ6qcP9EH5Oa2BMEQctDTfjeAm4BN4hKj4sSEuuInRdVWSQSAAIMwrIdtDnVjbktQSohnSQdyWU8/GOIp9hfCJbRrU2x8aO6bfqLxKhSbtgNjIbAdpT5AryewPwrs1NzEZP9Pflb3/lkaKTmzUeYPPJsK6TBlVbVnT/xDxD4ruIn/IeQGTcm/Df2KQsm2QzPTDougF0yn8SP8dXalTk9WzHhx47af8BHBH1o0xkIcIabWnLqx/55AsTSz//+c9PLEl1A7qyljLSJBiU5+gDzRspsThuCW88MMSZjiMNdYNRngGIL7K/wYLmb7NKtPjxRxaXZsBTn2Kjx4YASWdeQZcYEMmsi8D1qOp7mv+j3rXIF08J4BTIcrbA4RLgGYecuMTSzGfIiYQw4e6GnfcUcUaJiN4RdAxBp4O3mXEkKBQb+s30QeXX14xYfq5xpBuJtSMOg7ujMGVM7oLhJegAVL0DEb6iSILEPlHFdoibBqWTdtdBn5uKEj+T8WFb8XUAAUP71UV0z65DrqrxlBXH6Z0OaauoZZ96oZvepAYSGPVRGmSZii4iQcfB2QvdH+LZmtYwOFjDvJewfsN1f0v1jVeTSpGodfGwzJKnD52x0fdkD4mi7LOArYYiXOP013Aoj5fzFqDtY+BFALTuRhiH5WfNGKMJpOkpby96Vj0FcArwVha7XL9cnjBJapHWqPNwk68qso6dizqOoqOr66xwcp95xnBjcSni+EnUxk3H6qz3sLZled1KDsF83UxDaUPMp8LvlSIgOYY6M30ZBjRr5w7W+XVvouX1S2cZW6Gl9PItMdzRf0L7q6YyIBTncjtLlsZJ3qN0k8Ym/fbK2fLFZ7Kg08vg5XMOwV6A+hD9e5HrX/Pcn+Okvh1RfAk/fQuWb7q6toi6RRwvjTeOqEtAxEnKvBYNCiexvDBJgRqyN5hAW9G1xSQYTg5ebIgkXDIAzhOrBcfvrUUcyo0xSE5qeJ+Kf9FmaNHyrFyxfOjQ8Ho4WH8zv5VuAOcv6CSyup7KsxsnJ/WQKLb93M+y6xG08XyCVd/Nc5fbR57b2J9FKQAXKGNZrnTeRVnM9m9CBM9s4KdO3FVGGIrW+dH4Wsj1HkBngsP1+g6LEi7SDZezu6Y8Z090Ti+Zt6vbYuxxC655zq2qCfFhDY2aeZgmMrAnPHf0LtSfLuedWtbJ/JdzUd1EDm/gfXRTnT8KRW0c7K6QFVEaTFKzG0DrxuEiQey1eFLgfDVPrYHxnrxJ74NyAPpCPJnaFMSyHMMTLscEuDHjLbKIPW2MtYSv++F2lbwS73OJfldDdKxR9H3xi18s3GTbeueX1HvoHIyhg+gzbR9+eLAbfxvXB8f0Q4VUJblA/t0mKQccGTmyHPF2CZyu8/rrr5/EgQWTXABOjE9svAK36Cm6OuB80pgnkmWdm6UftJmfMR0fkK7j91vRiXsdfyrrXW6nBW+f/p4tHhj66ccPe5fAw3lfMWmiqJjwqphnLeYmwjzq0ns96lG76krelWQfSqIEY5OyzIuA53HVMpTj7dLHlC9yBvQkfD7zfPORqeG6VwwZrSzyntuHekwslsMlaEGX3vBRrKvcDqWcIjue+gUnrZXNbL322kKuHZybcIMuwNLFTaywmUVFgCqq2Ch1za2mMpnr1ta2oIMMYpzGUY8+PJTkbjgn3TVqIqoYSXJArw5WOWIRl1ZXFWi4GQYWLuwIb0hodmfD5++4447C+eY/zIy/QiOo2fjZ54wOKXFUB/Jqk64WGYUGge6gNLmgaDJmCpGEKhNRB4TB9YYECN+Zky8eEP22jL2JvX04s9cTTZtwvJBUqOx/W/ZqR1kCa21x4pdAzPPYuK3sj5eNlwOuSea/3A5QVNkMRaz6oDWfqQt3Le9Rd3Ax2eJYX/ua8efmxTHcWAPzRXHN9Em5HadVw2AzXE33xQd8573fVgB3jqE2HdSswxthjbeuPbqA5N577y0kdB6Aivoice/mN4siTIe+ZuNrtOi+yYtb9+2ll14K4yFmjbKY4jUhctXb7r5bVWxyUQxnJZBctVnb7NOuLzE6tjHf/wSt96FekbTR6Epq5sdTBHKJp7STB/YIvmzxlFhZ8JokqNwH8P6pJybvTtG605cFiBs4Hv1NvO9Ncctm71D/mi7bpUjhl7B33nlnA+gEY75ozUKMnWzANvp5E86ma0cQWvUr/tbfWct2T2kiKqbEg+4NFe2ZtNWyJB+wwZfWrHPnatRhuuL4P/zhD4PBlC9bt26VaYxxZ3cH69nJ3lS1bKcqSh0NESMVsymKcfU/1wftuUm44DuJQ9wozKQ70c0udCs+5wOWBaB+GRP+dN4i8/QBlCW6CljbNbRd64t88iLFtyAB4Nf5/mX8cDu0annGq1VJeKU0j+/mM8YxJr8UPeICAVxkXSk2FNt5UWr7rOKsn+7RRx8NmR+puPQz5jvK/J4AeJuYM9m7Y+8yppan3NgsXt+AcJS1H4NY59Gmuyhk5YYotp966qmIXLZgnDgvOU6RA93vFT1uputyLuqqReLXfklINdE0cJyZjO+mK06zL1FK3R3oyFvZq21MeT/rmc9cQiJGvghyuSN3SkJMXUDbh6GzojWlz8sIlCTSm3UdYE2/ZMwfoduiQ4/vh45eyHevG6IRzYDXwmC+3UjgLUaHuspFZSegc1IWD8GXorheoB6TV3I94cQrCYUteBribAV4cJuak9G4CHnf9O/1RUFu1vE+WPXFnPYuN0WdRhYtEdw4T5TzmEpUmTov2J2bfir1GIkqQdmATRyCJ/huu6CLXTrjpKyH12RYJZDedy841Hbv3rOCDZ3neAJG144cXLCZ5gTRq9DhKJfZS5zyshzbOadxWbmLABJIqhs9PbbtLjF2+ZVX4ledqDOma3zuuecCmJEiwd2za9fuIAGajc86DjD2fsJyY7Sbz3pL7oEgNIuEv3dB+0dNz2cMEgFK43v3vtfP/CpKLNcjp/RAJFknI4x7lDWNoRrNk+5kGAdVS0kmDQS54lRDw4iF+wJNzJJ5DaPt1/x8Mabt+CDVSIxBgkn/OqHpy7eZZB/E70P3uQrkP4CFN5DNHZuODTtBMlY8Ndu5nvf/MdVfTOKy2+F42Zdv80KbUidmPJy1sgTO9VkU/41MfgUiz6i30YGwePU3jYei6IhcRcAZEmJzMffnj3Kx3E1Qjx3xiiLreTQO040panfFXC4cAi8TeQAIlFd6XTfzWAkRr6hWj17LPBZDRF+849hVKv3NO0ifwWxLnODtGjjMo40xgu5MP2lbOYGvuDB3zuyfdubVRe10fq6P/gyvyZFHTBUz9MTBaAc8bbRp5dA6jgfCtTD2vEFoFm6D6/zl8LRhEPUxdrjQzWcBdNBarh6SWlnbeax3JXNcC2jNuyvrhkIUD5McMcRP5xjWY5+eC9p20Kfz9TUaQTXT4Ww0yYwh78ckrybZJeC8cajTPL2HwvjOcVJWctOQWeKXIyYZmf7zJCb5gKJkpl5+kxo5GaOcIHWm97QgRX9i1WazGHSvEArTwoxwZ5TbIewjsGvjvktY7DI4R7cOYUV5kRUpF5KrSDS4CtcCWw5CWC7DLBglcG3Ew8WbBYN4rRma0nGdgi4QJeZ2sDrErhwJGjuPMrmwit8l9I2PLaQOaYF7u3+YDZlYB3Ntoz2ZLQs7fDFRrJyX1ZON7ND2aMJN40vqbizA0Gke8uni6EFJX+gIcWyfDQmmuDxoM1/nLpseMoQ9tMHxjo7qi5GCL1TPgu2Yg4kUGmskXhzTSe8lpGBA6cQHJIehyz6402LWYy6h3oWQEUP7EIFK+gtzhN7QYV4H87St/kOppd6muy3sKTTdx8FwjwVcUF2Sy08ezMJU+CmAZ+eBwOS4tfxK5yLZwsu1HKcriljFBqDbwgSNz7rZwXFcZFr7WbIACDg2MSdozYt9hsI93Wag04j4+c9/bniK+xSdiNDxPQAi3LxKgO4acFyPQYzaXjkdvxu0lyANRJGYcp8YCHFcVRqwWe+ykaRkjbl5gtN7Fs7ZO6+BOyVcAtUkgCrEDRHjbGaI6hyJ1z7xksXAXWm3UMDKHO0n425SH5qXcMeGNyk4NhW9KbLf4H1w/HjOIY8yuMKSgx5o4GfOyznoXmQ9AZisZ4HApf1RAe9a071ND4fqVsL9XKNusxDZivsK6xJ4Ak3Ahd9VXQBoU9A5xhRJAiESYedwqfKgCiPK4x8Bvg59OkWcx00zxUcdCL1jOyflZUDwTnISnJALKzoBLlqRE7hNunh0kPsQm52CvVncNUnKxEHaAcBDbl/K6nlrVXztLw7XhbUk4A9zKDyJySEg68brinEGDoTfmxA/EHRsrSIAAAZVSURBVF4ApeBzE5xvLG4D55kAXgqMeFPjeHYCkiAe02fS9abgK+rzozZhTsEJHzv646SCZA5hP9N5J21C3mQCpHBd0vfWKFkSLhic+MnBmHh7UtJeCZSux/WFcdJ5JjRNaSvIPVwmT0z7TsOpgKf4EXxMtKY75FWMiL8j/HIXVk+PHnYVd42ANP5pXha/j6Gc7kTcPeO7UYwQJOw3FbMpDRt+ZrkNe1lBp/gmivdyb0U1S8G3AxVdRIeLDW+hAnhvxoH5CZClnEQuFd7ZlxgRhfPgQ9rBBuKETH4fU7SGDUg2NbBEQZThUCFYnwApeW1FDIDsRiVqRrZtmvuYzsUMn8BRkg9SnXAijpUAP6zJdkn7EFbMLMjDkeWg4Xs/ExzMM6g1GcDL9VLnfvg4y22TtYe5JOuZaC9NPzoI0wMuHXNK4NEocD1dIE4UZfZ5wGB60vpnn31mAN2NVOkadxxafBmjyuYwUQ19YLzEp+pLfN5KRFtTMZvd/cTfU+O52+nzdvP6s0FtLSyTBLJWbeLrGkzG0zfHJeugx6WXnMOF7JhgMyYM4kwdrYZoTe/KTgAvgCIHkGSzzNgJ3C/lPGnblJOkoaMQZhSsefSnc002PxWhGfUjON8D1/Vns9OTWa+/Bj2a9TgPABTPkzLBwXLt1ZcZs+YlpomDlLaPx/cy0kQUyrnM6FrjTIGX5Xp71b9EvdYMnG4AAvsOuw5TwFWkmQxe6nEUzbF3qISlqrpPguxPNn3K1GgXS1sv2PwbA87Z9CfTyDX577/fi/AflRh4dZNRU5HOHNThwoXu7ObMOC076V3OFzYs/jtcfcyWSf3Npm280YUJkxP9TtFfAFN+QtP8HTh5k3EL1pJtO7H2lKumgJ/tHCamOB3Hs2HQv9jM9KGQ8o7OtR/x62sciNHGcp/PD7np+scyP9NXO0x3IsILquE0f4izenH2BdX6w/QXqeflrWrdKHwerLcU5M1M+FluVNp8NsSdTduZgGe2/c10ibPpdzZtZzr+zN7EpP4VH5axoNdgGan3DcYKcnjxoEp3sIIBXHBVyOVi5XNq6yadKdzO/3izkZ/357NC9M9puOQzavXtoVPWcHY6XlBurR6WGVNgruEpocBMOF46MTY2TmNCgmnpCTp1hdTMDsppCsDYkpuxThXuptLzHb5bL5sCn4bJNDDyl7OT7F1BpgWatfJOCTHnBp05BWYDvETsBts7sY5i5VhlWmWTXxNrakK3mhGbTrjdOsB8VzaTVi6XXqtTl8tnXyQvD9JPpU4n8FOwz5wCcy1PCQVmC7yglyTuCEVjAqwGxXtGYMuuNvEneWO+PZvxqyNaV40uG8Vs/q5F/Lq0Fi6V1In/Bh9h1hVxSgg6N+jMKDCjO5BNukrTmvI/ZzbyR63UEQ0bLc3fHjPrQa4n+PKvnfBzncdwycHY3zbhUJ3T72a7A6eg/fFwvJMwzbrJACEjJV+0ZL39n79CKOg0YHwrJkaGuX4hFnoSJjfX5UmgwCkHXpwVElLfJ73yzKhFUZHbmazoWzl5zuyLNFzT+A8zTgLB5ro8MRT4XUTtiZkBveiOoewxQXImRdBhbODEbn0huSaZvAN44h7HTLqZa3MKKTCTfyl1UqenRavjGJE6j6SA1Rgu3VPdmzCxklrDCHkMo+Ilwnf8s5ZxuN74B+h5IT9trpz+FDjlwINEpvP4piJDccNkxH6GutAIhTHgbOavjmTuu44Sq32aMN2zxIr9FwcCzzQns1zjt1nPldOeAk0zkD/GmYcMZDheP0kIyxG5l/n2JfS2Jfz0zfPewvcVXiR1VvaRJcuLC+tbfNlPkklsGpT3PLNZzR/j9OeGOh4KnHLjgkmHQPxHWTCV1+LU79IyAMkr50u4W0omMhoz9rX+JnOGJIQk+dCIimGyWfsPj4dgc8+cGAqcDsAL6Uq6RjAUMHaCR4TrjhV0tvLZad6YvjrafJBPQpiLzZ4YIHzcvZwWwGPRaQYMMVf/A6HJBhNJCGkKevpmqjQZwBy/uRDZx42YEzTe6aDjZZeiWPVapZZu+HebabJkJgEhvWtg6G7yq6xOEGHmujm5FDjdgOdqwwucY2u3MUM3k/Gqo3hOpzu52DipvZ+OwMsuOP9K0zmwnVQ4zHU+R4E5CsxRYI4CcxSYo8AZQoF/AE+2CsK+WhLXAAAAAElFTkSuQmCC'''
online='''R0lGODlhHAAcAHAAACH5BAEAALgALAAAAAAcABwAhwAAAFWqVVGiaC65WB3FSxzDSxzGSxzFTBvGTDiuWVmZZgD/AFSpZynHVQ7QRA3PRA7QRQ7RRQ/PRDTHXlmZcmaZZiO/URLPRw3RRA/PRQ3PRQ7PRA3QRRDPRke3Z1+ffx3MTRHQRxHMRxbIRzysWn9/f06TazG2VhHNRg/QRDjOYx7MTg/QRhDORhbJSUulWiTEUTO/XDe2WC26UziyWxDQRUSuY1WUahLMRQ7PRRjHSVV/fzSzViy4VSu7Uym8Uiu8VEOpYCm/UhHMRW2RbS22URLLR1SbcRe9Rx/BTFyLcwD//w7ORA7RRDSvVw/ORTWxWFujbRzCShXLSTmsWhDMRhDNRybHUibCUw/ORGKcdVqUah3DTRPOSH+ffxjJSFKcalmZbDKvV2mWeGiWcy+0VQ3QRFObaVuXbWuTeGSRbT6nXVOcZlybajGwVm+Pb2WYcFuabSLBTRHORmKJdSzCVVegZVSNcSHFUBrGSxfMShTLSEOlYR3CTBLMR0+fbz+lWRLORj+tYg/QRRTJRxy9Sl2haxHPSDC6VA/NRS67V0aiYzK1VzG2VzG3VjW2WTywWxjKSRDORTy0YRDPRTi2WRLNRg/PRji3WyfBUhDQRii+UnWJdVChaxnJSR3KT////yTEUi+/WU+fZ0WpXBvASBLNRx7OTz62YBLQRw3ORCbCT2ObcT3EYCvKV0+nYGqUakGrYCa+USPATyLAUCO/TiO/Tyu8UgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjYAHEJHEiwoMGDCBMqXCgQCYghIBgmxKBqiMWLFiUOHKJKFQaOHSuqapKR4RCKQxBy/LiQZMqFHjEkbMJS4skmBy8eRGTh4MeXBDkCFYixJEGKBXUSHEkTw8+hTSoulTqQaZOmP4NyXAp1yNWvTTseVRWU7EanYLGaJboWF1WBTjGkvYp0YF22U+fSHSq2aluveqO29Rj0rlu0af8aFdi3qtyvKAsPdfuW8UmRSQkX7Dh5odPOuJSa3IrQpUnNCb0u1lp55ueQnEfW1NgxLmzQGi3o7qmxt8KAADs='''
offline='''R0lGODlhHAAcAHAAACH5BAEAAMEALAAAAAAcABwAhwAAAKpVVa1RUcw5QdwpMNsoL90nL90nLt0oL75ARKVZWf8AALNeXtw1OescJOobJOocJOwcJOscI+scJdxARJlmZtQuNekgKOwcI+kcJOocI+sbI+oeJsdPU59ff+QnL+ofJucfJuIlKrtDS59fX39/f5xYWMY7QuceJ+sdJeRDS+QqMOkeJeMjKrRLS9cvOOobI9I8QsdCQuoeJ+oeJc01PMFCR+geJeodJcBKUJRVauUeJuMkK8o5P802O881O9E0Os42O7VJT9U0OOcdJZFtbcg2O+QgJ6ljY9UlK9gqMItzc8E9QekdJcM7QaNbbdgoMOYhKb1BSuUeJ9sxN9gxOukeJuodJJxiYtwoMOcgKJ9/f+EkKqRaWp9fZsA+QpZpaZZoaMk6P6ZYXqNhYZNra+wbI5pkbbpKSqZYXaJjY8E5QY9vb5hlZcFCRppkZNYtNekgJ+keJ5x1ddg0PKdXXo1xcesdJN0rMusbJN4oMOUjK+geJKlUY+QhKaxLS9kpL+YhJ69fX7JGTOgfJ79LS+EhKNMnLukdI65dXekfJ+kbI8o4PNA5P7FNVMk7Qck6QMY9Q8JCSOMkLuceJqJcXMNLS8ZARMk5QOcgJ+seJcZCR9cyOeocJdIyN4l1deAmLekdJuofJ+EpMf///9oxN9U8P6dXV6lUcapqarlNTdUnLekcJeodJuUrM8pITOkhKegcJOkcI+kgJtgxNdhESeE3Pq9PV5RqarhKT9MwN9ctNNcuNNQuNNcuNc82Oq5QXQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjMAIMJHEiwoMGDCBMqXCjQgAFDBhgmNEORoiYzF81IHKgpY8WPFiV27Igwo6aFsEgurJjw4kmRZgwdzHjQk6eDIQsuilnQI0WDPwkaCjpwZ0WPBFkOpLgoKcanHwlqWvRSINFgPi1GXaqRq1OXIK+K7Wo1LFiywTA6dfo0K1qVZaWGhVo1bd2cVsF6bDowZd20aAF/nFrXZU+eSanu5MuV8cChgVeqNThyI16gVxFi/EtZKeWOkQ8aWgxyJOKNi4wOlrnRoKdDr1vLThgQADs='''
refresh='''R0lGODlhHAAcAHAAACH5BAEAADsALAAAAAAcABwAhQAAAG1tbSMjIxERERAQEBUVFQwMDBMTE0RERH9/f2NjY1xcXC8vLwEBAQICAg4ODj4+PkpKSgYGBgcHB3V1dWZmZg8PDwMDAx4eHgoKCnd3dyAgIDs7OwQEBAkJCS0tLVRUVFVVVQsLC19fX0VFRTc3N09PTxYWFiQkJF1dXQUFBXFxcQgICGpqajo6Oj8/P1BQUDMzMzk5OU5OTjQ0NCgoKCkpKSsrKxwcHEFBQUNDQwAAAAAAAAAAAAAAAAAAAAZmwJ1wSCwaj8ikcslsOp/EwQAwhRIB2Kx2MMQutWDtbgpQhgGCczYJPp6RW3bbvUaSxfQy/G28m8NHflZ9WAKDhF6HUXWKXYmNQniQcXZ6X5JXjH9gaYBNanNOd2Fcg1Onj5Cqq5BBADs='''
top.rgtarrow='''R0lGODlhFAAbAHAAACH5BAEAACEALAAAAAAUABsAhQAAAGdnZ2tra39/f////2FhYVpaWldXV15eXnFxcVhYWF1dXV9fX3Nzc4qKimBgYHl5eYuLi5CQkJSUlFxcXG5ubltbW2ZmZm1tbVlZWXh4eGlpaXR0dHZ2dnBwcFVVVWNjYwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZGwJBwSCwaj8ikUvn5XJbFphQ6vEidVKFT+sxar9nQd+ptfsNjbJmL3jbD1y41nY3XwVR7Hg81q/t8S1cfd2R3cmhhiotFQQA7'''
top.lftarrow='''R0lGODlhFAAbAHAAACH5BAEAACEALAAAAAAUABsAhQAAAKqqqnBwcGhoaJGRkX9/f1lZWVhYWGJiYm9vb1dXV1paWltbW3p6enR0dG5ubnJycmxsbIKCgnV1dV9fX3t7e4iIiFxcXF5eXoeHh3Nzc11dXYODg3d3d3h4eGNjY2ZmZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZBwJBwSCwaj8ikcolUKJhFpxMqlE6h1ifWSs12uVvpVxy+Mr1jclkBooZAaChc2qbO1ec4827Og+V/YXVucG6GUEEAOw=='''

imagePath2 = PhotoImage(data=online)
widgetf2 = Label(top,  image=imagePath2,bg="#ffd2ab")
widgetf2.place(x=0,y=0)


def is_connected():
    global online
    global offline
    try:
        socket.create_connection(("www.google.com", 80)) 
        state = "Online"
        stat  = online

    except OSError:
        state = "Offline"
        stat  = offline

    imagePath2 = PhotoImage(data=stat)
    widgetf2 = Label(top,  image=imagePath2,bg="#ffd2ab")
    widgetf2.image=imagePath2
    widgetf2.place(x=0,y=0)
    top.update_idletasks()
    top.after(1000, is_connected)
    
tt3 =threading.Event()
t3=threading.Thread(target=is_connected)
t3.start()

imagePath = PhotoImage(data=emp)
widgetf = Label(top,  image=imagePath,bd=3,  bg="#3399ff")
widgetf.place(x=60,y=80)

imagePath1 = PhotoImage(data=logo)
widgetf1 = Label(top,  image=imagePath1,bg="#ffd2ab")
widgetf1.place(x=145,y=5)


def newdir():
    top.desktop = os.getcwd()          
    os.chdir(top.desktop)                                   
    top.dirname=(top.desktop+r"\StructureImage cache")
    if not os.path.exists(top.dirname):                     
        os.makedirs(top.dirname,exist_ok=True)              
        os.chdir(top.dirname)                               


def molecularweight(CID):
    mwlink="https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/"+CID+"/property/MolecularWeight/txt"
    mwdata=requests.get(mwlink)
    mw= BeautifulSoup(mwdata.text, "html.parser")
    mw=str(mw).lstrip().rstrip()
    compweight2.config(text=mw)

def molecularname(CID):
    mnlink="https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/"+CID+"/property/IUPACName/txt"
    mndata=requests.get(mnlink)
    mn= BeautifulSoup(mndata.text, "html.parser")
    mn=str(mn).lstrip().rstrip()
    mn=mn.capitalize()
    compname2.config(text=mn)

def molecularformula(CID):
    mflink="https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/"+CID+"/property/MolecularFormula/txt"
    mfdata=requests.get(mflink)
    mf= BeautifulSoup(mfdata.text, "html.parser")
    mf=str(mf).lstrip().rstrip()
    compformula2.config(text=mf)

def molecularstructure(CID,comp):
    mslink="https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/"+CID+"/PNG?record_type=2d"
    path=top.dirname+"\\"+comp+".gif"
    urllib.request.urlretrieve(mslink,path)
    select(comp)
    
def select(comp):
    pth=top.dirname+"\\"+comp+".gif"
    img = Image.open(pth)
    tkimage = ImageTk.PhotoImage(img)
    structure = Label(top,image = tkimage,bd=3,bg="#3399ff")
    structure.image=tkimage
    structure.place(x=60,y=80)
    top.update_idletasks()


def getinfo(event):
    newdir()
    compound=txt.get()

    basepage = "https://pubchem.ncbi.nlm.nih.gov/compound/"+compound
    pagehtmldata = requests.get(basepage)
    soup = BeautifulSoup(pagehtmldata.text, "html.parser")
    name_formula = soup.find("meta", {"name": "description"})["content"]
    name_formula = name_formula.replace(s,"")
    name_formula = name_formula.split('|')
    try:
        x=name_formula[2].lstrip().rstrip().split(" ")
    except:
        pass

    molecularname(x[1])
    molecularweight(x[1])
    molecularformula(x[1])
    molecularstructure(x[1],compound)


def reset():
    global emp
    compformula2.config(text="")
    compname2.config(text="")
    compweight2.config(text="")
    txt.delete(0,"end")
    
    imagePath = PhotoImage(data=emp)
    widgetf = Label(top,  image=imagePath,bd=3)
    widgetf.place(x=60,y=80)
    top.update_idletasks()    


def expand():
    if top.size==top.initsize:
        top.geometry('830x700')
        top.size=top.finasize
        lftpic=PhotoImage(data=top.lftarrow)
        exp.config(image=top.lftpic)
        exp.place(x=400,y=0)    
    elif top.size==top.finasize:
        top.geometry('430x700')
        top.size=top.initsize
        rgtpic=PhotoImage(data=top.rgtarrow)
        exp.config(image=top.rgtpic)
        exp.place(x=400,y=0)         


refpic=PhotoImage(data=refresh)
top.rgtpic=PhotoImage(data=top.rgtarrow)
top.lftpic=PhotoImage(data=top.lftarrow)

ref=Button(top,image=refpic,bg="#ffd2ab",bd=0,command=reset)
ref.place(x=0,y=35)

exp=Button(top,image=top.rgtpic,bg="#ffd2ab",bd=0,command=expand)
exp.place(x=400,y=0)

txt=Entry(top,bd=5,font=("Arial Rounded MT",17),width=23)
txt.place(x=60,y=400)


compformula1 = Label(top,font=("cooper",17),text="Molecular Formula",bg="#ffd2ab",fg="#cc0066")
compformula1.place(x=115,y=450)

compformula2 = Label(top,font=("cooper",16),text=" ",width=25,bd=5)
compformula2.place(x=60,y=480)


compname1 = Label(top,font=("cooper",17),text="Molecular Name",bg="#ffd2ab",fg="#cc0066")
compname1.place(x=115,y=530)

compname2 = Label(top,font=("cooper",16),text=" ",width=25,bd=5)
compname2.place(x=60,y=560)


compweight1 = Label(top,font=("cooper",17),text="Molecular Weight",bg="#ffd2ab",fg="#cc0066")
compweight1.place(x=115,y=610)

compweight2 = Label(top,font=("cooper",16),text=" ",width=25,bd=5)
compweight2.place(x=60,y=640)

top.bind('<Return>', getinfo)


top.configure(background="#ffd2ab")
top.geometry('430x700')
top.update()
top.mainloop()
