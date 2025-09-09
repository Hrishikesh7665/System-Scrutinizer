# -*- coding: utf-8 -*-
from math import ceil
import subprocess
import time
import datetime
import dateutil.parser
from configuration import red, green, yellow, log_col, debug_mode

def list_allStartup_Software():
    startup_apps_report = f"""</section>

    <div class="blurb"> </div>

    <section>
		<div class="reportSection">
			<h2 class="reportSectionHeader">
				Startup Softwares
			</h2>
			<div class="reportSectionBody">
    """
    command_startup = 'Get-CimInstance Win32_StartupCommand | Select-Object Location, Name, Command, User | sort Name | Format-List'
    result_startup = subprocess.run(["powershell", command_startup], shell=True, stdout=subprocess.PIPE)
    output_startup = result_startup.stdout.decode("utf-8").strip()
    startup_apps_report += f"""<table role="presentation">
    <thead>
        <tr>
            <th>Name <span class="rshNote">(hover mouse to show details)</span></th>
            <th>Startup Command</th>
            <th>User</th>
        </tr>
    </thead>

    <tbody>"""
    for line in output_startup.split("\n"):
        if "Location : " in line:
            startup_apps_report += f"""
        <tr>
            <td class="hasInfo" style="white-space:nowrap;" title="{str(line[11:].strip())}">"""
        if "Name     : " in line:
            startup_apps_report += f""" {str(line[11:].strip())} </td>
            """
        if "Command  : " in line:
            startup_apps_report += f"""<td> {str(line[11:].strip())} </td>
            """
        if "User     : " in line:
            startup_apps_report += f"""<td> {str(line[11:].strip())} </td>
        </tr>"""
    startup_apps_report += f"""
    </tbody>
</table>
</div>
</div>
</section>"""
    return startup_apps_report


def installed_Software ():
    report_installed_software = f"""<div class="blurb"> </div>

    <section>
        <div class="reportSection">
            <h2 class="reportSectionHeader">
                Installed Software & Application
            </h2>
            <div class="reportSectionBody">
                <table role="presentation">
                    <colgroup>
                        <col style="width: 50%">
                        <col style="width: 50%">
                    </colgroup>
                    <tr>
                        <td>
    """
    name = []
    install_date = []
    version = []
    vendor = []
    size = []
    location = []
    startup = []
    runningState = []
    ps_name = []
    ps_id = []
    bit_list = []

    command_list_software = 'Get-ItemProperty HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\*, HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Where-Object {$_.DisplayName -ne $null} | Select-Object DisplayName, InstallDate, DisplayVersion, Publisher, EstimatedSize, InstallLocation, @{Name="Bit";Expression={If($_.InstallLocation.Contains("Program Files (x86)")){"32 Bit"}Else{"64 Bit"}}} | Sort-Object DisplayName -Unique | Format-List | Out-String -Stream | ForEach-Object { $_ -replace \'[\\x00]\', \'\' }'
    result_list_software = subprocess.run(["powershell", command_list_software], shell=True, stdout=subprocess.PIPE)
    output_list_software = result_list_software.stdout.decode("utf-8", errors="ignore").strip()

    command_startup = 'Get-CimInstance Win32_StartupCommand | Select-Object Name'
    result_startup = subprocess.run(["powershell", command_startup], shell=True, stdout=subprocess.PIPE)
    output_startup = result_startup.stdout.decode("utf-8").strip().split("\n")[2:]
    output_startup = [ item.strip() for item in output_startup]

    for line in output_list_software.split("\n"):
        if "DisplayName     : " in line:
            n = line[18:].strip()
            if n!= "":
                name.append(n)
            else:
                name.append(None)
            if n in output_startup:
                startup.append('Enabled')
            else :
                startup.append('Disabled')
            command_running = 'if ((Get-Process | Where-Object {$_.MainWindowTitle -like "*'+n+'*"}) -ne $null) {return (Get-Process | Where-Object {$_.MainWindowTitle -like "*'+n+'*"} | Select-Object -Property ProcessName,Id | Format-List)} else {return $false}'
            result_running = subprocess.run(["powershell", command_running], shell=True, stdout=subprocess.PIPE)
            output_running = result_running.stdout.decode("utf-8").strip()
            if output_running == "False":
                runningState.append ('Not Running')
                ps_name.append(None)
                ps_id.append(None)
            else:
                runningState.append ('Running')
                for line2 in output_running.split("\n"):
                    if 'ProcessName : ' in line2:
                        ps_name.append(line2[14:].strip())
                    if 'Id          : ' in line2:
                        ps_id.append(line2[14:].strip())
        if "InstallDate     : " in line:
            date = line[18:].strip()
            if date!= "":
                install_date.append(date)
            else:
                install_date.append(None)
        if "DisplayVersion  : " in line:
            ver = line[18:].strip()
            if ver!= "":
                version.append(ver)
            else:
                version.append(None)
        if "Publisher       : " in line:
            pub = line[18:].strip()
            if pub!= "":
                vendor.append(pub)
            else:
                vendor.append(None)
        if "EstimatedSize   : " in line:
            si = line[18:].strip()
            if si!= "":
                size.append(si)
            else:
                size.append(None)
        if "InstallLocation : " in line:
            loc = line[18:].strip()
            if loc!= "":
                location.append(loc)
            else:
                location.append(None)
        if "Bit             : " in line:
            bit_version = line[18:].strip()
            if bit_version!= "":
                bit_list.append(bit_version)
            else:
                bit_list.append(None)
    len_dev = 0
    total_dev = len(name)
    for i in range(len(name)):
        # print ("Name : " + str(name[i]) + "\nState : " + str(runningState[i]) + "\nPsName : " + str(ps_name[i]) + "\nPsID : " + str(ps_id[i]) + "\nInstall Date : " + str(install_date[i]) + "\nVersion : " + str(version[i]) + "\nVendor : " + str(vendor[i]), "\nSize : " + str(size[i]) + "\nAuto Start : "+ str(startup[i]) +"\n")
        # report_installed_software += f"""<span class="hasInfo" title="{"Vendor: "+vendor[i] if vendor[i] is not None else ""}"> """
        len_dev = len_dev+1
        report_installed_software += '<span class="hasInfo" title="'
        if vendor[i] is not None:
            report_installed_software+="Vendor: "+vendor[i]+"\r"
        if version[i] is not None:
            report_installed_software+="Version: "+str(version[i])+"\r"
        if size[i] is not None:
            report_installed_software+="Size: "+str(size[i])+" Bytes\r"
        if install_date[i] is not None:
            yourdate = dateutil.parser.parse(str(install_date[i]))
            report_installed_software+="Install Date: "+ yourdate.strftime("%d-%m-%Y") + "\r"
        if runningState[i] is not None:
            report_installed_software+="State: "+str(runningState[i])+ "\r"
            if runningState[i] == "Running":
                if ps_name[i] is not None:
                    report_installed_software+="Process Name: "+str(ps_name[i])+ "\r"
                if ps_id[i] is not None:
                    report_installed_software+="Process ID: "+str(ps_id[i])+ "\r"
        if bit_list[i] is not None:
            report_installed_software+="Bit: "+str(bit_list[i])+"\r"
        if startup[i] is not None:
            report_installed_software+="Auto Start: "+str(startup[i])+"\r"
        if location[i] is not None:
            report_installed_software+="Install Location: "+str(location[i])+"\r"
        report_installed_software +=  f""""><span class="swLinkI">&#119946;</span></span>&nbsp;&nbsp;{name[i]}"""
        if bit_list[i] is not None:
            report_installed_software+=" (<span style=\"color:#049304; font-weight:bold;\">"+str(bit_list[i])+"</span>)"
        if (len(name) / 2) % 1 == 0 and i == (len(name) / 2):
            report_installed_software += """</td><td>
            """
        elif (len(name) / 2) % 1 != 0 and i == ceil((len(name) / 2)) - 1:
            report_installed_software +="""</td><td>
            """
        else:
            if total_dev > 1 and len_dev != total_dev:
                report_installed_software += """\r\n<br>\r\n"""
    report_installed_software += """</td>
            </tr>
            </table>
            </div>
            </div>
            <div class="rsFooter">
                <div class="footnoteList">
                    <span class="swLinkI">&nbsp;&nbsp;&nbsp;&#119946;&nbsp;</span>Mouse over to see details about the software
                </div>
            </div>
            </section>"""
    report_installed_software = report_installed_software.encode('utf-8').decode('utf-8')
    return report_installed_software

# Startup Software Details
def startupSoftware_Report(show_verbose):
    report_StartupSoftware = ""
    print(yellow, end='')
    print('[!] Fetching Startup Software details')
    if show_verbose:
        st_time = time.localtime()
        print(log_col,end="")
        print('[v] Startup Software details fetching starting at '+str(time.strftime("%H:%M:%S", st_time)))
    try:
        report_StartupSoftware = list_allStartup_Software()
        # print (report_StartupSoftware)
        print(green, end='')
        print('[√] Startup Software details fetched successfully')
    except Exception as e:
        report_StartupSoftware = f"""</section>

        <div class="blurb"></div>

        <section>
            <div class="reportSection">
                <h2 class="reportSectionHeader">
                    Startup Software
                </h2>
                <div class="reportSectionBody">
                    <span style="font-size: 1.28em; color: #ff0000;">Error In Fetching Startup Softwares Details</span>
                </div>
            </div>
            </section>
        """

        print(red, end='')
        print('[×] Error in Fetching Startup Software details')
        if debug_mode:
            print('Debug : '+str(e))
    if show_verbose:
        ed_time = time.localtime()
        print(log_col,end="")
        print('[v] Startup Software details fetched at '+str(time.strftime("%H:%M:%S", ed_time)),end="")
        print(" [{:.0f}:{:02.0f}:{:02.0f}]".format(*map(int, str(datetime.datetime.fromtimestamp(time.mktime(ed_time)) - datetime.datetime.fromtimestamp(time.mktime(st_time))).split(":"))))
    return {'report_StartupSoftware': report_StartupSoftware}


# Installed software details
def installSoftware_Report(show_verbose):
    report_installedSoftware = ""
    print(yellow, end='')
    print('[!] Fetching Installed Software details')
    if show_verbose:
        st_time_IS = time.localtime()
        print(log_col,end="")
        print('[v] Installed Software details fetching starting at '+str(time.strftime("%H:%M:%S", st_time_IS)))
    try:
        report_installedSoftware = installed_Software()
        print(green, end='')
        print('[√] Installed Software details fetched successfully')
    except Exception as e:
        report_installedSoftware = f"""
        <div class="blurb"></div>
        <section>
            <div class="reportSection">
                <h2 class="reportSectionHeader">
                    Installed Software & Application
                </h2>
                <div class="reportSectionBody">
                    <span style="font-size: 1.28em; color: #ff0000;">Error In Fetching Installed Softwares Details</span>
                </div>
            </div>
            </section>
        """
        print(red, end='')
        print('[×] Error in Fetching Installed Software details')
        if debug_mode:
            print('Debug : '+str(e))
    if show_verbose:
        ed_time_IS = time.localtime()
        print(log_col,end="")
        print('[v] Installed Software details fetched at '+str(time.strftime("%H:%M:%S", ed_time_IS)),end="")
        print(" [{:.0f}:{:02.0f}:{:02.0f}]".format(*map(int, str(datetime.datetime.fromtimestamp(time.mktime(ed_time_IS)) - datetime.datetime.fromtimestamp(time.mktime(st_time_IS))).split(":"))))
    return {'report_installedSoftware': report_installedSoftware}


if __name__ == '__main__':
    print("This module cannot be run directly. Please import it.")