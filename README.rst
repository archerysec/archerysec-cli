
Archery CLI
*******************

A commandline tool that wraps the Archerysec REST API for controlling Archery and executing quick, targeted scans.

- `For More details <http://docs.archerysec.com/>`__

Requirements
~~~~~~~~~~~~

- `Archery tool <https://github.com/archerysec/archerysec>`__
- Python 3.9

Quick Start
~~~~~~~~~~~~

Several quick start options are available:

- Install with pip: ``pip install archerysec-cli``
- Build locally: ``python setup.py build``
- `Download the latest release <https://github.com/target/webinspectapi/releases/latest/>`__


Output
~~~~~~~

::
        
                               _                      _____
             /\            | |                    / ____|
            /  \   _ __ ___| |__   ___ _ __ _   _| (___   ___  ___
           / /\ \ | '__/ __| '_ \ / _ \ '__| | | |\___ \ / _ \/ __|
          / ____ \| | | (__| | | |  __/ |  | |_| |____) |  __/ (__
         /_/    \_\_|  \___|_| |_|\___|_|   \__, |_____/ \___|\___|
                                             __/ |
                                            |___/
        
         Copyright (C) 2021 ArcherySec CLI v2.0.1
        
        Usage: cli.py [OPTIONS]
        
        Options:
          -h, --host TEXT        Provide ArcherySec End Point Address.
          -t, --token TEXT       Provide Auth token from ArcherySec.
          -p, --path TEXT        Report File input
          --file-type TEXT       File type
          --target TEXT          target name or url
          -s, --scanner TEXT     Select scanners ( zap_scan, burp_scan, arachni,
                                 acunetix, netsparker, webinspect,
                                 banditscan,dependencycheck,findbugs, checkmarx,
                                 clair, trivy, gitlabsca, gitlabsast,
                                 gitlabcontainerscan, npmaudit, nodejsscan,
                                 semgrepscan, tfsec, whitesource, inspec, dockle,
                                 nessus, openvas, nikto, twistlock, brakeman, )
        
          -th, --threshold TEXT  threshold type (ex. fail, pass)
          --project TEXT         Project ID
          --cicd_id TEXT         CICD Policies ID
          --upload               Upload Report
          --project-create       Create New Project
          --bandit               Run Bandit Scan
          --dependency-check     Run dependency-check Scan
          --project-name TEXT    Create New Project
          --project-disc TEXT    Create New Project
          --code_path TEXT       Path of the source code
          --report_path TEXT     Path of the Report
          --help                 Show this message and exit.



Example
~~~~~~~

::

        
        # Create Project:
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x --createproject --project_name="test_project" --project_disc="test project"
        
        
        # Upload ZAP Scan:
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/OWASP-ZAP-v2.7.0.xml --file-type=XML --target=ASFLKSF --scanner=zap_scan --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload Burp Scan:
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/Burp_Report.xml --file-type=XML --target=ASFLKSF --scanner=burp_scan --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload arachni Scan:
        
        
        $ archerysec-cli  -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/Arachni_v1.3.xml --file-type=XML --target=ASFLKSF --scanner=arachni --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload acunetix Scan:
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/Acunetix_report_sample.xml --file-type=XML --target=ASFLKSF --scanner=acunetix --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload netsparker Scan:
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/Netsparker_report.xml --file-type=XML --target=ASFLKSF --scanner=netsparker --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload webinspect scan:
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/webinspect.xml --file-type=XML --target=ASFLKSF --scanner=webinspect --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload banditscan scan
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/banditscan.json --file-type=JSON --target=ASFLKSF --scanner=banditscan --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload dependencycheck scan
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/dependencycheck.xml --file-type=XML --target=ASFLKSF --scanner=dependencycheck --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload findbugs scan
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/findbugs.xml --file-type=XML --target=ASFLKSF --scanner=findbugs --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload checkmarx scan
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/checkmarx.xml --file-type=XML --target=ASFLKSF --scanner=checkmarx --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload clair scan
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/clair.json --file-type=JSON --target=ASFLKSF --scanner=clair --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload trivy scan
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/trivy.json --file-type=JSON --target=ASFLKSF --scanner=trivy --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload Git Lab SCA scan
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/gitlabsca.json --file-type=JSON --target=ASFLKSF --scanner=gitlabsca --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload Git Lab SAST scan
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/gitlabsast.json --file-type=JSON --target=ASFLKSF --scanner=gitlabsast --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload Git Lab Container scan
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/gitlabcontainerscan.json --file-type=JSON --target=ASFLKSF --scanner=gitlabcontainerscan --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload npmaudit scan
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/npmaudit.json --file-type=JSON --target=ASFLKSF --scanner=npmaudit --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload nodejsscan scan
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/nodejsscan.json --file-type=JSON --target=ASFLKSF --scanner=nodejsscan --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload netsparker scan
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/semgrepscan.json --file-type=JSON --target=ASFLKSF --scanner=netsparker --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload tfsec scan
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/tfsec.json --file-type=JSON --target=ASFLKSF --scanner=tfsec --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload whitesource scan
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/whitesource.xml --file-type=XML --target=ASFLKSF --scanner=whitesource --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload inspec scan
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/inspec.json --file-type=JSON --target=ASFLKSF --scanner=inspec --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload dockle scan
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/dockle.json --file-type=JSON --target=ASFLKSF --scanner=dockle --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload nessus scan
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/nessus.xml --file-type=XML --target=ASFLKSF --scanner=nessus --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload openvas scan
        
        
        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/openvas.xml --file-type=XML --target=ASFLKSF --scanner=openvas --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload twistlock scan

        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/twistlock.json --file-type=JSON --target=ASFLKSF --scanner=twistlock --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        
        
        # Upload brakeman scan

        $ archerysec-cli -h http://127.0.0.1:8000 -t VpVSD99bX25yW27f-yv8q562U9ObZfbWnBLVkjfRjQ-FR52p4GlhjpYuCJwY56_x -p /report/sample/brakeman.json --file-type=JSON --target=ASFLKSF --scanner=brakeman --project=eaf6f89e-56ee-4ef7-8257-07b7136c9e31 --upload
        

Bugs and Feature Requests
~~~~~~~~~~~~~~~~~~~~~~~~~

- `If you Found bug or have a feature request? Please open a new issue <https://github.com/archerysec/archerysec/issues>`__