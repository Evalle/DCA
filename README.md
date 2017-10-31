# Docker Certified Associate Exam Preparation Guide

This guide is intended to be a point of knowledge to everyone who wants to pass [Docker Certified Associate Exam](https://blog.docker.com/2017/09/introducing-docker-global-professional-certification-program/). The main idea is to provide the right answer/link to every "question" in every domain. Feel free to add useful links below. 

## Table of Contents:
1. [Orchestration](https://github.com/Evalle/DCA/blob/master/README.md#domain-1-orchestration-25-of-exam)
2. [Image Creation, Management, and Registry](https://github.com/Evalle/DCA/blob/master/README.md#domain-2-image-creation-management-and-registry-20-of-exam)
3. [Installation and Configuration](https://github.com/Evalle/DCA/blob/master/README.md#domain-3-installation-and-configuration-15-of-exam)
4. [Networking](https://github.com/Evalle/DCA/blob/master/README.md#domain-4-networking-15-of-exam)
5. [Security](https://github.com/Evalle/DCA/blob/master/README.md#domain-5-security-15-of-exam)
6. [Storage and Volumes](https://github.com/Evalle/DCA/blob/master/README.md#domain-6-storage-and-volumes-10-of-exam)
7. [Links](https://github.com/evalle/dca#links)

## Content

### Domain 1: Orchestration (25% of exam)
- [Complete the setup of a swarm mode cluster, with managers and worker nodes](https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/)
- [State the differences between running a container vs running a service](https://stackoverflow.com/a/43408904)
- [Demonstrate steps to lock a swarm cluster](https://docs.docker.com/engine/swarm/swarm_manager_locking/)
- Extend the instructions to run individual containers into running services under swarm
- [Interpret the output of "docker inspect" commands](https://docs.docker.com/engine/swarm/swarm-tutorial/inspect-service/)
- Convert an application deployment into a stack file using a YAML compose file with
"docker stack deploy"
- Manipulate a running stack of services
- [Increase number of replicas](https://docs.docker.com/engine/reference/commandline/service_scale/)
- Add networks, publish ports
- [Mount volumes](https://docs.docker.com/engine/admin/volumes/volumes/)
- Illustrate running a replicated vs global service
- Identify the steps needed to troubleshoot a service not deploying
- Apply node labels to demonstrate placement of tasks
- Sketch how a Dockerized application communicates with legacy systems
- Paraphrase the importance of quorum in a swarm cluster
- Demonstrate the usage of templates with "docker service create"

### Domain 2: Image Creation, Management, and Registry (20% of exam)
- [Describe Dockerfile options(add, copy, volumes, expose, entrypoint, etc)](https://docs.docker.com/engine/reference/builder/#from)
- Show the main parts of a Dockerfile
- [Give examples on how to create an efficient image via a Dockerfile](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)
- [Use CLI commands such as list, delete, prune, rmi, etc to manage images](https://docs.docker.com/engine/reference/commandline/image/#usage)
- Inspect images and report specific attributes using filter and format
- [Demonstrate tagging an image](https://docs.docker.com/engine/reference/commandline/tag/)
- Utilize a registry to store an image
- Display layers of a Docker image
- Apply a file to create a Docker image
- Modify an image to a single layer
- Describe how image layers work
- Deploy a registry (not architect)
- Configure a registry
- Log into a registry
- Utilize search in a registry
- [Tag an image](https://docs.docker.com/engine/reference/commandline/tag/)
- Push an image to a registry
- Sign an image in a registry
- Pull an image from a registry
- Describe how image deletion works
- Delete an image from a registry

### Domain 3: Installation and Configuration (15% of exam)
- [Demonstrate the ability to upgrade the Docker engine](https://askubuntu.com/questions/472412/how-do-i-upgrade-docker)
- Complete setup of repo, select a storage driver, and complete installation of Docker
engine on multiple platforms
- Configure logging drivers (splunk, journald, etc)
- Setup swarm, configure managers, add nodes, and setup backup schedule
- Create and manager user and teams
- Interpret errors to troubleshoot installation issues without assistance
- Outline the sizing requirements prior to installation
- Understand namespaces, cgroups, and configuration of certificates
- Use certificate-based client-server authentication to ensure a Docker daemon has the
rights to access images on a registry
- Consistently repeat steps to deploy Docker engine, UCP, and DTR on AWS and on
premises in an HA config
- Complete configuration of backups for UCP and DTR
- Configure the Docker daemon to start on boot

### Domain 4: Networking (15% of exam)
- Create a Docker bridge network for a developer to use for their containers
- Troubleshoot container and engine logs to understand a connectivity issue between
containers
- Publish a port so that an application is accessible externally
- Identify which IP and port a container is externally accessible on
- Describe the different types and use cases for the built-in network drivers
- Understand the Container Network Model and how it interfaces with the Docker engine
and network and IPAM drivers
- [Configure Docker to use external DNS](https://gist.github.com/Evalle/7b21e0357c137875a03480428a7d6bf6)
- Use Docker to load balance HTTP/HTTPs traffic to an application (Configure L7 load
balancing with Docker EE)
- Understand and describe the types of traffic that flow between the Docker engine,
registry, and UCP controllers
- Deploy a service on a Docker overlay network
- Describe the difference between "host" and "ingress" port publishing mode

### Domain 5: Security (15% of exam)
- Describe the process of signing an image
- Demonstrate that an image passes a security scan
- Enable Docker Content Trust
- Configure RBAC in UCP
- Integrate UCP with LDAP/AD
- Demonstrate creation of UCP client bundles
- Describe default engine security
- Describe swarm default security
- Describe MTLS

### Domain 6: Storage and Volumes (10% of exam)
- State which graph driver should be used on which OS
- Demonstrate how to configure devicemapper
- Compare object storage to block storage, and explain which one is preferable when
available
- Summarize how an application is composed of layers and where those layers reside on
the filesystem
- Describe how volumes are used with Docker for persistent storage
- Identify the steps you would take to clean up unused images on a filesystem, also on
DTR
- Demonstrate how storage can be used across cluster nodes
- Identity roles
- Describe the difference between UCP workers and managers
- Describe process to use external certificates with UCP and DTR

## Links

- [Basic info](https://success.docker.com/Certification) about Exam
- Study guide (pdf) can be found [here](https://success.docker.com/@api/deki/files/613/DCA_Study_Guide_v1.0.pdf?revision=1)
