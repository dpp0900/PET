import paramiko
from scp import SCPClient, SCPException

class SSHManager:
    def __init__(self):
        self.ssh_client = None

    def create_ssh_client(self, hostname, username, password, port=22):
        
        if self.ssh_client is None:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(hostname, username=username, password=password, port=port)
        else:
            print("SSH client session exist.")

    def close_ssh_client(self):
        
        self.ssh_client.close()

    def send_file(self, local_path, remote_path):
        
        try:
            with SCPClient(self.ssh_client.get_transport()) as scp:
                scp.put(local_path, remote_path, preserve_times=True)
        except SCPException:
            raise SCPException

    def get_file(self, remote_path, local_path):
        
        try:
            with SCPClient(self.ssh_client.get_transport()) as scp:
                scp.get(remote_path, local_path)
        except SCPException:
            raise SCPException

    def send_command(self, command):
        
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        return stdout.readlines()
    

ssh = SSHManager()
HOST = open("scphost", "r").readline().strip()
USER = open("scpid", "r").readline().strip()
PASS = open("scppass", "r").readline().strip()
ssh.create_ssh_client(HOST, USER, PASS, 7722)
#ssh.send_command("tshark -i eth0 -f 'tcp port 80' -w /tmp/Capture/capture.pcap -F pcap")

cmd = input("Enther any key to download capture file: ")
ssh.get_file("/tmp/capture.pcap", ".")
ssh.close_ssh_client()