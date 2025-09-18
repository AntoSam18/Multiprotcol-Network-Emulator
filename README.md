 # 🌐 Multi-Protocol Network Emulator

The **Multi-Protocol Network Emulator** is an advanced **Flask-based web application** that simulates the behavior of multiple networking protocols including **TCP, UDP, RPC, Telnet, and ICMP**. Designed for both educational and research purposes, this project allows users to explore how different protocols react under various network conditions such as **packet loss, encryption overhead, retransmission delays, and tampering attempts**.  

This project has been thoroughly **tested in the GNS3 environment**, ensuring realistic performance measurements and compatibility with professional-grade network simulations. It offers a powerful combination of backend packet handling with **Scapy**, interactive visualization through **Bootstrap and Jinja2 templates**, and automated **PDF report generation** for deeper analysis.  

🎥 **Demo Video:** [Watch Here](https://drive.google.com/file/d/1RYjcMthORix1wIY4xgsKobR2rWClVKU4/view)  

---

## ✨ Key Features

- 🔹 Simulation of **TCP, UDP, RPC, Telnet, and ICMP** protocols in a single tool  
- 🔹 Configurable parameters: **packet size, window size, retransmission timeout**  
- 🔹 **Encryption support** with realistic latency and packet size overhead  
- 🔹 **Packet tampering detection** to mimic real-world threats  
- 🔹 **Packet loss and retransmission mechanism** with timing analysis  
- 🔹 Automatic generation of **detailed PDF reports**  
- 🔹 Clean, responsive **Bootstrap-based UI** for inputs and results  
- 🔹 Tested and validated in a **GNS3 network simulation environment**  

---

## 📂 Project Structure
```
│
├── app.py # Main Flask application with simulation logic & PDF reporting
│
├── templates/ # HTML templates for frontend
│ ├── index.html # User input form for simulation parameters
│ └── results.html # Results page with tables, insights & report download option
│
├── static/ # Static files generated/used by the app
│ └── report.pdf # Auto-generated simulation report (created after running)
│
├── requirements.txt # Python dependencies for easy setup
│
└── README.md # Project documentation
```

---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO```
2.**Install dependencies**

```bash
pip install -r requirements.txt
```
3.**Run the Flask server**
```bash
python app.py
```
📊 Example Workflow

Enter the destination IP and set parameters like packet count, size, window size, and timeout.

Choose the number of packets for each protocol (TCP, UDP, RPC, Telnet, ICMP).

Enable encryption to analyze performance with security overhead.

Run the simulation to view results including sent, received, lost, retransmitted, and tampered packets.

Download the comprehensive PDF report for further analysis.

🛠 Tech Stack

Backend: Python, Flask

Networking: Scapy (for packet crafting and sending)

Reporting: FPDF (for PDF generation)

Visualization: Bootstrap 5, Jinja2 templates

Simulation Environment: Tested and validated in GNS3

Additional Libraries: Matplotlib, Random, OS, Time

## 👨‍💻 Author

**Anto Sam Christ A**  
📧 Email: [antosamchrista@gmail.com](mailto:antosamchrista@gmail.com)
