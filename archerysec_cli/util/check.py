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


class ReadConfig(object):
    def __init__(self, data):
        self.data = data

    def get_project_id(self):
        """

        :return:
        """
        project_id = self.data["project"]["projectId"]
        return project_id

    def get_scanner(self):
        """

        :return:
        """
        get_scanner = self.data["project"]["scanner"]
        return get_scanner

    def get_threshold(self, severity=None):
        """

        :return:
        """
        if severity == "high":
            get_threshold = self.data["project"]["threshold"]["high"]
        elif severity == "medium":
            get_threshold = self.data["project"]["threshold"]["medium"]
        elif severity == "low":
            get_threshold = self.data["project"]["threshold"]["low"]
        elif severity == "action":
            get_threshold = self.data["project"]["threshold"]["action"]
        else:
            get_threshold = "severity not found"
        return get_threshold

    def get_action(self):
        """

        :return:
        """
        get_action = self.data["project"]["action"]
        return get_action

    def get_code_path(self):
        """

        :return:
        """
        get_code_path = self.data["project"]["codePath"]
        return get_code_path

    def get_report_path(self):
        """

        :return:
        """
        get_report_path = self.data["project"]["reportStorePath"]
        return get_report_path

    def get_config(self, value):
        """[summary]

        :return:
        """
        if value == "exclude":
            get_config = self.data["project"]["config"]["exclude"]
        elif value == "include":
            get_config = self.data["project"]["config"]["include"]
        elif value == "exclude_dirs":
            get_config = self.data["project"]["config"]["exclude_dirs"]
        else:
            get_config = "config not found"
        return get_config
