import paramiko


def execute_ssh_command(
    hostname,
    username,
    password,
    command,
    port=22
):
    try:
        client = paramiko.SSHClient()

        client.set_missing_host_key_policy(
            paramiko.AutoAddPolicy()
        )

        client.connect(
            hostname=hostname,
            username=username,
            password=password,
            port=port
        )

        stdin, stdout, stderr = client.exec_command(command)

        output = stdout.read().decode()
        error = stderr.read().decode()

        client.close()

        return {
            "success": True,
            "output": output,
            "error": error
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }