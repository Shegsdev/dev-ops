import subprocess
servers = ["google.com" , "amazon.com" , "microsoft.com" , "wiki.org"]



def ping_server(ip):
    try:
        command = ['ping', ip, '-c' , '1']
        if subprocess.os.name == 'nt':
            command = ['ping', ip, '-n' , '1']

        # output = subprocess.check_output(command)
        output = subprocess.run(command, text=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print(output)
        return
        if output.returncode == 0:
            print(f'{ip} is reachable')
        else:
            print(f'{ip} is not reachable')
    except Exception as e:
            print(f'Error pinging {ip}:{e}')


if __name__ == "__main__":
    for server in servers:
        ping_server(server)