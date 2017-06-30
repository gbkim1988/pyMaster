import pipes
import subprocess

ps = subprocess.Popen(('C:\\Windows\\System32\\NETSTAT.EXE', '-A'), stdout=subprocess.PIPE)
output = subprocess.check_output(('findstr', '192.168.3.169'), stdin=ps.stdout)
print(x for x in output.splitlines())
ps.wait()