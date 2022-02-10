# -*- coding: utf_8 -*-
"""JSON output format."""
import json


def json_output(version):
    """JSON Output."""
    scan_results['archerysec_version'] = version
    json_out = json.dumps(
        scan_results,
        sort_keys=True,
        indent=2,
        separators=(',', ': '))
    print(json_out)
    return json_out
