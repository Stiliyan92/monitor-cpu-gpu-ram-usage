import re

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

proc_reader = ProcReader()
#print(proc_reader.get_cpuinfo())
