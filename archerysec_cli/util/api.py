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

import json

import requests


def all_headers(auth_token):
    headers = {
        "Content-Type": "application/json",
        "x-api-key": auth_token,
    }
    return headers


class API(object):
    def __init__(self, host, project_id, scanner, target, token):
        """
        :param host:
        :param project_id:
        :param scanner:
        :param target:
        :param token:
        """

        self.host = host
        self.project_id = project_id
        self.scanner = scanner
        self.target = target
        self.token = token

    def json_upload(self, file):
        """

        :param file:
        :return:
        """
        headers = {"x-api-key": self.token}
        f = (open(file, "rb")).read()
        files = {
            "filename": (None, f),
            "project_id": (None, self.project_id),
            "scanner": (None, self.scanner),
            "scan_url": (None, self.target),
        }
        url = self.host + "/api/v1/uploadscan/"
        send_request = requests.post(url, files=files, headers=headers)
        return send_request.json()

    def xml_upload(self, file):
        """

        :param file:
        :return:
        """

        headers = {"x-api-key": self.token}
        f = (open(file, "rb")).read()
        files = {
            "filename": (None, f),
            "project_id": (None, self.project_id),
            "scanner": (None, self.scanner),
            'scan_url': (None, self.target)
        }
        url = self.host + "/api/v1/uploadscan/"
        send_request = requests.post(url, files=files, headers=headers)
        return send_request.json()

    def create_project(self, project_name, project_disc):
        """

        :param file:
        :return:
        """
        url = "/api/v1/project-create/"
        headers = all_headers(auth_token=self.token)
        data = {
            "project_name": project_name,
            "project_disc": project_disc,
        }
        data = json.dumps(data)
        return self._request('POST', url, params='format=json', headers=headers, data=data)

    def get_cicd_policies(self, cicd_id):
        """

        :param cicd_id:
        :return:
        """
        url = "/api/v1/get-cicd-policies/%s/" % (cicd_id)
        headers = all_headers(auth_token=self.token)
        return self._request('GET', url, params='format=json', headers=headers)

    def _request(self, method, url, params=None, headers=None, data=None):
        """Common handler for all the HTTP requests."""
        if not params:
            params = {}

        # set default headers
        if not headers:
            headers = {"Content-Type": "application/json"}
        try:
            response = requests.request(
                method=method,
                url=self.host + url,
                params=params,
                headers=headers,
                data=data,
            )

            try:
                response.raise_for_status()

                response_code = response.status_code
                success = True if response_code // 100 == 2 else False
                if response.text:
                    try:
                        data = response.json()
                    except ValueError:
                        data = response.content
                else:
                    data = ""

                return Response(success=success, response_code=response_code, data=data)
            except ValueError as e:
                return Response(
                    success=False,
                    message="JSON response could not be decoded {}.".format(e),
                )
            except requests.exceptions.HTTPError as e:
                if response.status_code == 400:
                    return Response(
                        success=False, response_code=400, message="Bad Request"
                    )
                else:
                    return Response(
                        message="There was an error while handling the request. {}".format(
                            response.content
                        ),
                        success=False,
                    )
        except Exception as e:
            return Response(success=False, message="Eerror is %s" % e)


class Response(object):
    """Container for all Archery REST API response, even errors."""

    def __init__(self, success, message="OK", response_code=-1, data=None):
        self.message = message
        self.success = success
        self.response_code = response_code
        self.data = data

    def __str__(self):
        if self.data:
            return str(self.data)
        else:
            return self.message

    def data_json(self, pintu=False):
        """Returns the data as a valid JSON String."""
        if pintu:
            return json.dumps(
                self.data, sort_keys=True, indent=4, separators=(",", ": ")
            )
        else:
            return json.dumps(self.data)
