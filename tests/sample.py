# Asked ChatGPT to genrate a random python file which is long to test the pipeline and see
# difference between basic and optimized version 

class myClass:
    pass

def Func(a, b, c, d):
    return a + b
import math
import os
import random
import statistics


class DataProcessor:
    def __init__(self, values):
        self.values = values

    def normalize(self):
        total = sum(self.values)
        if total == 0:
            return self.values
        return [v / total for v in self.values]

    def moving_average(self, window):
        result = []
        for i in range(len(self.values)):
            start = max(0, i - window + 1)
            chunk = self.values[start:i + 1]
            result.append(sum(chunk) / len(chunk))
        return result

    def variance(self):
        mean = sum(self.values) / len(self.values)
        acc = 0
        for v in self.values:
            acc += (v - mean) * (v - mean)
        return acc / len(self.values)


class CodeMetrics:
    def __init__(self, name, lines, functions):
        self.name = name
        self.lines = lines
        self.functions = functions

    def score(self):
        return self.lines + self.functions * 10

    def is_large(self):
        return self.lines > 100


class ReportBuilder:
    def __init__(self):
        self.sections = []

    def add_section(self, title, body):
        self.sections.append((title, body))

    def build(self):
        output = []
        for title, body in self.sections:
            output.append("# " + title)
            output.append(body)
        return "\n".join(output)


def helper_1(a, b):
    return a + b


def helper_2(a, b):
    return a - b


def helper_3(a, b):
    return a * b


def helper_4(a, b):
    if b == 0:
        return 0
    return a / b


def helper_5(a, b, c, d, e):
    return a + b + c + d + e


def compute_series_1(n):
    values = []
    for i in range(n):
        values.append(i * i + 3 * i + 1)
    return values


def compute_series_2(n):
    values = []
    for i in range(n):
        if i % 2 == 0:
            values.append(i // 2)
        else:
            values.append(3 * i + 1)
    return values


def compute_series_3(n):
    values = []
    for i in range(n):
        values.append(math.sin(i) + math.cos(i))
    return values


def analyze_values(values):
    result = {}
    result["count"] = len(values)
    result["min"] = min(values)
    result["max"] = max(values)
    result["sum"] = sum(values)
    result["mean"] = sum(values) / len(values)
    return result


def format_result(name, data):
    lines = []
    lines.append("Result for " + name)
    for key, value in data.items():
        lines.append(str(key) + ": " + str(value))
    return "\n".join(lines)


def long_line_function():
    text = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx xxx xxxxxx xxxxx xxxxxx xxxxxxxxxxxx xxxxxxxxx xxxxxxxxx xxxxxxxxxx xxxxxxxxxxx xxxx xxx xxxxxxxxxxx xxx"
    return text


def function_with_many_args(a, b, c, d, e, f):
    return a + b + c + d + e + f


def pipeline_step_1(data):
    output = []
    for item in data:
        output.append(item + 1)
    return output


def pipeline_step_2(data):
    output = []
    for item in data:
        output.append(item * 2)
    return output


def pipeline_step_3(data):
    output = []
    for item in data:
        if item % 3 == 0:
            output.append(item)
    return output


def pipeline_step_4(data):
    output = {}
    for item in data:
        key = item % 5
        if key not in output:
            output[key] = []
        output[key].append(item)
    return output


def pipeline_step_5(groups):
    result = []
    for key, values in groups.items():
        result.append((key, sum(values)))
    return result


def repeated_func_01(x):
    y = x + 1
    z = y * 2
    return z


def repeated_func_02(x):
    y = x + 2
    z = y * 3
    return z


def repeated_func_03(x):
    y = x + 3
    z = y * 4
    return z


def repeated_func_04(x):
    y = x + 4
    z = y * 5
    return z


def repeated_func_05(x):
    y = x + 5
    z = y * 6
    return z


def repeated_func_06(x):
    y = x + 6
    z = y * 7
    return z


def repeated_func_07(x):
    y = x + 7
    z = y * 8
    return z


def repeated_func_08(x):
    y = x + 8
    z = y * 9
    return z


def repeated_func_09(x):
    y = x + 9
    z = y * 10
    return z


def repeated_func_10(x):
    y = x + 10
    z = y * 11
    return z


def repeated_func_11(x):
    y = x + 11
    z = y * 12
    return z


def repeated_func_12(x):
    y = x + 12
    z = y * 13
    return z


def repeated_func_13(x):
    y = x + 13
    z = y * 14
    return z


def repeated_func_14(x):
    y = x + 14
    z = y * 15
    return z


def repeated_func_15(x):
    y = x + 15
    z = y * 16
    return z


def repeated_func_16(x):
    y = x + 16
    z = y * 17
    return z


def repeated_func_17(x):
    y = x + 17
    z = y * 18
    return z


def repeated_func_18(x):
    y = x + 18
    z = y * 19
    return z


def repeated_func_19(x):
    y = x + 19
    z = y * 20
    return z


def repeated_func_20(x):
    y = x + 20
    z = y * 21
    return z


def repeated_func_21(x):
    y = x + 21
    z = y * 22
    return z


def repeated_func_22(x):
    y = x + 22
    z = y * 23
    return z


def repeated_func_23(x):
    y = x + 23
    z = y * 24
    return z


def repeated_func_24(x):
    y = x + 24
    z = y * 25
    return z


def repeated_func_25(x):
    y = x + 25
    z = y * 26
    return z


def repeated_func_26(x):
    y = x + 26
    z = y * 27
    return z


def repeated_func_27(x):
    y = x + 27
    z = y * 28
    return z


def repeated_func_28(x):
    y = x + 28
    z = y * 29
    return z


def repeated_func_29(x):
    y = x + 29
    z = y * 30
    return z


def repeated_func_30(x):
    y = x + 30
    z = y * 31
    return z


def run_all():
    data = compute_series_1(100)
    data = pipeline_step_1(data)
    data = pipeline_step_2(data)
    data = pipeline_step_3(data)
    groups = pipeline_step_4(data)
    summary = pipeline_step_5(groups)
    return summary