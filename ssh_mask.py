import os

def main():
    process = [
        "systemctl mask sshd",
        "systemctl stop sshd",
	"clear"]
    
    for p in process:
        os.popen(p)

main()
