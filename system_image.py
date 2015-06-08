from proc_read import ProcReader
from time import time


class SystemImage:

    def __init__(self):
        self.time = time()
        self.memory_state = ProcReader().get_meminfo()



si = SystemImage()
print(si.memory_state)
