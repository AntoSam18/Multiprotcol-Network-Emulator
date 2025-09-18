from flask import Flask, render_template, request, send_file, session
import scapy.all as scapy
import random
import time
import os
import matplotlib
matplotlib.use('Agg')
from fpdf import FPDF

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # required for session management


# ---------------------------
# Encryption Overhead Simulation
# ---------------------------
def simulate_encryption(packet_size, encryption_enabled):
    if encryption_enabled:
        encrypted_size = packet_size * 1.3  # Assume 30% size increase
        latency = random.uniform(0.05, 0.2)  # additional latency
    else:
        encrypted_size = packet_size
        latency = random.uniform(0.01, 0.05)
    return encrypted_size, latency


# ---------------------------
# Packet Tampering Detection
# ---------------------------
def detect_tampering():
    return random.choice([True, False])


# ---------------------------
# Packet Transmission Simulation
# ---------------------------
def send_packets(protocol, dst_ip, num_packets, encryption_enabled, packet_size, window_size, retransmission_timeout):
    sent, received, lost, tampered = 0, 0, 0, 0
    loss_rate = random.uniform(0.1, 0.5)
    receive_times = []

    for _ in range(num_packets):
        encrypted_size, latency = simulate_encryption(packet_size, encryption_enabled)

        if protocol == "TCP":
            packet = scapy.IP(dst=dst_ip) / scapy.TCP()
        elif protocol == "UDP":
            packet = scapy.IP(dst=dst_ip) / scapy.UDP()
        elif protocol == "ICMP":
            packet = scapy.IP(dst=dst_ip) / scapy.ICMP()
        elif protocol == "Telnet":
            packet = scapy.IP(dst=dst_ip) / scapy.TCP(dport=23)
        elif protocol == "RPC":
            packet = scapy.IP(dst=dst_ip) / scapy.TCP(dport=111)
        else:
            raise ValueError(f"Unsupported protocol: {protocol}")

        sent += 1
        start_time = time.time()

        if random.random() > loss_rate:
            scapy.send(packet, verbose=False)
            time.sleep(latency)
            end_time = time.time()
            received += 1
            receive_times.append(end_time - start_time)
            if detect_tampering():
                tampered += 1
        else:
            lost += 1

    success_rate = (received / sent) * 100 if sent > 0 else 0
    return sent, received, lost, tampered, loss_rate, receive_times, success_rate


# ---------------------------
# Retransmission Simulation
# ---------------------------
def retransmit_packets(protocol, dst_ip, num_lost):
    retransmitted = 0
    retrans_loss_rate = random.uniform(0.05, 0.3)
    start_time = time.time()

    for _ in range(num_lost):
        if protocol == "TCP":
            packet = scapy.IP(dst=dst_ip) / scapy.TCP()
        elif protocol == "UDP":
            packet = scapy.IP(dst=dst_ip) / scapy.UDP()
        elif protocol == "ICMP":
            packet = scapy.IP(dst=dst_ip) / scapy.ICMP()
        elif protocol == "Telnet":
            packet = scapy.IP(dst=dst_ip) / scapy.TCP(dport=23)
        elif protocol == "RPC":
            packet = scapy.IP(dst=dst_ip) / scapy.TCP(dport=111)
        else:
            raise ValueError(f"Unsupported protocol: {protocol}")

        if random.random() > retrans_loss_rate:
            scapy.send(packet, verbose=False)
            retransmitted += 1

    end_time = time.time()
    retransmission_time = end_time - start_time
    return retransmitted, retransmission_time, retrans_loss_rate


# ---------------------------
# PDF Report Generator
# ---------------------------
def generate_report(results, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Network Simulation Report", ln=True, align='C')
    pdf.ln(10)

    for res in results:
        line = (
            f"Protocol: {res[0]}, "
            f"Sent: {res[1]}, "
            f"Received: {res[2]}, "
            f"Lost: {res[3]}, "
            f"Tampered: {res[4]}, "
            f"Retransmitted: {res[5]}, "
            f"Retransmission Time: {res[6]:.3f}s, "
            f"Success Rate: {res[7]:.2f}%"
        )
        pdf.multi_cell(0, 10, line)

    pdf.output(filename)


# ---------------------------
# Routes
# ---------------------------
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/simulate', methods=['POST'])
def run_simulation():
    dst_ip = request.form['dst_ip']
    packet_size = int(request.form['packet_size'])
    window_size = int(request.form['window_size'])
    retransmission_timeout = int(request.form['retransmission_timeout'])
    encryption_enabled = 'encryption' in request.form

    results = []
    protocols = ["TCP", "UDP", "RPC", "Telnet", "ICMP"]

    for protocol in protocols:
        num_packets = int(request.form[f'{protocol.lower()}_packets'])
        sent, received, lost, tampered, loss_rate, receive_times, success_rate = send_packets(
            protocol, dst_ip, num_packets, encryption_enabled, packet_size, window_size, retransmission_timeout
        )
        retransmitted, retrans_time, retrans_loss = retransmit_packets(protocol, dst_ip, lost)
        results.append([protocol, sent, received, lost, tampered, retransmitted, retrans_time, success_rate])

    # Generate report
    report_path = 'static/report.pdf'
    generate_report(results, report_path)

    # Store results in session
    session['simulation_results'] = results

    return render_template('results.html', results=results, report_path=report_path)


@app.route('/download_report')
def download_report():
    report_path = 'static/report.pdf'
    if not os.path.exists(report_path):
        return "Report not found. Please run a simulation first."

    return send_file(report_path, as_attachment=True)


# ---------------------------
# Run Flask App
# ---------------------------
if __name__ == '__main__':
    app.run(debug=True)
