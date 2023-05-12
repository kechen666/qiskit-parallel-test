import numpy as np

# 导入Qiskit相关库
from qiskit import QuantumCircuit
from qiskit.circuit.library import QuantumVolume
from qiskit import Aer, transpile
from qiskit.providers.aer import AerSimulator
# from qiskit.tools.visualization import plot_histogram

time_list = []

for qubits in range(1,30):
    shots = 1024
    depth = 10
    # qubits = 20

    circ = QuantumVolume(qubits, depth, seed=0)
    circ.measure_all()          # 对全部量子比特添加测量操作

    # 打印电路
    #print(circ)

    # 根据模拟器类型，对电路进行转译（可理解为编译电路）

    simulator = Aer.get_backend('aer_simulator_statevector')

    simulator.set_options(shots = shots, max_parallel_threads = 0, max_parallel_experiments = 1, max_parallel_shots = 0, statevector_parallel_threshold = qubits-1)

    # simulator = AerSimulator(method="statevector")
    circ = transpile(circ, simulator)

    # 模拟器运行
    result = simulator.run(circ).result()
    # 获取结果计数情况
    counts = result.get_counts(circ)

    # 输出结果：
    # print("backend_name: ",result.backend_name)
    print("qubits: ",qubits)
    print("results.metadata: ", result.results[0].metadata)
    # print("metadata", result.metadata)
    # print("header: ", result.results[0].header)
    print("shots: ", result.results[0].shots)
    # print("Experiment time: ", result.results[0].time_taken)
    print("totle time: ", result.time_taken)
    time_list.append(result.time_taken)

print(time_list)