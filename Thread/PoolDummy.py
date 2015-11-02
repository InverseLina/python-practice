__author__ = 'Hinsteny'

from urllib import request
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'http://www.python.org',
    'http://www.python.org/about',
    'http://www.python.org/doc',
    'http://www.python.org/community'
]

# Make the Pool of workers
pool = ThreadPool(4)
# Open the urls in their own threads
# and return the results
results = pool.map(request.urlopen(), urls)
# close the pool and wait for the work to finish
pool.close()
pool.join()

results = []

for url in urls:
    result = request.urlopen(url)
    results.append(result)

