import psutil
from rich import print

# CPU Information
cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
cpu_freq = psutil.cpu_freq()

# Memory Usage
memory = psutil.virtual_memory()
print(f"Memory Total: {memory.total / (1024**3):.2f} GB")
print(f"Memory Available: {memory.available / (1024**3):.2f} GB")
print(f"Memory Percent used: {memory.percent}%")

# Disk Usage
disk = psutil.disk_usage('/')
print(f"Disk Total: {disk.total / (1024**3):.2f} GB")
print(f"Disk Free: {disk.free / (1024**3):.2f} GB")

# Process Management
listOfProcObjects = []
for proc in psutil.process_iter():
    #print(proc.info)
    try:
        pinfo = proc.as_dict(attrs=['pid', 'name', 'cpu_percent', 'username'])
        pinfo['vms'] = round(proc.memory_info().vms / (1024 * 1024), 2)
        # Append dict to list
        listOfProcObjects.append(pinfo)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# Sort list of dict by key vms i.e. memory usage
listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)[:10]
print("Top processes as per memory usage:")
print(listOfProcObjects)

# Network Information
net_io = psutil.net_io_counters()
print(f"Bytes sent: {net_io.bytes_sent}")
print(f"Bytes received: {net_io.bytes_recv}")