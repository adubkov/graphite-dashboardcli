# Graphite Dashboard CLI tool
This tool allow manage graphite dashboards from command line.

Cerrently it supports:
* Show dashboard configuration from local storage or remote Graphite
* Import\Export dashboards from\to Graphite
* Synchronize dashboards between multiple Graphite servers
* Delete dashboards from local storage or remote Graphite

## Install
You can install Graphite-Dashboard CLI tool with pip:
```bash
pip install graphite-dashboard
``` 

## Usage

```bash
$ graphite-dashboard COMMAND DASHBOARD_NAME ENDPOINT [DESTINATIONS...]

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
$ graphite-dashboard show TestDashboard ./dashboards

# Show from remote Graphite
$ graphite-dashboard show TestDashboard http://graphite.local
```

Copy dashboard from\to:
```bash
# Copy from local storage to remote Graphite server
$ graphite-dashboard copy TestDashboard ./dashboards http://graphite.local

# Copy all dashboards from remote Graphite to local
$ graphite-dashboard copy '*' http://graphite.local ./dashboards

# Copy from one Graphite server to another
$ graphite-dashboard copy TestDashboard http://graphite1.local http://graphite2.local
```

Sync dashboards between graphite servers:
```bash
$ graphite-dashboard sync '*' http://graphite1.local http://graphite2.local http://graphite3.local
```

Delete dashboard:
```bash
$ graphite-dashboard delete 'TestDashboard' http://graphite1.local http://graphite2.local
```
