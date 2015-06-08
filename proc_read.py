import re
import os


class Process:

    def __init__(self, pid, user, virt_memory, phys_memory, status, cpu_time, command):
        self.pid, self.user, self.command = pid, user, command
        self.virt_memory, self.phys_memory = virt_memory, phys_memory
        self.cpu_time, self.status = cpu_time, status


class ProcReader:

    def get_meminfo(self):
        re_parser = re.compile(r'^(?P<key>\w*):\s*(?P<value>\w*)\s*')
        memory_info = {}
        for line in open('/proc/meminfo'):
            match = re_parser.match(line)
            if not match:
                continue
            key, value = match.groups(['key', 'value'])
            memory_info[key] = int(value)
        return memory_info

    def get_cpuinfo(self):
        re_parser = re.compile(r'^(?P<key>\w*)\s*:\s(?P<value>\w*)\s*')
        cpu_info = {}
        for line in open('/proc/cpuinfo'):
            match = re_parser.match(line)
            if not match:
                continue
#            print(match.groups())
            key, value = match.groups(['key', 'value'])
            cpu_info[key] = value
        return cpu_info


    def read_processes(self):
        return [get_pidinfo(pid) for pid in os.listdir('/proc') if pid.isdigit()]


    def get_pidinfo(self, pid):
        stat = os.popen('cat /proc/%s/stat' % pid).read()
        return Process()


proc_reader = ProcReader()
#print(proc_reader.get_cpuinfo())
