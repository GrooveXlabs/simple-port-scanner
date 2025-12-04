import socket

def scan_port(host: str, port: int) -> bool:
    """Return True if the TCP port is open on the given host."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # timeout in seconds
    try:
        s.connect((host, port))
        s.close()
        return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def main():
    print("=== Groovexlabs Simple Port Scanner ===\n")

    host = input("Enter host to scan (e.g. 127.0.0.1 or scanme.nmap.org): ").strip()

    try:
        start_port = int(input("Enter start port (e.g. 1): ").strip())
        end_port = int(input("Enter end port (e.g. 1024): ").strip())
    except ValueError:
        print("\n[!] Please enter valid numbers for ports.")
        return

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("\n[!] Port range must be between 1 and 65535, and start <= end.")
        return

    print(f"\nScanning {host} from port {start_port} to {end_port}...\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)

    if open_ports:
        print("\nScan complete. Open ports:")
        for p in open_ports:
            print(f"- {p}")
    else:
        print("\nScan complete. No open ports found in this range.")


if __name__ == "__main__":
    main()
