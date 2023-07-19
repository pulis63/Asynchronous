#example of getting the curret task from the main coroutine
import asyncio

#define a main coroutine
async def main():
    #report a message
    print('main oroutine started')
    #get the current task
    task = asyncio.current_task()
    #report its details
    print(task)
#start the asyncio program
asyncio.run(main())