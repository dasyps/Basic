import psutil
import sqlite3

def k_to_gb(num):
    num /= 1024.0
    num /= 1024.0
    num /= 1024.0
    return "%.1f" % (num)

def get_memdata():
    mem_info = psutil.virtual_memory()
    total = mem_info.total
    available = mem_info.available
    percent = mem_info.percent
    used = mem_info.used
    total = k_to_gb(total)
    available = k_to_gb(available)
    used = k_to_gb(used)
    return float(total),float(available),float(percent),float(used)

def get_cpudata():
    cpu_info = psutil.cpu_times(percpu=False)
    user = cpu_info.user % 100
    system = cpu_info.system  % 100 
    idle = cpu_info.idle % 100
    return user,system,idle

def create_mon_db():
    if db file exists:
        dont create_mon_db
    else:
        create database

def create_mon_db_conn():

def main():
    total,available,percent,used = get_memdata()
    user,system,idle = get_cpudata()
    print(f"CPU:Idle={idle:.2f}|User={user:.2f}|System={system:.2f}")
    print(f"MEM:Total={total:.2f}|Avail={available:.2f}|Used={used:.2f}|Percent={percent:.2f}")

if __name__ == '__main__':
    main()
