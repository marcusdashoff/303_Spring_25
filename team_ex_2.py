# Concurrency example using multiple implementations
# Example searches for a topic on wikipedia, gets related topics and 
#   saves the references from related topics in their own text file
# info on wikipedia library: https://thepythoncode.com/article/access-wikipedia-python
# info on concurrent.futures library: https://docs.python.org/3/library/concurrent.futures.html#

import time
import wikipedia
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from contextlib import contextmanager

#convert objects produced by wikipedia package to a string var for saving to text file
def convert_to_str(obj):
  mystr = '\n'.join(obj)
  return mystr

def dl_and_save(item):
    page = wikipedia.page(item, auto_suggest=False)
    title = page.title
    references = convert_to_str(page.references)
    out_filename = title + ".txt"
    print(f'writing to {out_filename}')
    with open(out_filename, 'w') as fileobj:
      fileobj.write(references)

# IMPLEMENTATION 1: sequential example
@contextmanager
def measure_time(label):
  t_start = time.perf_counter()
  yield
  t_end = time.perf_counter()
  print(f'{label} executed in {t_end - t_start} seconds')

def wiki_sequentially():
  print('\nsequential function:')
  with measure_time("Sequential function"):
    results = wikipedia.search("general artificial intelligence")
    for item in results:
      dl_and_save(item)

# IMPLEMENTATION 2: concurrent example w/ threads
def concurrent_threads():
  print('\nthread pool function:')
  with measure_time("Thread pool function"):
    results = wikipedia.search("general artificial intelligence")
    with ThreadPoolExecutor() as executor:
      executor.map(dl_and_save, results)

# IMPLEMENTATION 3: concurrent example w/ processes
def concurrent_process():
  print('\nprocess pool function:')
  with measure_time("Process pool function"):
    results = wikipedia.search("general artificial intelligence")
    with ProcessPoolExecutor() as executor:
      executor.map(dl_and_save, results)

if __name__ == "__main__":
  wiki_sequentially()
  concurrent_threads()
  concurrent_process()