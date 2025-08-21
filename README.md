# System Scrutinizer

<p align="center">
  <picture>
    <img width="420" height="420" src="../resources/logo.png" alt="System Scrutinizer logo" unselectable="on">
  </picture>
  <div align="center">Logo created using <a href="https://www.bing.com/images/">bing ai</a>.</div>
</p>

**System Scrutinizer** is a Python-based tool designed to analyze and report on the security posture of Windows 10 and 11 systems. This tool leverages PowerShell commands to execute various system checks and generate a comprehensive HTML report, ensuring compliance with the CIS Windows Benchmark.

## Features

- **Detailed Reporting**: Generates an HTML report including:
  - Operating System details
  - Hardware security status (e.g., TPM and Secure Boot)
  - Installed and startup software lists
  - Installed OS security patch information
  - Virus protection details
- **Cross-Platform Compatibility**: Works seamlessly on both Windows 10 and 11.

## Requirements

- Python 3.x

## Installing From Sources
Clone the repository to your local machine using the following command:
```bash
git clone https://github.com/Hrishikesh7665/System-Scrutinizer.git
```
Alternatively, You can Download and Extract the Zip

`Direct Download Zip` [Click Here](https://github.com/Hrishikesh7665/System-Scrutinizer/archive/refs/heads/main.zip)

## Usage
Run Command Prompt as Administrator
  ```bash
  cd System-Scrutinizer
  python audit.py
  ```

## Output
The generated HTML report will include:

- System Information
- Security Compliance
- Software Inventory
- Virus Protection Status
- Hardware Security Features
- USB history
- More

Report Sample [Click Here](https://raw.githack.com/Hrishikesh7665/System-Scrutinizer/refs/heads/resources/DESKTOP_T40RSIR_final_report_20-26-49-31-10-2024.html)

Report Preview:
- Sample 1
  ![System-Scrutinizer_Report_Preview-1](../resources/Screenshots/System-Scrutinizer_Report_Preview-1.png)
- Sample 2
  ![System-Scrutinizer_Report_Preview-2](../resources/Screenshots/System-Scrutinizer_Report_Preview-2.png)
- Sample 3
  ![System-Scrutinizer_Report_Preview-3](../resources/Screenshots/System-Scrutinizer_Report_Preview-3.png)
