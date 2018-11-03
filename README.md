# Archery CLI

A commandline tool that wraps the Archerysec REST API for controlling Archery and executing quick, targeted scans.


## Installation

To install the latest release from PyPI, you can run the following command:

```
pip install archerysec-cli
```
To install the latest development version of Archerysec CLI, you can run the following:

```
$ git clone https://github.com/archerysec/archerysec-cli.git
$ cd archerysec-cli
$ pip install -r requirements.txt

```
## Usage

To use Archery CLI, you need to set the port Archery runs on (defaults to 8000) and the path to the folder in which Archery is installed. 
You can Use Archery installation instruction from [Archery DOC](https://docs.archerysec.info/getting-started/Docker-install/)

Archery CLI can then be used with the following commands:
```
(env) Anand:archerysec-cli anand$ python archerysec.py


                   _
    /\            | |
   /  \   _ __ ___| |__   ___ _ __ _   _
  / /\ \ | '__/ __| '_ \ / _ \ '__| | | |
 / ____ \| | | (__| | | |  __/ |  | |_| |
/_/    \_\_|  \___|_| |_|\___|_|   \__, |
                                    __/ |
                                   |___/
 Copyright (C) 2018 ArcherySec
 Open Source Vulnerability Assessment and Management.


Usage: archerysec.py [options]

Options:
  -h, --help            show this help message and exit

  Archery Authentication:
    Authenticate into Archery REST API

    -s SERVER, --server=SERVER
                        Archery API server host address
    -u USERNAME, --username=USERNAME
                        Archery authentication username
    -p PASSWORD, --password=PASSWORD
                        Archery authentication password
    --target_url=TARGET_URL
                        Target URL's
    --scan_id=SCAN_ID   Target URL's
    --target_ip=TARGET_IP
                        Target IP's
    --project_id=PROJECT_ID
                        Project ID

  Get the Archery REST API token:
    -t, --token         Print archery REST API Auth token

  Archery Projects:
    Perform action on Projects modules

    --projectlist       Print project list
    --createproject     Create new project with project name
    --project_name=PROJECT_NAME
                        Project Name
    --project_disc=PROJECT_DISC
                        Project Description
    --project_start=PROJECT_START
                        Project start date Ex. 2018-01-11
    --project_end=PROJECT_END
                        Project End date Ex. 2018-01-11
    --project_owner=PROJECT_OWNER
                        Project Owner name

  ZAP Scans:
    ZAP Scans module to perform ZAP Scans

    --zapscanlist       List all ZAP Scans
    --zapscan           Launch ZAP Scan
    --zapscanresult     Get ZAP Scan result (Ex. python archery_cli.py -s
                        http://127.0.0.1:8000 -u admin -p admin@123A
                        --zapscanresult --scan_id=4ea6852b-
                        bbf2-4171-9e98-4d798731e87a)

  OpenVAS Scanner:
    OpenVAS Scans module to perform OpenVAS Scan

    --openvaslist       List all OpenVAS Scans
    --openvasscan       Launch OpenVAS Scans
    --openvas_result    Get OpenVAS Scan result (Ex. python archery_cli.py -s
                        http://127.0.0.1:8000 -u admin -p admin@123A
                        --openvas_result --scan_id=4ea6852b-
                        bbf2-4171-9e98-4d798731e87a)

  Upload Scanner Reports:
    Upload multiple scanners reports

    --upload            Upload scans report
    --file=FILE         Input JSON or XML file
    --TARGET=TARGET     Scan URL or IP
    --scanner=SCANNER   Select scanners [ zap_scan, burp_scan, arachni,
                        netsparker, webinspect, banditscan]

Example to get auth token: archerysec-cli -s http://127.0.0.1:8000 -u admin -p admin@123A -t
```
