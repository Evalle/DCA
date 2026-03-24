# Domain 5: Security (15% of exam)

[← Domain 4: Networking](domain4-networking.md) | [Back to Study Guide Index](README.md)

- (Since Study Guide 1.5) Describe [security administration](https://docs.docker.com/engine/security/) and [tasks](https://docs.docker.com/engine/swarm/how-swarm-mode-works/services/#tasks-and-scheduling)
- [Describe the process of signing an image](https://docs.docker.com/engine/security/trust/content_trust/#push-trusted-content)
- [Describe default engine security](https://docs.docker.com/engine/security/security/)
- [Describe swarm default security](https://docs.docker.com/engine/swarm/how-swarm-mode-works/pki/)
- [Describe MTLS](https://diogomonica.com/2017/01/11/hitless-tls-certificate-rotation-in-go/)
- [Identity roles](https://docs.mirantis.com/mke/3.6/ref-arch/rbac.html#rbac)
- Describe the difference between UCP workers and managers:
  - [workers](https://docs.mirantis.com/mke/3.4/ref-arch/worker-nodes.html)
  - [managers](https://docs.mirantis.com/mke/3.4/ref-arch/manager-nodes.html)
- Describe process to use external certificates with:
  1. UCP
  - [from cli](https://docs.mirantis.com/mke/3.6/ops/administer-cluster/use-your-own-tls-certificates.html)
  - [from GUI](https://docs.mirantis.com/docker-enterprise/v3.0/dockeree-products/ucp/admin/configure/use-your-own-tls-certificates.html)
  - [print the public certificates](https://docs.mirantis.com/mke/3.3/cli-ref/mke-cli-dump-certs.html)
  2. [**DTR** is now Mirantis Secure Registry or **MSR**](https://docs.mirantis.com/containers/v3.1/dockeree-products/msr/msr-configure/use-your-own-tls-certificates.html)
- [Describe and demonstrate that an image passes a security scan](https://docs.mirantis.com/msr/2.9/ops/manage-images/scan-images-for-vulnerabilities.html)
- [Describe and demonstrate how to enable Docker Content Trust.](https://docs.docker.com/engine/security/trust/content_trust/)
- [Describe and demonstrate how to configure RBAC with UCP](https://docs.mirantis.com/containers/v3.0/dockeree-products/mke/admin/configure/configure-kube-rbac.html)
- [Describe and demonstrate how to integrate UCP with LDAP/AD](https://docs.mirantis.com/containers/v3.0/dockeree-products/mke/admin/configure/integrate-with-LDAP-directory.html)
- [Describe and demonstrate how to create UCP client bundles](https://docs.mirantis.com/mke/3.4/ops/access-cluster/client-bundle/configure-client-bundle.html)

---

[← Domain 4: Networking](domain4-networking.md) | [Back to Study Guide Index](README.md) | [Next: Domain 6 - Storage and Volumes →](domain6-storage.md)
