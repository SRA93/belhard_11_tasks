from db import client
import time
import inspect


def get_module_name(func):

    return inspect.getmodule(func)


def func_bench(func, cls):

    def wrapper(*args, **kwargs):

        print(args)
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        benchmarks = client.benchmarks
        class_func_bench = benchmarks.class_functions_benchmark
        class_func_benchdata = {"class_name": cls.__name__,
                                "module": get_module_name(func).__name__,
                                "function": func.__name__,
                                "args": args[1:],
                                "kwargs": kwargs,
                                "start_time": start_time,
                                "end_time": end_time,
                                "duration": end_time - start_time}
        class_func_bench.insert_one(class_func_benchdata)

    return wrapper


def class_bench(cls):

    functions = {k: v for k, v in cls.__dict__.items() if callable(v)}

    for name, func in functions.items():

        func_name = str(func.__name__)

        if func_name.startswith('__'):
            continue

        else:
            dec_func = func_bench(func, cls)
            setattr(cls, name, dec_func)

    return cls
