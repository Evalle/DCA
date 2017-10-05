# Docker Certified Associate exam Preparation Guide

This guide is intended to be a point of knowledge to everyone who wants to pass [Docker Certified Associate Exam](https://blog.docker.com/2017/09/introducing-docker-global-professional-certification-program/). The main idea is to provide the right answer/link to every "question" in every domain. Feel free to add useful links below. 

## Content

### Domain 1: Orchestration (25% of exam)
- Complete the setup of a swarm mode cluster, with managers and worker nodes
- State the differences between running a container vs running a service
- Demonstrate steps to lock a swarm cluster
- Extend the instructions to run individual containers into running services under swarm
- Interpret the output of "docker inspect" commands
- Convert an application deployment into a stack file using a YAML compose file with
"docker stack deploy"
- Manipulate a running stack of services
- Increase # of replicas
- Add networks, publish ports
- Mount volumes
- Illustrate running a replicated vs global service
- Identify the steps needed to troubleshoot a service not deploying
- Apply node labels to demonstrate placement of tasks
- Sketch how a Dockerized application communicates with legacy systems
- Paraphrase the importance of quorum in a swarm cluster
- Demonstrate the usage of templates with "docker service create"

### Domain 2: Image Creation, Management, and Registry (20% of exam)
- Describe Dockerfile options [add, copy, volumes, expose, entrypoint, etc)
- Show the main parts of a Dockerfile
- Give examples on how to create an efficient image via a Dockerfile
- Use CLI commands such as list, delete, prune, rmi, etc to manage images
- Inspect images and report specific attributes using filter and format
- Demonstrate tagging an image
- Utilize a registry to store an image
- Display layers of a Docker image
- Apply a file to create a Docker image
- Modify an image to a single layer
- Describe how image layers work
- Deploy a registry (not architect)
- Configure a registry
- Log into a registry
- Utilize search in a registry
- Tag an image
- Push an image to a registry
- Sign an image in a registry
- Pull an image from a registry
- Describe how image deletion works
- Delete an image from a registry

### Domain 3: Installation and Configuration (15% of exam)
- Demonstrate the ability to upgrade the Docker engine
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
- Configure Docker to use external DNS
- Use Docker to load balance HTTP/HTTPs traffic to an application (Configure L7 load
balancing with Docker EE)
- Understand and describe the types of traffic that flow between the Docker engine,
registry, and UCP controllers
- Deploy a service on a Docker overlay network
- Describe the difference between "host" and "ingress" port publishing mode

