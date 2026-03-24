# Domain 4: Networking (15% of exam)

[← Domain 3: Installation and Configuration](domain3-installation.md) | [Back to Study Guide Index](README.md)

- [Describe the Container Network Model and how it interfaces with the Docker engine and network and IPAM drivers](https://docs.docker.com/network/)
- [Describe the different types and use cases for the built-in network drivers](https://www.docker.com/blog/understanding-docker-networking-drivers-use-cases/)
- [Describe the types of traffic that flow between the Docker engine, registry and UCP controllers](https://docs.mirantis.com/msr/2.9/ref-arch/networks.html)
- [Describe and demonstrate how to create a Docker bridge network for developers to use for their containers](https://docs.docker.com/engine/network/drivers/bridge/)
- [Describe and demonstrate how to publish a port so that an application is accessible externally](https://github.com/wsargent/docker-cheat-sheet#exposing-ports)
- [Identify which IP and port a container is externally accessible on](https://docs.docker.com/engine/reference/commandline/port/#examples)
- Compare and contrast "host" and "ingress" publishing modes ([Host](https://docs.docker.com/engine/swarm/services/#publish-a-services-ports-directly-on-the-swarm-node), [Ingress](https://docs.docker.com/engine/swarm/ingress/))
- [Describe and demonstrate how to configure Docker to use external DNS](https://gist.github.com/Evalle/7b21e0357c137875a03480428a7d6bf6)
- [Describe and demonstrate how to use Docker to load balance HTTP/HTTPs traffic to an application (Configure L7 load balancing with Docker EE)](https://www.mirantis.com/blog/enhanced-layer-7-routing-for-swarm-in-docker-enterprise-edition-beta)
- [Describe and demonstrate how to deploy a service on a Docker overlay network](https://docs.docker.com/network/overlay/)
- Describe and demonstrate how to troubleshoot container and engine logs to resolve connectivity issues between containers:
  - [how to troubleshoot docker container logs](https://docs.docker.com/engine/reference/commandline/logs/)
  - [how to troubleshoot docker enginee logs](https://docs.docker.com/config/daemon/logs/)
- (Since Study Guide 1.5) [Describe how to route traffic to Kubernetes pods using ClusterIP and NodePort services](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types)
- (Since Study Guide 1.5) [Describe the Kubernetes' container network model](https://kubernetes.io/docs/concepts/cluster-administration/networking/)

---

[← Domain 3: Installation and Configuration](domain3-installation.md) | [Back to Study Guide Index](README.md) | [Next: Domain 5 - Security →](domain5-security.md)
