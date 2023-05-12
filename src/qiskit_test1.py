import numpy as np

# 导入Qiskit相关库
from qiskit import QuantumCircuit
from qiskit import Aer, transpile
# from qiskit.tools.visualization import plot_histogram


circ = QuantumCircuit(2)    # 创建两个量子比特量子电路
circ.h(0)                   # 应用H门到0号逻辑量子比特
circ.cx(0, 1)               # 应用CNOT门，其中0号逻辑量子比特为控制比特，1号逻辑量子比特为受控比特
circ.measure_all()          # 对全部量子比特添加测量操作

# 打印电路
print(circ)

# 根据模拟器类型，对电路进行转译（可理解为编译电路）
simulator = Aer.get_backend('aer_simulator_statevector')
circ = transpile(circ, simulator)

# 模拟器运行
result = simulator.run(circ).result()
# 获取结果计数情况
counts = result.get_counts(circ)
print(result)
# 输出结果：

# print("results.metadata: ", result.results[0].metadata)
# print("metadata", result.metadata)
# print("header: ", result.results[0].header)
print("shots: ", result.results[0].shots)
# print("Experiment time: ", result.results[0].time_taken)
print("totle time: ", result.time_taken)