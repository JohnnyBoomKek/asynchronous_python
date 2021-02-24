import requests
import time 
import asyncio
import aiohttp
import random 

### ______ syncronous file downoader 

def get_file(url):
    res = requests.get(url)
    return res

def write_file(response):
    filename = 'file ' + str(int(time.time()))
    with open(filename, 'wb') as f:
        f.write(response.content)
        print(filename, 'saved')

#takse around 13 seconds on avg
def sync_main():
    t0 = time.time()
    url = 'https://loremflickr.com/320/240'
    for _ in range(10):
        write_file(get_file(url))
    print(f'It looks like it took us {time.time() - t0} seconds' )
    

### ____ async file downloader 
def write_image(data):
    filename = f'file {random.randint(0, 123213)}.jpg'
    with open(filename, 'wb') as file:
        file.write(data)
        print(filename, "was created")

async def fetch_img(url, session):
    async with session.get(url, allow_redirects=True) as response:
        #returns bynary of the response
        data = await response.read()
        write_image(data)

#takes about 3 seconds
async def async_main():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_img(url, session))
            tasks.append(task)
        
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    t0 = time.time()
    asyncio.run(async_main())
    print(f'It looks like it took us about {time.time() - t0} seconds')