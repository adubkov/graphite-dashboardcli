# Graphite Dashboard CLI tool
This tool allow manage graphite dashboards from command line.

Cerrently it supports:
* Show dashboard configuration in YAML format from local storage or remote Graphite
* Import\Export dashboards from\to Graphite
* Synchronize dashboards between multiple Graphite servers
* Delete dashboards from local storage or remote Graphite
* Keep dashboards in YAML format

## Install
You can install Graphite-Dashboard CLI tool with pip:
```bash
pip install graphite-dashboardcli
``` 

## Usage

```bash
$ graphite-dashboardcli COMMAND DASHBOARD_NAME ENDPOINT [DESTINATIONS...]

COMMAND:
    show  - Show content of dashboard
    copy  - Copy dashboard from source to destinations
    sync  - Sync dashboard between multiple Graphite servers
    delete - Delete dashboard
```

## Examples

Show content of specific dashboad:
```bash
# Show from local storage
$ graphite-dashboardcli show TestDashboard ./dashboards

# Show from remote Graphite
$ graphite-dashboardcli show TestDashboard http://graphite.local
```

Copy dashboard from\to:
```bash
# Copy from local storage to remote Graphite server
$ graphite-dashboardcli copy TestDashboard ./dashboards http://graphite.local

# Copy all dashboards from remote Graphite to local
$ graphite-dashboardcli copy '*' http://graphite.local ./dashboards

# Copy from one Graphite server to another
$ graphite-dashboardcli copy TestDashboard http://graphite1.local http://graphite2.local
```

Sync dashboards between graphite servers:
```bash
$ graphite-dashboardcli sync '*' http://graphite1.local http://graphite2.local http://graphite3.local
```

Delete dashboard:
```bash
$ graphite-dashboardcli delete 'TestDashboard' http://graphite1.local http://graphite2.local
```
