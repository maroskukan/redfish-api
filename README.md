# Redfish API

- [Redfish API](#redfish-api)
  - [Introduction](#introduction)
  - [Documentation](#documentation)
  - [Architecture](#architecture)
  - [Environment](#environment)
    - [Local environment](#local-environment)
    - [Remote environment](#remote-environment)

## Introduction

Redfish initiative started in 2014 as collaboration between Intel, Dell, HPE, and Emerson. The initiative eventually formed Distributed Management Task Force (DMTF) standard body.

Redfish provides a standard specification for protocols, data model and behaviors. It is replacement for legacy IPMI which is no longer developed.


## Documentation

[Redfish Developer Hub](https://redfish.dmtf.org/)
[Hello Redfish, Goodbye IPMI](https://www.thomas-krenn.com/de/tkmag/wp-content/uploads/2016/03/Werner_Fischer_-_Hello_Redfish__Goodbye_IPMI.pdf)
[HPE iLO RESTful API](https://developer.hpe.com/platform/ilo-restful-api/home/)
[HPE iLO REST API Docs](https://hewlettpackard.github.io/ilo-rest-api-docs/)


## Architecture

Redfish secures communication between client and server using HTTPS. It provides a REST API interface and works with JSON data structures. It provides ODATA which is a schema-backed data model. It was designed to be easily implemented on existing server firmware.


## Environment

### Local environment

In order to start quickly experimenting with Redfish API implementation you can leverage [Redfish Mockup Server](https://github.com/DMTF/Redfish-Mockup-Server).

Using [Docker](https://www.docker.com/) it is very easy to start a Mockup server container.

```bash
docker run --rm -p 8000:8000 dmtf/redfish-mockup-server:latest
Redfish Mockup Server, version 1.1.5
Hostname: 0.0.0.0
Port: 8000
Mockup directory path specified: public-rackmount1
Response time: 0 seconds
Serving Mockup in absolute path: /usr/src/app/public-rackmount1
Serving Redfish mockup on port: 8000
running Server...
```

Try sample curl request to root.

```json
curl -s localhost:8000/redfish/v1/Systems/437XR1138R2 | jq -r '.MemorySummary'
{
  "MemoryMirroring": "None",
  "Status": {
    "Health": "OK",
    "HealthRollup": "OK",
    "State": "Enabled"
  },
  "TotalSystemMemoryGiB": 96,
  "TotalSystemPersistentMemoryGiB": 0
}
```

### Remote environment

If using local development environment is not convenient or you just want to explore the Redfish data model you have several options available.

You can use [online mockups](https://redfish.dmtf.org/redfish/v1) provided by DMTF working group. You can select from a wide variety of sample configurations such as **Simple Rack-mounted Server**, **Blade System** and more.

If you are looking some vendor specific implementation, for example on HPE Proliant servers you can use the [iLO RESTful API Explorer](https://ilorestfulapiexplorer.ext.hpe.com/) where JSON Explorer and Object model are available.