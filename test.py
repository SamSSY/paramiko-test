import paramiko, base64
import logging
paramiko.util.log_to_file("log.txt")
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
client.connect('169.254.220.8', username='pi', password='raspberry')
stdin, stdout, stderr = client.exec_command('ls')
for line in stdout:
    print '... ' + line.strip('\n')
client.close()