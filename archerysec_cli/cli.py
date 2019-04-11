from optparse import OptionParser
from optparse import OptionGroup
from pyArchery import api
import requests

data = """

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

"""
print(data)


def main():
    """
    Archery REST-JSON API main function
    """
    parser = OptionParser()

    # Authenticate into Archery Application
    group = OptionGroup(parser, "Archery Authentication",
                        "Authenticate into Archery REST API")
    group.add_option("-s", "--server",
                     help="Archery API server host address",
                     action="store")
    group.add_option("-u", "--username",
                     help="Archery authentication username",
                     action="store")
    group.add_option("-p", "--password",
                     help="Archery authentication password",
                     action="store")
    group.add_option("--target_url",
                     help="Target URL's",
                     action="store")
    group.add_option("--scan_id",
                     help="Target Scan ID",
                     action="store")
    group.add_option("--target_ip",
                     help="Target IP's",
                     action="store")
    group.add_option("--project_id",
                     help="Project ID",
                     action="store")

    parser.add_option_group(group)

    # Token
    group = OptionGroup(parser, "Get the Archery REST API token", )
    group.add_option("-t", "--token",
                     help="Print archery REST API Auth token",
                     action="store_true")
    parser.add_option_group(group)

    # Archery Projects
    group = OptionGroup(parser, "Archery Projects", "Perform action on Projects modules")
    group.add_option("--projectlist",
                     help="Print project list",
                     action="store_true")
    group.add_option("--createproject",
                     help="Create new project with project name",
                     action="store_true")
    group.add_option("--project_name",
                     help="Project Name",
                     action="store")
    group.add_option("--project_disc",
                     help="Project Description",
                     action="store")
    group.add_option("--project_start",
                     help="Project start date Ex. 2018-01-11",
                     action="store")
    group.add_option("--project_end",
                     help="Project End date Ex. 2018-01-11",
                     action="store")
    group.add_option("--project_owner",
                     help="Project Owner name",
                     action="store")
    parser.add_option_group(group)

    # Archery ZAP Scans
    group = OptionGroup(parser, "ZAP Scans",
                        "ZAP Scans module to perform ZAP Scans")

    group.add_option("--zapscanlist",
                     help="List all ZAP Scans",
                     action="store_true")

    # Launch ZAP Scan
    group.add_option("--zapscan",
                     help="Launch ZAP Scan",
                     action="store_true")

    # Get ZAP Scan status
    group.add_option("--zapscanstatus",
                     help="Get ZAP Scan Status"
                          " (Ex. python archery_cli.py -s "
                          "http://127.0.0.1:8000 -u admin -p admin@123A --zapscanstatus"
                          " --scan_id=4ea6852b-bbf2-4171-9e98-4d798731e87a)",
                     action="store_true"
                     )

    # Get ZAP Scan results
    group.add_option("--zapscanresult",
                     help="Get ZAP Scan result"
                          " (Ex. python archery_cli.py -s "
                          "http://127.0.0.1:8000 -u admin -p admin@123A --zapscanresult"
                          " --scan_id=4ea6852b-bbf2-4171-9e98-4d798731e87a)",
                     action="store_true"
                     )
    parser.add_option_group(group)

    # Launch Arachni Scan
    group.add_option("--arachni",
                     help="Launch Arachni Scan",
                     action="store_true")

    # Get OpenVAS Scan Results
    group = OptionGroup(parser, "OpenVAS Scanner",
                        "OpenVAS Scans module to perform OpenVAS Scan"
                        )

    group.add_option("--openvaslist",
                     help="List all OpenVAS Scans",
                     action="store_true")

    group.add_option("--openvasscan",
                     help="Launch OpenVAS Scans",
                     action="store_true")

    group.add_option("--openvas_result",
                     help="Get OpenVAS Scan result"
                          " (Ex. python archery_cli.py -s "
                          "http://127.0.0.1:8000 -u admin -p admin@123A --openvas_result"
                          " --scan_id=4ea6852b-bbf2-4171-9e98-4d798731e87a)",
                     action="store_true"
                     )

    parser.add_option_group(group)

    group = OptionGroup(parser, "Upload Scanner Reports",
                        "Upload multiple scanners reports"
                        )

    group.add_option("--upload",
                     help="Upload scans report",
                     action="store_true")
    group.add_option("--file",
                     help="Input JSON or XML file",
                     action="store")
    group.add_option("--TARGET",
                     help="Scan URL or IP",
                     action="store")
    group.add_option("--file_type",
                     help="File type (JSON, XML)",
                     action="store")
    group.add_option("--scanner",
                     help="Select scanners [ zap_scan, "
                          "burp_scan, "
                          "arachni, "
                          "netsparker, "
                          "webinspect, "
                          "banditscan]",
                     action="store")

    parser.add_option_group(group)

    (args, _) = parser.parse_args()

    archery = api.ArcheryAPI(args.server)

    # REST API Authentication
    authenticate = archery.archery_auth(args.username, args.password)

    # Get the authentication Token
    auth_token = authenticate.data

    if args.token:
        try:
            for key, value in auth_token.items():
                token = value
                print(token)
        except:
            print("Error !!!!")
            print ("Please check Username and Password")
    elif args.projectlist:
        try:
            for key, value in auth_token.items():
                token = value
                project = archery.list_project(auth=token)
                print("Project List :-")
                print(project.data_json())
        except:
            print("Error !!!!")
            print("Please check Username and Password")
    elif args.createproject:
        try:
            for key, value in auth_token.items():
                token = value
                create_proj = archery.create_project(auth=token,
                                                     project_name=args.project_name,
                                                     project_disc=args.project_disc,
                                                     project_start=args.project_start,
                                                     project_end=args.project_end,
                                                     project_owner=args.project_owner)
                print(create_proj.data_json())
        except:
            print("Error !!!!")
            print("Please check Username and Password")
    elif args.zapscanlist:
        for key, value in auth_token.items():
            token = value
            all_web_scans = archery.web_scans(auth=token)
            print(all_web_scans.data_json())

    elif args.zapscanresult:
        for key, value in auth_token.items():
            token = value
            web_scan_result = archery.webscan_result(
                auth=token,
                scan_id=args.scan_id,
            )
            print(web_scan_result.data_json())

    elif args.zapscanstatus:
        for key, value in auth_token.items():
            token = value
            zap_scan_status = archery.zap_scan_status(
                auth=token,
                scan_id=args.scan_id,
            )
            print(zap_scan_status.data_json())

    elif args.zapscan:
        for key, value in auth_token.items():
            token = value
            web_scan_create = archery.create_webscan(
                auth=token,
                scan_url=args.target_url,
                project_id=args.project_id,
                scanner='zap_scan'
            )
            print(web_scan_create.data_json())

    elif args.arachni:
        for key, value in auth_token.items():
            token = value
            web_scan_create = archery.create_webscan(
                auth=token,
                scan_url=args.target_url,
                project_id=args.project_id,
                scanner='arachni'
            )
            print(web_scan_create.data_json())

    elif args.openvaslist:
        for key, value in auth_token.items():
            token = value
            network_scans = archery.network_scan(
                auth=token,
            )

            print(network_scans.data_json())

    elif args.openvasscan:
        for key, value in auth_token.items():
            token = value
            create_network_scan = archery.create_newtworkscan(
                auth=token,
                scan_ip=args.target_ip,
                project_id=args.project_id
            )
            print(create_network_scan.data_json())

    elif args.openvas_result:
        for key, value in auth_token.items():
            token = value
            network_result = archery.networkscan_result(
                auth=token,
                scan_id=args.scan_id
            )

            print(network_result)

    elif args.upload:
        for key, value in auth_token.items():
            token = value
            headers = {'Authorization': 'JWT ' + token}
            if args.file_type == "JSON":
                f = (open(args.file, 'rb')).read()
                files = {'filename': (None, f), 'project_id': (None, args.project_id),
                         'scanner': (None, args.scanner), 'scan_url': (None, args.TARGET)}
                url = args.server + '/api/uploadscan/'
                send_request = requests.post(url, files=files, headers=headers)
                print(send_request.text)
            elif args.file_type == "XML":
                files = {'filename': (None, args.file), 'project_id': (None, args.project_id),
                         'scanner': (None, args.scanner), 'scan_url': (None, args.TARGET)}
                url = args.server + '/api/uploadscan/'
                send_request = requests.post(url, files=files, headers=headers)
                print(send_request.text)
    else:
        parser.print_help()
        print("")
        print("Example to get auth token: archerysec-cli -s http://127.0.0.1:8000 -u admin -p admin@123A -t")


if __name__ == "__main__":
    main()
