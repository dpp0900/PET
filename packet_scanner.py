import socket
import os
import subprocess

current_dir = os.getcwd()
captures_dir = os.path.join(current_dir, "server")
os.makedirs(captures_dir, exist_ok=True)

output_file_path = os.path.join(captures_dir, "capture.pcap")

host_port = 7777

def packet_scanner():
    print("Starting packet capture...")

    # 패킷 캡처 필터
    filter = "tcp port 80"

    # 패킷 캡처 시작
    output_tmp_file_path = os.path.join(captures_dir, "capture_tmp.pcap")
    command = f"tshark -i eth0 -f '{filter}' -w {output_file_path} -F pcap"
    p = subprocess.Popen(command, shell=True)
    p.wait()

    # merge_command = f"mergecap -a -w {output_file_path} {output_tmp_file_path}"
    # p = subprocess.Popen(merge_command, shell=True)
    # p.wait()

    # os.remove(output_tmp_file_path)
    # 캡처한 패킷을 파일로 저장
    print(f"Capture saved as {output_file_path}")

# def upload_file():
#     global host_port

#     print("Uploading Result file...")

#     host_ip = '192.168.0.23'
#     print(f"Host IP: {host_ip}, Host Port: {host_port}")
    
#     # 소켓 생성
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((host_ip, host_port))

#     file_to_send = output_file_path

#     with open(file_to_send, 'rb') as f:
#         while True:
#             data = f.read(4096) #4096 바이트 단위로 청크 읽기
#             if not data:
#                 break
#             s.sendall(data)

#     print("File sent successfully.")
#     s.close()

#     if host_port == 7777:
#         host_port += 1
#     elif host_port == 7778:
#         host_port -= 1

if __name__ == '__main__':
    while True:
        packet_scanner()
