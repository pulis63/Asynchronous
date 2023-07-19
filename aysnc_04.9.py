# example of an asynchronous iterator with async for loop 
import asyncio
import time

# define an asynchronous iterator
class AsyncIterator():
    # constructor, define some state 
    def __init__(self):
        self.counter = 0

    # create an instance of the iterator                 # Wed Jul 19 14:04:48 2023 1
    def __aiter__(self):                                 # Wed Jul 19 14:04:49 2023 2
        return self                                      # Wed Jul 19 14:04:50 2023 3
                                                         # Wed Jul 19 14:04:51 2023 4
    # return the next awaitable                          # Wed Jul 19 14:04:52 2023 5
    async def __anext__(self):                           # Wed Jul 19 14:04:53 2023 6
        # check for no furture items                     # Wed Jul 19 14:04:54 2023 7
        if self.counter >= 10:                           # Wed Jul 19 14:04:55 2023 8
            raise StopAsyncIteration                     # Wed Jul 19 14:04:56 2023 9
        # increment the counter                          # Wed Jul 19 14:04:57 2023 10
        self.counter += 1
        # simulate work
        await asyncio.sleep(1)
        # return the counter value
        return self.counter

# main coroutine
async def main():
    # loop over async iterator with async for loop 
    async for item in AsyncIterator():
        print (f'{time.ctime()} {item}')
# execute the asyncio program
asyncio.run(main())