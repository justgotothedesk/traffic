import socket
import threading
import time

def send_traffic_thread(host, port, message, target_bandwidth_gbps):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            print(f"[Thread-{threading.current_thread().name}] Connected to {host}:{port}")

            message_size = len(message)
            bytes_per_second = (target_bandwidth_gbps * 1e9) / 8
            delay_per_packet = message_size / bytes_per_second

            while True:
                start_time = time.time()
                client_socket.sendall(message.encode('utf-8'))
                elapsed_time = time.time() - start_time
                if elapsed_time < delay_per_packet:
                    time.sleep(delay_per_packet - elapsed_time)

    except Exception as e:
        print(f"[Thread-{threading.current_thread().name}] Error: {e}")

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 8080
    MESSAGE = (
        "GET / HTTP/1.1\r\n"
        "Host: localhost:8080\r\n"
        "User-Agent: TrafficGenerator\r\n"
        "Connection: Keep-Alive\r\n\r\n"
    )
    TARGET_BANDWIDTH_GBPS = 10
    NUM_THREADS = 4

    threads = []
    for i in range(NUM_THREADS):
        thread = threading.Thread(target=send_traffic_thread, args=(HOST, PORT, MESSAGE, TARGET_BANDWIDTH_GBPS / NUM_THREADS))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
