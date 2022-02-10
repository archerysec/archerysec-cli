#!/usr/bin/env python

"""
======================= START OF LICENSE NOTICE =======================
  Copyright (C) 2021 ArcherySec. All Rights Reserved
  NO WARRANTY. THE PRODUCT IS PROVIDED BY DEVELOPER "AS IS" AND ANY
  EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL DEVELOPER BE LIABLE FOR
  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
  GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
  IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
  OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THE PRODUCT, EVEN
  IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
======================== END OF LICENSE NOTICE ========================
  Primary Author: Anand Tiwari
"""
import os
import sys

import click
import json
import yaml
from yaml import safe_load

from archerysec_cli import __version__
from archerysec_cli.scanners.scanners import ScannersRunner
from archerysec_cli.util import check
from archerysec_cli.util.api import API
from archerysec_cli.formatters import (
    cli,
    json
)

data = """

                    _                      _____           
     /\            | |                    / ____|          
    /  \   _ __ ___| |__   ___ _ __ _   _| (___   ___  ___ 
   / /\ \ | '__/ __| '_ \ / _ \ '__| | | |\___ \ / _ \/ __|
  / ____ \| | | (__| | | |  __/ |  | |_| |____) |  __/ (__ 
 /_/    \_\_|  \___|_| |_|\___|_|   \__, |_____/ \___|\___|
                                     __/ |                 
                                    |___/                  
"""
print(data)
print(cli.print_tool_info(__version__))



@click.command()
@click.option("--host", "-h", "host", help="Provide ArcherySec End Point Address.")
@click.option("--token", "-t", "token", help="Provide Auth token from ArcherySec.")
@click.option('--path', '-p', "path", help='Report File input')
@click.option('--file-type', "filetype", help='File type')
@click.option('--target', "target", help='target name or url')
@click.option('--scanner', '-s', "scanner", help='Select scanners '
                                                 '( zap_scan, '
                                                 'burp_scan, '
                                                 'arachni, '
                                                 'acunetix, '
                                                 'netsparker, '
                                                 'webinspect, '
                                                 'banditscan,'
                                                 'dependencycheck,'
                                                 'findbugs, '
                                                 'checkmarx, '
                                                 'clair, '
                                                 'trivy, '
                                                 'gitlabsca, '
                                                 'gitlabsast, '
                                                 'gitlabcontainerscan, '
                                                 'npmaudit, '
                                                 'nodejsscan, '
                                                 'semgrepscan, '
                                                 'tfsec, '
                                                 'whitesource, '
                                                 'inspec, '
                                                 'dockle, '
                                                 'nessus, '
                                                 'openvas, '
                                                 'nikto, '
                                                 'twistlock, '
                                                 'brakeman, '

                                                 ')')
@click.option('--threshold', '-th', "threshold", help='threshold type (ex. fail, pass)')
@click.option('--project', "projectid", help='Project ID')
@click.option('--cicd_id', "cicd_id", help='CICD Policies ID')
@click.option('--upload', "upload", help="Upload Report", is_flag=True)
@click.option('--createproject', "projectcreate", help="Create New Project", is_flag=True)
@click.option('--bandit', "bandit", help="Run Bandit Scan", is_flag=True)
@click.option('--zap-base-line-scan', "zapbaselinescan", help="Run ZAP Base Line Scan", is_flag=True)
@click.option('--zap-full-scan', "zapfullscan", help="Run ZAP Full Scan", is_flag=True)
@click.option('--findsecbugs-scan', "findsecbugs", help="Run FindSecBugs Scan", is_flag=True)
@click.option('--dependency-check', "dependencycheck", help="Run dependency-check Scan", is_flag=True)
@click.option('--project_name', "projectname", help="Create New Project")
@click.option('--project_disc', "projectdisc", help="Create New Project")
@click.option('--code_path', "code_path", help="Path of the source code")
@click.option('--report_path', "reportpath", help="Path of the Report")

def scan_action(host, token, filetype, target, scanner, projectid, path, upload, projectcreate, projectname,
                projectdisc, bandit, reportpath, code_path, cicd_id, dependencycheck, threshold,
                zapbaselinescan, zapfullscan, findsecbugs):
    if upload:
        upload_report(
            host=host,
            token=token,
            file_type=filetype,
            target=target,
            scanner=scanner,
            project=projectid,
            report_path=path,
            threshold_status="",
            threshold_high="",
            threshold_medium="",
            threshold_low="",
            threshold=threshold,
        )
    if projectcreate:
        archerysec = API(
            host=host, project_id='', scanner='', target='', token=token
        )
        print(projectname)
        project_data = archerysec.create_project(project_name=projectname, project_disc=projectdisc)
        print(project_data.data_json())

    if bandit:
        bandit_scan(
            host=host,
            token=token,
            project=projectid,
            bandit='bandit',
            cicd_id=cicd_id,
            reportpath=reportpath
        )
    if dependencycheck:
        dependencycheck_scan(
            host=host,
            token=token,
            project=projectid,
            dependencycheck='dependencycheck',
            cicd_id=cicd_id,
            reportpath=reportpath
        )

    if zapbaselinescan:
        zap_base_line_scan(
            host=host,
            token=token,
            project=projectid,
            cicd_id=cicd_id,
            reportpath=reportpath,
            zap_scan='zap_scan',
        )

    if zapfullscan:
        zap_full_scan(
            host=host,
            token=token,
            project=projectid,
            zap_scan='zap_scan',
            cicd_id=cicd_id,
            reportpath=reportpath
        )

    if findsecbugs:
        findsecbugs_scan(
            host=host,
            token=token,
            project=projectid,
            findsecbugs='findsecbugs',
            cicd_id=cicd_id,
            reportpath=reportpath
        )

def get_cicd_policies(host, token, project, scanner, target, cicd_id):
    archerysec = API(
        host=host, project_id=project, scanner=scanner, target=target, token=token
    )
    cicd_policies = archerysec.get_cicd_policies(cicd_id=cicd_id).data
    return cicd_policies


def scan_data_parser(scan_data,
                     threshold_status,
                     threshold,
                     threshold_high,
                     threshold_medium,
                     threshold_low):
    try:
        total = scan_data["result"]["total_vul"]
        high = scan_data["result"]["total_high"]
        medium = scan_data["result"]["total_medium"]
        low = scan_data["result"]["total_low"]
        print("===================================================+")
        print(
            "Scan Result: Total: %s High: %s Medium: %s Low: %s"
            % (total, high, medium, low)
        )
        print("===================================================+")
        if threshold_status == "fail":
            if threshold_high == 0:
                threshold_high = high
            elif threshold_medium == 0:
                threshold_medium = medium
            elif threshold_low == 0:
                threshold_low = low
            if threshold == 'high':
                if int(threshold_high) < int(high):
                    print("Failed Due to High:", high)
                    sys.exit(1)
            elif threshold == 'medium':
                if int(threshold_medium) < int(medium):
                    print("Failed Due to Medium:", medium)
                    print("threshold_medium", threshold_medium)
                    print("medium", medium)
                    sys.exit(1)
            elif threshold == 'medium':
                if int(threshold_low) < int(low):
                    print("Failed Due to Low:", low)
                    sys.exit(1)
            else:
                sys.exit(0)
    except Exception as e:
        print(e)


def upload_report(
        host,
        token,
        file_type,
        target,
        scanner,
        project,
        report_path,
        threshold_status,
        threshold_high,
        threshold_medium,
        threshold,
        threshold_low):
    """upload report into archerysec portal"""
    archerysec = API(
        host=host, project_id=project, scanner=scanner, target=target, token=token
    )

    if file_type == "JSON":
        scan_data = archerysec.json_upload(file=report_path)
        scan_data_parser(scan_data, threshold_status, threshold, threshold_high, threshold_medium, threshold_low)
    elif file_type == "XML":
        scan_data = archerysec.xml_upload(file=report_path)
        scan_data_parser(scan_data, threshold_status, threshold, threshold_high, threshold_medium, threshold_low)
    else:
        print("File Type Not Support")


def bandit_scan(host,
                token,
                project,
                bandit,
                cicd_id,
                reportpath
                ):
    cicd_policies = get_cicd_policies(host, token, project, scanner=bandit, target='', cicd_id=cicd_id)
    code_path = cicd_policies['target']
    report_path = reportpath
    scanner = ScannersRunner(pwd=code_path, report_pwd=report_path)
    scanner.bandit_scan()

    target = cicd_policies['target_name']
    threshold = cicd_policies['threshold']
    threshold_high = ''
    threshold_medium = ''
    threshold_low = ''
    if threshold == 'high':
        threshold_high = cicd_policies['threshold_count']
    elif threshold == 'medium':
        threshold_medium = cicd_policies['threshold_count']
    elif threshold == 'low':
        threshold_low = cicd_policies['threshold_count']

    upload_report(
        host=host,
        token=token,
        file_type="JSON",
        target=target,
        scanner="banditscan",
        project=project,
        report_path=report_path + "/banditResult.json",
        threshold_status='fail',
        threshold=threshold,
        threshold_high=threshold_high,
        threshold_medium=threshold_medium,
        threshold_low=threshold_low,
    )


def dependencycheck_scan(host,
                         token,
                         project,
                         dependencycheck,
                         cicd_id,
                         reportpath):
    data_path = 'OWASP-Dependency-Check'
    cicd_policies = get_cicd_policies(host, token, project, scanner=dependencycheck, target='', cicd_id=cicd_id)
    code_path = cicd_policies['target']
    report_path = reportpath
    scanner = ScannersRunner(pwd=code_path, report_pwd=report_path)
    scanner.dependency_check_scan(data=data_path)

    target = cicd_policies['target_name']
    threshold = cicd_policies['threshold']
    threshold_high = ''
    threshold_medium = ''
    threshold_low = ''
    if threshold == 'high':
        threshold_high = cicd_policies['threshold_count']
    elif threshold == 'medium':
        threshold_medium = cicd_policies['threshold_count']
    elif threshold == 'low':
        threshold_low = cicd_policies['threshold_count']

    upload_report(
        host=host,
        token=token,
        file_type="JSON",
        target=target,
        scanner="dependencycheck",
        project=project,
        report_path=report_path + "/dependency-check-report.xml",
        threshold_status='fail',
        threshold=threshold,
        threshold_high=threshold_high,
        threshold_medium=threshold_medium,
        threshold_low=threshold_low,
    )


def zap_base_line_scan(host,
                       token,
                       project,
                       zap_scan,
                       cicd_id,
                       reportpath
                       ):
    cicd_policies = get_cicd_policies(host, token, project, scanner=zap_scan, target='', cicd_id=cicd_id)
    target = cicd_policies['target']
    report_path = reportpath
    scanner = ScannersRunner(pwd=target, report_pwd=report_path)
    scanner.owasp_zap_baseline_scan(target=target)

    target = cicd_policies['target_name']
    threshold = cicd_policies['threshold']
    threshold_high = ''
    threshold_medium = ''
    threshold_low = ''
    if threshold == 'high':
        threshold_high = cicd_policies['threshold_count']
    elif threshold == 'medium':
        threshold_medium = cicd_policies['threshold_count']
    elif threshold == 'low':
        threshold_low = cicd_policies['threshold_count']

    upload_report(
        host=host,
        token=token,
        file_type="XML",
        target=target,
        scanner="zap_scan",
        project=project,
        report_path=report_path + "/archerysec-owasp-zap-base-line-report.xml",
        threshold_status='fail',
        threshold=threshold,
        threshold_high=threshold_high,
        threshold_medium=threshold_medium,
        threshold_low=threshold_low,
    )


def zap_full_scan(host,
                  token,
                  project,
                  zap_scan,
                  cicd_id,
                  reportpath
                  ):
    cicd_policies = get_cicd_policies(host, token, project, scanner=zap_scan, target='', cicd_id=cicd_id)
    target = cicd_policies['target']
    report_path = reportpath
    scanner = ScannersRunner(pwd=target, report_pwd=report_path)
    scanner.owasp_zap_full_scan(target=target)

    target = cicd_policies['target_name']
    threshold = cicd_policies['threshold']
    threshold_high = ''
    threshold_medium = ''
    threshold_low = ''
    if threshold == 'high':
        threshold_high = cicd_policies['threshold_count']
    elif threshold == 'medium':
        threshold_medium = cicd_policies['threshold_count']
    elif threshold == 'low':
        threshold_low = cicd_policies['threshold_count']

    upload_report(
        host=host,
        token=token,
        file_type="XML",
        target=target,
        scanner="zap_scan",
        project=project,
        report_path=report_path + "/archerysec-owasp-zap-full-scan-report.xml",
        threshold_status='fail',
        threshold=threshold,
        threshold_high=threshold_high,
        threshold_medium=threshold_medium,
        threshold_low=threshold_low,
    )


def findsecbugs_scan(host,
                     token,
                     project,
                     findsecbugs,
                     cicd_id,
                     reportpath
                     ):
    cicd_policies = get_cicd_policies(host, token, project, scanner=findsecbugs, target='', cicd_id=cicd_id)
    code_path = cicd_policies['target']
    report_path = reportpath
    scanner = ScannersRunner(pwd=code_path, report_pwd=report_path)
    scanner.findsecbugs_scan()

    target = cicd_policies['target_name']
    threshold = cicd_policies['threshold']
    threshold_high = ''
    threshold_medium = ''
    threshold_low = ''
    if threshold == 'high':
        threshold_high = cicd_policies['threshold_count']
    elif threshold == 'medium':
        threshold_medium = cicd_policies['threshold_count']
    elif threshold == 'low':
        threshold_low = cicd_policies['threshold_count']

    upload_report(
        host=host,
        token=token,
        file_type="XML",
        target=target,
        scanner="findbugs",
        project=project,
        report_path=report_path + "/findsecbugs-report.xml",
        threshold_status='fail',
        threshold=threshold,
        threshold_high=threshold_high,
        threshold_medium=threshold_medium,
        threshold_low=threshold_low,
    )


def main():
    scan_action()


if __name__ == "__main__":
    main()
