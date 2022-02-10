# -*- coding: utf_8 -*-
"""CLI archerysec-cli output format."""
from datetime import datetime

def print_tool_info(ver):
    """Tool info."""
    
    tool_str = 'Copyright (C) %s ArcherySec CLI v{} '.format(ver) % datetime.now().year
    return tool_str


def cli_output(version):
    """Format output printing."""
    tool = print_tool_info(version)
    buffer = []
    if outfile and buffer:
        buffer.insert(0, tool)
        outdata = '\n'.join(buffer)
        with open(outfile, 'w') as of:
            of.write(outdata)
    return buffer