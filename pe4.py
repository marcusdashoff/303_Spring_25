import time
import wikipedia
from concurrent.futures import ThreadPoolExecutor

def wiki_dl_and_save(topic):
    page = wikipedia.page(topic, auto_suggest = False)
    page_title = page.title
    page_reference = page.references
    txt_file_name = f"{page_title}.txt"
    with open(txt_file_name, "w", encoding="utf-8") as file:
        file.write("\n".join(page_reference))  

def im_just_super_slow_as_you_wish_with_sequential_download(): 
    begin = time.perf_counter()
    search = wikipedia.search("generative artificial intelligence")
    
    for item in search: 
        wiki_dl_and_save(item)  
    
    end = time.perf_counter()
    print(f"Sequentially downloaded time: {end - begin:.2f}s")
    
def im_just_surprisingly_fast_with_threads():
    begin = time.perf_counter()
    search = wikipedia.search("generative artificial intelligence")
    
    with ThreadPoolExecutor() as executor:
        executor.map(wiki_dl_and_save, search)
    
    end = time.perf_counter()
    print(f"ThreadPool downloaded time: {end - begin:.2f}s")

if __name__ == "__main__":
    print("Start Downloading...\n")
    im_just_super_slow_as_you_wish_with_sequential_download()
    im_just_surprisingly_fast_with_threads()