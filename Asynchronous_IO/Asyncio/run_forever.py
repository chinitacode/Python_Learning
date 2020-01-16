import asyncio

async def func(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')

def call_result(future):
    print(future.result())
    loop.stop()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(func(future)) #确保这个是一个 Future 对象：Task 是 Future 子类, 创建task
    future.add_done_callback(call_result)        # 注意这行
    try:
        loop.run_forever()
    finally:
        loop.close()
