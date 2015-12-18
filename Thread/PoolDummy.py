
__author__ = 'Hinsteny'

from urllib import request
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'https://www.baidu.com/',
    'http://music.baidu.com/',
    'http://news.baidu.com/',
    'http://baike.baidu.com/'
]

# Make the Pool of workers
pool = ThreadPool(4)
# Open the urls in their own threads
# and return the results
results = pool.map(request.urlopen, urls)
# close the pool and wait for the work to finish
pool.close()
pool.join()

results = []

for url in urls:
    result = request.urlopen(url)
    results.append(list(result),)

print(results)

