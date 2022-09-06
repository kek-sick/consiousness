
class TemporalCasualNode:

    def __init__(self, input_state: list | None, function, speed, initial_value=None):
        if input_state is not None:
            self.input_state = list(map(lambda i: i[0] * i[1], input_state))  # previous output state multiplied by weight
            self.speed = speed
            self.self_state = 0
        else:
            self.input_state = initial_value
            self.speed = 1
            self.self_state = initial_value
        self.function = function

    def step(self):
        dif = 0
        match self.function:
            case 'add':
                # print(sum(self.input_state))
                dif = self.self_state - sum(self.input_state)
            case 'mul':
                pass
            case 'max':
                pass
            case 'avg':
                dif = self.self_state - sum(self.input_state)/len(self.input_state)
            case 'min':
                dif = self.self_state - min(self.input_state)
            case 'id':
                dif = self.self_state - self.input_state
            case _:
                print('undefined function')

        self.self_state = self.self_state - (dif * self.speed)
        return self.self_state


class TemporalCasualNetwork:

    def __init__(self, nodes: list):
        self.nodes = nodes

    def step(self, n=1):
        if self.nodes is not None:
            for i in range(n):
                for node in self.nodes:
                    # node.step()
                    print(node.step())
                print('----------------------------')
