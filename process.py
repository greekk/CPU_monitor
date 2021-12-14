import psutil as pt

class CpuMonitor:
    def __init__(self):
        self.__cpu_count = pt.cpu_count(logical=False)
        self.__thread_count = pt.cpu_count(logical=True)

    @property
    def cpu_count(self):
        return self.__cpu_count

    @property
    def thread_count(self):
        return self.__thread_count

cpu_monitor = CpuMonitor()

print(f"real cores count: {cpu_monitor.cpu_count}, threads count: {cpu_monitor.thread_count}")
