from db import client
import time
import inspect


def get_module_name(func):

    return inspect.getmodule(func)


def func_bench(func):

    def wrapper(*args, **kwargs):

        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        benchmarks = client.benchmarks
        func_bench = benchmarks.functions_benchmark
        func_benchdata = {"module": get_module_name(func).__name__,
                          "function": func.__name__,
                          "args": args,
                          "kwargs": kwargs,
                          "start_time": start_time,
                          "end_time": end_time,
                          "duration": end_time - start_time}
        func_bench.insert_one(func_benchdata)

    return wrapper
