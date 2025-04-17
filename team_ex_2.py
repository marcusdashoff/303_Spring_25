# Concurrency example using multiple implementations
# Example searches for a topic on wikipedia, gets related topics and 
#   saves the references from related topics in their own text file
# info on wikipedia library: https://thepythoncode.com/article/access-wikipedia-python
# info on concurrent.futures library: https://docs.python.org/3/library/concurrent.futures.html#

import time
import wikipedia
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from contextlib import contextmanager
import os

#convert objects produced by wikipedia package to a string var for saving to text file
def convert_to_str(obj):
  mystr = '\n'.join(obj)
  return mystr

def dl_and_save(item):
    page = wikipedia.page(item, auto_suggest=False)
    title = page.title
    references = convert_to_str(page.references)
    os.makedirs("wiki_dl", exist_ok=True)
    out_filename = "wiki_dl/" + title + ".txt"
    print(f'writing to {out_filename}')
    with open(out_filename, 'w') as fileobj:
      fileobj.write(references)

@contextmanager
def measure_time(label):
  t_start = time.perf_counter()
  yield
  t_end = time.perf_counter()
  print(f'{label} executed in {t_end - t_start} seconds')

def wiki_sequentially(results):
  print('\nsequential function:')
  with measure_time("Sequential function"):
    for item in results:
      dl_and_save(item)

def concurrent_threads(results):
  print('\nthread pool function:')
  with measure_time("Thread pool function"):
    with ThreadPoolExecutor() as executor:
      executor.map(dl_and_save, results)

def concurrent_process(results):
  print('\nprocess pool function:')
  with measure_time("Process pool function"):
    with ProcessPoolExecutor() as executor:
      executor.map(dl_and_save, results)

if __name__ == "__main__":
  user_input = input("What ya tryna search: ")
  
  if len(user_input) < 4:
    user_input = "general artificial intelligence"
  results = wikipedia.search(user_input)
  
  try:
    wiki_sequentially(results)
    concurrent_threads(results)
    concurrent_process(results)
  except:
    print("Ambigious search. Neeed more details!!!")