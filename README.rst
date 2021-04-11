
Archery CLI
*******************

A commandline tool that wraps the Archerysec REST API for controlling Archery and executing quick, targeted scans.

- `For More details <http://docs.archerysec.com/>`__

Requirements
~~~~~~~~~~~~

- `Archery tool <https://github.com/archerysec/archerysec>`__
- Python 3.9

Installation
~~~~~~~~~~~~

- `pip install archerysec-cli`__

To use Archery CLI, you need to set the port Archery runs on (defaults to 8000) and the path to the folder in which Archery is installed.
You can Use Archery installation instruction from [Archery DOC](https://docs.archerysec.info/getting-started/Docker-install/)


Example
~~~~~~~

::


    Create Project:

```
$archerysec-cli -s http://127.0.0.1:8000 -u admin -p admin@123 --createproject --project_name=test_project --project_disc="test project"  --project_start=2018-01-11 --project_end=2018-01-11 --project_owner=anand
```

Launch ZAP Scan:

```
$archerysec-cli -s http://127.0.0.1:8000 -u admin -p admin@123 --zapscan --target_url=http://demo.testfire.net --project_id=aa6730d4-d3c8-40ab-9ac1-27592afbdcb3
```


Bugs and Feature Requests
~~~~~~~~~~~~~~~~~~~~~~~~~

- `If you Found bug or have a feature request? Please open a new issue <https://github.com/archerysec/archerysec/issues>`__