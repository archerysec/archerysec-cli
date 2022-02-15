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
import time

import docker


class ScannersRunner(object):
    def __init__(self, pwd, report_pwd):
        self.pwd = pwd
        self.report_pwd = report_pwd

    def bandit_scan(self):
        print("Scan Running")
        client = docker.from_env()
        d = client.containers.run(
            "archerysec/bandit:latest",
            volumes={
                self.pwd: {"bind": "/src", "mode": "rw"},
                self.report_pwd: {"bind": "/report", "mode": "rw"},
            },
            detach=True,
        )
        c_id = d.id
        container = client.containers.get(c_id)
        status = container.status
        while status == "running":
            time.sleep(5)
            container = client.containers.get(c_id)
            status = container.status
            # print(status)
        container.remove()
        print("Scan Completed")

    def dependency_check_scan(self, data):
        print("Scan Running")
        client = docker.from_env()
        d = client.containers.run(
            "archerysec/dependency-check:latest",
            volumes={
                self.pwd: {"bind": "/src", "mode": "rw"},
                self.report_pwd: {"bind": "/report", "mode": "rw"},
                data: {"bind": "/usr/share/dependency-check/data", "mode": "rw"},
            },
            command='--scan /src --format "ALL" --project "dependency-check scan: %s" --out /report' % self.pwd,
            detach=True,
        )
        c_id = d.id
        container = client.containers.get(c_id)
        status = container.status
        while status == "running":
            time.sleep(5)
            container = client.containers.get(c_id)
            status = container.status
            # print(status)
        container.remove()
        print("Scan Completed")

    def owasp_zap_baseline_scan(self, target):
        print("Scan Running")
        client = docker.from_env()
        d = client.containers.run(
            "archerysec/owasp-zap:latest",
            volumes={
                self.report_pwd: {"bind": "/zap/wrk"},
            },
            command='zap-baseline.py -t %s -x archerysec-owasp-zap-base-line-report.xml' % target,
            detach=True,

        )
        c_id = d.id
        container = client.containers.get(c_id)
        status = container.status
        while status == "running":
            time.sleep(5)
            container = client.containers.get(c_id)
            status = container.status
            # print(status)
        container.remove()
        print("Scan Completed")

    def owasp_zap_full_scan(self, target):
        print("Scan Running")
        client = docker.from_env()
        d = client.containers.run(
            "archerysec/owasp-zap:latest",
            volumes={
                self.report_pwd: {"bind": "/zap/wrk"},
            },
            command='zap-full-scan.py -t %s -x archerysec-owasp-zap-full-scan-report.xml' % target,
            detach=True,
        )
        c_id = d.id
        container = client.containers.get(c_id)
        status = container.status
        while status == "running":
            time.sleep(5)
            container = client.containers.get(c_id)
            status = container.status
            # print(status)
        container.remove()
        print("Scan Completed")

    def findsecbugs_scan(self):
        print("Scan Running")
        client = docker.from_env()
        d = client.containers.run(
            "archerysec/findsecbugs:latest",
            volumes={
                self.pwd: {"bind": "/src", "mode": "rw"},
                self.report_pwd: {"bind": "/report", "mode": "rw"},
            },
            detach=True,
        )
        c_id = d.id
        container = client.containers.get(c_id)
        status = container.status
        while status == "running":
            time.sleep(5)
            container = client.containers.get(c_id)
            status = container.status
            # print(status)
        container.remove()
        print("Scan Completed")
