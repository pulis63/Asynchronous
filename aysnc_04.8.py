# example of running a blocking io-bound task in asyncio
import asyncio
import time

# a  blocking io-bound task
def blocking_task():
    # report a message                                      # Wed Jul 19 13:48:12 2023 Main running the blocking task
    print (f'{time.ctime()} Task starting...')              # Wed Jul 19 13:48:12 2023 Main doing other things
    # block for a while                                     # Wed Jul 19 13:48:12 2023 Task starting...
    time.sleep(2)                                           # Wed Jul 19 13:48:14 2023 Task done
    # report a message
    print (f'{time.ctime()} Task done')
# main coroutine
async def main():
    # report a message
    print (f'{time. ctime()} Main running the blocking task')
    # create a coroutine for the blocking task
    coro = asyncio.to_thread (blocking_task)
    # schedule the task
    task= asyncio.create_task(coro)
    # report a message
    print (f'{time.ctime()} Main doing other things')
    # allow the scheduled task to start
    await asyncio.sleep(0)
    # await the task
    await task
    
# run the asyncio program 
asyncio.run(main())