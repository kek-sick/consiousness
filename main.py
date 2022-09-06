# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import consiousness_node as cn

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    node_A = cn.TemporalCasualNode(None, 'id', None, 0.5)
    node_B = cn.TemporalCasualNode(None, 'id', None, 0.2)
    node_C = cn.TemporalCasualNode([[node_A.self_state, 0.2], [node_B.self_state, 0.7]], 'add', 0.1)

    network = cn.TemporalCasualNetwork([node_A, node_B, node_C])
    network.step(100)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
