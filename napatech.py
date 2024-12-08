import napatech as nt

def replay_pcap(pcap_file, adapter):
    """
    Replays a PCAP file using the Napatech adapter.
    :param pcap_file: Path to the PCAP file.
    :param adapter: Napatech adapter object.
    """
    print(f"Replaying PCAP: {pcap_file}")
    adapter.replay_pcap(pcap_file, loop=10)
    print("PCAP replay complete.")

if __name__ == "__main__":
    pcap_file = "/path/to/your/pcap/file.pcap"
    try:
        adapter = nt.open("nt3g", mode=nt.WRITE_MODE)
        replay_pcap(pcap_file, adapter)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        adapter.close()