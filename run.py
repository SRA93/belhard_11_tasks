from db import client
from utils.class_bench import class_bench
from utils.func_bench import func_bench
from view.my_function import wait_1_sec


@func_bench
def test_1(test: str):
    wait_1_sec()
    print(test)


@class_bench
class Second:

    color = "red"
    form = "circle"

    def changecolor(self, newcolor):
        self.color = newcolor

    def changeform(self, newform):
        self.form = newform


if __name__ == '__main__':

    test_1("Hello World!")
    obj1 = Second()
    obj2 = Second()
    print(obj1.color, obj1.form)
    print(obj2.color, obj2.form)
    obj1.changecolor("green")
    obj2.changecolor("blue")
    obj2.changeform("oval")
    print(obj1.color, obj1.form)
    print(obj2.color, obj2.form)
    benchmarks = client.benchmarks
    class_benchmark = benchmarks.class_functions_benchmark
    func_benchmark = benchmarks.functions_benchmark
    func_result = func_benchmark.find()
    class_result = class_benchmark.find()
    print(func_result)
    print(class_result)
