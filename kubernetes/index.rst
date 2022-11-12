Kubernetes
==========

.. todo::

   * `Learning Kubernetes Controllers <https://maelvls.dev/learning-kubernetes-controllers/>`_

A Kubernetes cluster contains several software components. Every node in the
cluster runs an agent called the kubelet to maintain membership in the cluster
and accept work from it, a container engine, and kube-proxy to enable network
communication with containers running on other nodes.

The components that maintain the state of the cluster and make decisions about
resource allocations are collectively referred to as the control plane — these
include a distributed key-value store called etcd, a scheduler that assigns
work to cluster nodes, and one or more controller processes that react to
changes in the state of the cluster and trigger any actions needed to make the
actual state match the desired state. Users and cluster nodes interact with the
control plane through the Kubernetes API server. To effect changes, users set
the desired state of the cluster through the API server, while the kubelet
reports the actual state of each cluster node to the controller processes.

Kubernetes runs containers inside an abstraction called a pod, which can
contain one or more containers, although running containers for more than one
service in a pod is discouraged. Instead, a pod will generally have a single
main container that provides a service, and possibly one or more "sidecar"
containers that collect metrics or logs from the service running in the main
container. All of the containers in a pod will be scheduled together on the
same machine, and will share a network namespace — containers running within
the same pod can communicate with each other over the loopback interface. Each
pod receives its own unique IP address within the cluster. Containers running
in different pods can communicate with each other using their cluster IP
addresses.

About Docker https://lwn.net/Articles/902049/

Docker has transformed the way many people develop and deploy software. It
wasn't the first implementation of containers on Linux, but Docker's ideas
about how containers should be structured and managed were different from its
predecessors. Those ideas matured into industry standards, and an ecosystem of
software has grown around them.

Anatomy of a container

A container is somewhat like a lightweight virtual machine; it shares a kernel
with the host, but in most other ways it appears to be an independent machine
to the software running inside of it.

The Linux kernel itself has no concept of containers; instead, they are created
by using a combination of several kernel features:

* Bind mounts and overlayfs may be used to construct the root filesystem of the
  container.

* Control groups may be used to partition CPU, memory, and I/O resources for
  the host kernel.

* Namespaces are used to create an isolated view of the system for processes
  running inside the container.

Linux's namespaces are the key feature that allow the creation of containers.

Linux supports namespaces for multiple different aspects of the system,
including user namespaces for separate views of user and group IDs, PID
namespaces for distinct sets of process IDs, network namespaces for distinct
sets of network interfaces, and several others. When a container is started, a
runtime creates the appropriate control groups, namespaces, and filesystem
mounts for the container; then it launches a process inside the environment it
has created.

There is some level of disagreement about what that process should be. Some
prefer to start an init process like systemd and run a full Linux system inside
the container. This is referred to as a "system container"; it was the most
common type of container before Docker. System containers continue to be
supported by software like LXC and OpenVZ.

Docker's developers had a different idea. Instead of running an entire system
inside a container, Docker says that each container should only run a single
application. This style of container is known as an "application container." An
application container is started using a container image, which bundles the
application together with its dependencies and just enough of a Linux root
filesystem to run it.

A container image generally does not include an init system, and may not even
include a package manager —container images are usually replaced with updated
versions rather than updated in place. An image for a statically-compiled
application may be as minimal as a single binary and a handful of support files
in /etc.

Application containers usually don't have a persistent root filesystem;
instead, overlayfs is used to create a temporary layer on top of the container
image. This is thrown away when the container is stopped. Any persistent data
outside of the container image is grafted on to the container's filesystem via
a bind mount to another location on the host.

The OCI ecosystem

These days, when people talk about containers, they are likely to be talking
about the style of application containers popularized by Docker. In fact,
unless otherwise specified, they are probably talking about the specific
container image format, run-time environment, and registry API implemented by
Docker's software. Those have all been standardized by the Open Container
Initiative (OCI), which is an industry body that was formed in 2015 by Docker
and the Linux Foundation. Docker refactored its software into a number of
smaller components; some of those components, along with their specifications,
were placed under the care of the OCI. The software and specifications
published by the OCI formed the seed for what is now a robust ecosystem of
container-related software.

OCI image specification defines a format for container images that consists
of a JSON configuration (containing environment variables, the path to execute,
and so on) and a series of tarballs called "layers". The contents of each layer
are stacked on top of each other, in series, to construct the root filesystem
for the container image. Layers can be shared between images; if a server is
running several containers that refer to the same layer, they can potentially
share the same copy of that layer. Docker provides minimal images for several
popular Linux distributions that can be used as the base layer for application
containers.

OCI Distribution specification defines an HTTP API for pushing and pulling
container images to and from a server; servers that implement this API are
called container registries. Docker maintains a large public registry called
Docker Hub as well as a reference implementation that can be self-hosted.

Other implementations of the specification include Red Hat's Quay and VMware's
Harbor, as well as hosted offerings from Amazon, GitHub, GitLab, and Google.

A program that implements the OCI runtime specification is responsible for
everything pertaining to actually running a container. It sets up any necessary
mounts, control groups, and kernel namespaces, executes processes inside the
container, and tears down any container-related resources once all the
processes inside of it have exited. The reference implementation of the runtime
specification is runc, which was created by Docker for the OCI.

There are a number of other OCI runtimes to choose from. For example, crun
offers an OCI runtime written in C that has the goal of being faster and more
lightweight than runc, which, like most of the rest of the OCI ecosystem, is
written in Go. Google's gVisor includes runsc, which provides greater isolation
from the host by running applications on top of a user-mode kernel. Amazon's
Firecracker is a minimal hypervisor written in Rust that can use KVM to give
each container its own virtual machine; Intel's Kata Containers works similarly
but supports multiple hypervisors (including Firecracker.)

A container engine is a program that ties these three specifications together.
It implements the client side of the distribution specification to retrieve
container images from registries, interprets the images it has retrieved
according to the image specification, and launches containers using a program
that implements the runtime specification. A container engine provides tools
and/or APIs for users to manage container images, processes, and storage.

Kubernetes is a container orchestrator, capable of scheduling and running
containers across hundreds or even thousands of servers. Kubernetes does not
implement any of the OCI specifications itself. It needs to be used in
combination with a container engine, which manages containers on behalf of
Kubernetes. The interface that it uses to communicate with container engines is
called the Container Runtime Interface (CRI).

Docker

Docker is the original OCI container engine. It consists of two main
user-visible components: a command-line-interface (CLI) client named docker,
and a server. The server is named dockerd in Docker's own packages, but the
repository was renamed moby.

dockerd provides an HTTP API; it usually listens on a Unix socket named
/var/run/docker.sock, but can be made to listen on a TCP socket as well. The
docker command is merely a client to this API; the server is responsible for
downloading images and starting container processes. The client supports
starting containers in the foreground, so that running a container at the
command-line behaves similarly to running any other program, but this is only a
simulation. In this mode, the container processes are still started by the
server, and input and output are streamed over the API socket; when the process
exits, the server reports that to the client, and then the client sets its own
exit status to match.

This design does not play well with systemd or other process supervision tools,
because the CLI never has any child processes of its own. Running the docker
CLI under a process supervisor only results in supervising the CLI process.
This has a variety of consequences for users of these tools. For example, any
attempt to limit a container's memory usage by running the CLI as a systemd
service will fail; the limits will only apply to the CLI and its non-existent
children. In addition, attempts to terminate a client process may not result in
terminating all of the processes in the container.

Failure to limit access to Docker's socket can be a significant security
hazard. By default dockerd runs as root. Anyone who is able to connect to the
Docker socket has complete access to the API. Since the API allows things like
running a container as a specific UID and binding arbitrary filesystem
locations, it is trivial for someone with access to the socket to become root
on the host. Support for running in rootless mode was added in 2019 and
stabilized in 2020, but is still not the default mode of operation.

Docker can be used by Kubernetes to run containers, but it doesn't directly
support the CRI specification. Originally, Kubernetes included a component
called dockershim that provided a bridge between the CRI and the Docker API,
but it was deprecated in 2020. The code was spun out of the Kubernetes
repository and is now maintained separately as cri-dockerd.

containerd & nerdctl

Docker refactored its software into independent components in 2015; containerd
is one of the fruits of that effort. In 2017, Docker donated containerd to the
Cloud Native Computing Foundation (CNCF), which stewards the development of
Kubernetes and other tools. It is still included in Docker, but it can also be
used as a standalone container engine, or with Kubernetes via an included CRI
plugin. The architecture of containerd is highly modular. This flexibility
helps it to serve as a proving ground for experimental features. Plugins may
provide support for different ways of storing container images and additional
image formats, for example.

Without any additional plugins, containerd is effectively a subset of Docker;
its core features map closely to the OCI specifications. Tools designed to work
with Docker's API cannot be used with containerd. Instead, it provides an API
based on Google's gRPC. Unfortunately, concerned system administrators looking
for access control won't find it here; despite being incompatible with Docker's
API, containerd's API appears to carry all of the same security implications.

The documentation for containerd notes that it follows a smart client model (as
opposed to Docker's "dumb client"). Among other differences, this means that
containerd does not communicate with container registries; instead, (smart)
clients are required to download any images they need themselves. Despite the
difference in client models, containerd still has a process model similar to
that of Docker; container processes are forked from the containerd process. In
general, without additional software, containerd doesn't do anything
differently from Docker, it just does less.

When containerd is bundled with Docker, dockerd serves as the smart client,
accepting Docker API calls from its own dumb client and doing any additional
work needed before calling the containerd API; when used with Kubernetes, these
things are handled by the CRI plugin. Other than that, containerd didn't really
have its own client until relatively recently. It includes a bare-bones CLI
called ctr, but this is only intended for debugging purposes.

This changed in December 2020 with the release of nerdctl. Since its release,
running containerd on its own has become much more practical; nerdctl features
a user interface designed to be compatible with the Docker CLI and provides
much of the functionality Docker users would find missing from a standalone
containerd installation. Users who don't need compatibility with the Docker API
might find themselves quite happy with containerd and nertdctl.

Podman

Podman is an alternative to Docker sponsored by Red Hat, which aims to be a
drop-in replacement for Docker. Like Docker and containerd, it is written in Go
and released under the Apache 2.0 License, but it is not a fork; it is an
independent reimplementation. Red Hat's sponsorship of Podman is likely to be
at least partially motivated by the difficulties it encountered during its
efforts to make Docker's software interoperate with systemd.

On a superficial level, Podman appears nearly identical to Docker. It can use
the same container images, and talk to the same registries. The podman CLI is a
clone of docker, with the intention that users migrating from Docker can alias
docker to podman and mostly continue with their lives as if nothing had
changed.

Originally, Podman provided an API based on the varlink protocol. This meant
that while Podman was compatible with Docker on a CLI level, tools that used
the Docker API directly could not be used with Podman. In version 3.0, the
varlink API was scrapped in favor of an HTTP API, which aims to be compatible
with the one provided by Docker while also adding some Podman-specific
endpoints. This new API is maturing rapidly, but users of tools designed for
Docker would be well-advised to test for compatibility before committing to
switch to Podman.

As it is largely a copy of Docker's API, Podman's API doesn't feature any sort
of access control, but Podman has some architectural differences that may make
that less important. Podman gained support for running in rootless mode early
on in its development. In this mode, containers can be created without root or
any other special privileges, aside from that small bit of help from newuidmap
and newgidmap. Unlike Docker, when Podman is invoked by a non-root user,
rootless mode is used by default.

Users of Podman can also dodge security concerns about its API socket by simply
disabling it. Though its interface is largely identical to the Docker CLI,
podman is no mere API client. It creates containers for itself without any help
from a daemon. As a result, Podman plays nicely with tools like systemd; using
podman run with a process supervisor works as expected, because the processes
inside the container are children of podman run. The developers of Podman
encourage people to use it in this way by a command to generate systemd units
for Podman containers.

Aside from its process model, Podman caters to systemd users in other ways.
While running an init system such as systemd inside of a container is
antithetical to the Docker philosophy of one application per container, Podman
goes out of its way to make it easy. If the program to run specified by the
container is an init system, Podman will automatically mount all the kernel
filesystems needed for systemd to function. It also supports reporting the
status of containers to systemd via sd_notify(), or handing the notification
socket off to the application inside of the container for it to use directly.

Podman also has some features designed to appeal to Kubernetes users. Like
Kubernetes, it supports the notion of a "pod", which is a group of containers
that share a common network namespace. It can run containers using Kubernetes
configuration files and also generate Kubernetes configurations. However,
unlike Docker and containerd, there is no way for Podman to be used by
Kubernetes to run containers. This is a deliberate omission. Instead of adding
CRI support to Podman, which is a general-purpose container engine, Red Hat
chose to sponsor the development of a more specialized alternative in the form
of CRI-O.

CRI-O
-----

CRI-O is based on many of the same underpinnings as Podman. So the relationship
between CRI-O and Podman could be said to be similar to the one between
containerd and Docker; CRI-O delivers much of the same technology as Podman,
with fewer frills. This analogy doesn't stretch far, though. Unlike containerd
and Docker, CRI-O and Podman are completely separate projects; one is not
embedded by the other.

As might be suggested by its name, CRI-O implements the Kubernetes CRI. In
fact, that's all that it implements; CRI-O is built specifically and only for
use with Kubernetes. It is developed in lockstep with the Kubernetes release
cycle, and anything that is not required by the CRI is explicitly declared to
be out of scope. CRI-O cannot be used without Kubernetes and includes no CLI of
its own; based on the stated goals of the project, any attempt to make CRI-O
suitable for standalone use would likely be viewed as an unwelcome distraction
by its developers.

Like Podman, the development of CRI-O was initially sponsored by Red Hat; like
containerd, it was later donated to the CNCF in 2019. Although they are now
both under the aegis of the same organization, the narrow focus of CRI-O may
make it more appealing to Kubernetes administrators than containerd. The
developers of CRI-O are free to make decisions solely on the basis of
maximizing the benefit to users of Kubernetes, whereas the developers of
containerd and other container engines have many other types of users and uses
cases to consider.

Conclusion

These are just a few of the most popular container engines; other projects like
Apptainer and Pouch cater to different ecological niches. There are also a
number of tools available for creating and manipulating container images, like
Buildah, Buildpacks, skopeo, and umoci. Docker deserves a great deal of credit
for the Open Container Initiative; the standards and the software that have
resulted from this effort have provided the foundation for a wide array of
projects. The ecosystem is robust; should one project shut down, there are
multiple alternatives ready and available to take its place. As a result, the
future of this technology is no longer tied to one particular company or
project; the style of containers that Docker pioneered seems likely to be with
us for a long time to come.


Container Orchestration Landscape
---------------------------------

Docker and other container engines can greatly simplify many aspects of
deploying a server-side application, but numerous applications consist of more
than one container. Managing a group of containers only gets harder as
additional applications and services are deployed; this has led to the
development of a class of tools called container orchestrators. The best-known
of these by far is Kubernetes; the history of container orchestration can be
divided into what came before it and what came after.

The convenience offered by containers comes with some trade-offs; someone who
adheres strictly to Docker's idea that each service should have its own
container will end up running a large number of them. Even a simple web
interface to a database might require running separate containers for the
database server and the application; it might also include a separate container
for a web server to handle serving static files, a proxy server to terminate
SSL/TLS connections, a key-value store to serve as a cache, or even a second
application container to handle background jobs and scheduled tasks.

An administrator who is responsible for several such applications will quickly
find themselves wishing for a tool to make their job easier; this is where
container orchestrators step in. A container orchestrator is a tool that can
manage a group of multiple containers as a single unit. Instead of operating on
a single server, orchestrators allow combining multiple servers into a cluster,
and automatically distribute container workloads among the cluster nodes.

Docker Compose and Swarm
------------------------

Docker Compose is not quite an orchestrator, but it was Docker's first attempt
to create a tool to make it easier to manage applications that are made out of
several containers. It consumes a YAML-formatted file, which is almost always
named docker-compose.yml. Compose reads this file and uses the Docker API to
create the resources that it declares; Compose also adds labels to all of the
resources, so that they can be managed as a group after they are created. In
effect, it is an alternative to the Docker command-line interface (CLI) that
operates on groups of containers. Three types of resources can be defined in a

Compose file:

* services contains declarations of containers to be launched. Each entry in
  services is equivalent to a docker run command.
* networks declares networks that can be attached to the containers defined in
  the Compose file. Each entry in networks is equivalent to a docker network
  create command.
* volumes defines named volumes that can be attached to the containers. In
  Docker parlance, a volume is persistent storage that is mounted into the
  container. Named volumes are managed by the Docker daemon. Each entry in
  volumes is equivalent to a docker volume create command.


Networks and volumes can be directly connected to networks and filesystems on
the host that Docker is running on, or they can be provided by a plugin.
Network plugins allow things like connecting containers to VPNs; a volume
plugin might allow storing a volume on an NFS server or an object storage
service.

Compose provides a much more convenient way to manage an application that
consists of multiple containers, but, at least in its original incarnation, it
only worked with a single host; all of the containers that it created were run
on the same machine. To extend its reach across multiple hosts, Docker
introduced Swarm mode in 2016. This is actually the second product from Docker
to bear the name "Swarm" — a product from 2014 implemented a completely
different approach to running containers across multiple hosts, but it is no
longer maintained. It was replaced by SwarmKit, which provides the
underpinnings of the current version of Docker Swarm.

Swarm mode is included in Docker; no additional software is required. Creating
a cluster is a simple matter of running docker swarm init on an initial node,
and then docker swarm join on each additional node to be added. Swarm clusters
contain two types of nodes. Manager nodes provide an API to launch containers
on the cluster, and communicate with each other using a protocol based on the
Raft Consensus Algorithm in order to synchronize the state of the cluster
across all managers. Worker nodes do the actual work of running containers. It
is unclear how large these clusters can be; Docker's documentation says that a
cluster should have no more than 7 manager nodes but does not specify a limit
on the number of worker nodes. Bridging container networks across nodes is
built-in, but sharing storage between nodes is not; third-party volume plugins
need to be used to provide shared persistent storage across nodes.

Services are deployed on a swarm using Compose files. Swarm extended the
Compose format by adding a deploy key to each service that specifies how many
instances of the service should be running and which nodes they should run on.
Unfortunately, this led to a divergence between Compose and Swarm, which caused
some confusion because options like CPU and memory quotas needed to be
specified in different ways depending on which tool was being used. During this
period of divergence, a file intended for Swarm was referred to as a "stack
file" instead of a Compose file in an attempt to disambiguate the two;
thankfully, these differences appear to have been smoothed over in the current
versions of Swarm and Compose, and any references to a stack file being
distinct from a Compose file seem to have largely been scoured from the
Internet. The Compose format now has an open specification and its own GitHub
organization providing reference implementations.

There is some level of uncertainty about the future of Swarm. It once formed
the backbone of a service called Docker Cloud, but the service was suddenly
shut down in 2018. It was also touted as a key feature of Docker's Enterprise
Edition, but that product has since been sold to another company and is now
marketed as Mirantis Kubernetes Engine. Meanwhile, recent versions of Compose
have gained the ability to deploy containers to services hosted by Amazon and
Microsoft. There has been no deprecation announcement, but there also hasn't
been any announcement of any other type in recent memory; searching for the
word "Swarm" on Docker's website only turns up passing mentions.

Kubernetes

Kubernetes (sometimes known as k8s) is a project inspired by an internal Google
tool called Borg. Kubernetes manages resources and coordinates running
workloads on clusters of up to thousands of nodes; it dominates container
orchestration like Google dominates search. Google wanted to collaborate with
Docker on Kubernetes development in 2014, but Docker decided to go its own way
with Swarm. Instead, Kubernetes grew up under the auspices of the Cloud Native
Computing Foundation (CNCF). By 2017, Kubernetes had grown so popular that
Docker announced that it would be integrated into Docker's own product.

Aside from its popularity, Kubernetes is primarily known for its complexity.
Setting up a new cluster by hand is an involved task, which requires the
administrator to select and configure several third-party components in
addition to Kubernetes itself. Much like the Linux kernel needs to be combined
with additional software to make a complete operating system, Kubernetes is
only an orchestrator and needs to be combined with additional software to make
a complete cluster. It needs a container engine to run its containers; it also
needs plugins for networking and persistent volumes.

Kubernetes distributions exist to fill this gap. Like a Linux distribution, a
Kubernetes distribution bundles Kubernetes with an installer and a curated
selection of third-party components. Different distributions exist to fill
different niches; seemingly every tech company of a certain size has its own
distribution and/or hosted offering to cater to enterprises. The minikube
project offers an easier on-ramp for developers looking for a local environment
to experiment with. Unlike their Linux counterparts, Kubernetes distributions
are certified for conformance by the CNCF; each distribution must implement the
same baseline of functionality in order to obtain the certification, which
allows them to use the "Certified Kubernetes" badge.

A Kubernetes cluster contains several software components. Every node in the
cluster runs an agent called the kubelet to maintain membership in the cluster
and accept work from it, a container engine, and kube-proxy to enable network
communication with containers running on other nodes.

The components that maintain the state of the cluster and make decisions about
resource allocations are collectively referred to as the control plane — these
include a distributed key-value store called etcd, a scheduler that assigns
work to cluster nodes, and one or more controller processes that react to
changes in the state of the cluster and trigger any actions needed to make the
actual state match the desired state. Users and cluster nodes interact with the
control plane through the Kubernetes API server. To effect changes, users set
the desired state of the cluster through the API server, while the kubelet
reports the actual state of each cluster node to the controller processes.

Kubernetes runs containers inside an abstraction called a pod, which can
contain one or more containers, although running containers for more than one
service in a pod is discouraged. Instead, a pod will generally have a single
main container that provides a service, and possibly one or more "sidecar"
containers that collect metrics or logs from the service running in the main
container. All of the containers in a pod will be scheduled together on the
same machine, and will share a network namespace — containers running within
the same pod can communicate with each other over the loopback interface. Each
pod receives its own unique IP address within the cluster. Containers running
in different pods can communicate with each other using their cluster IP
addresses.

A pod specifies a set of containers to run, but the definition of a pod says
nothing about where to run those containers, or how long to run them for —
without this information, Kubernetes will start the containers somewhere on the
cluster, but will not restart them when they exit, and may abruptly terminate
them if the control plane decides the resources they are using are needed by
another workload. For this reason, pods are rarely used alone; instead, the
definition of a pod is usually wrapped in a Deployment object, which is used to
define a persistent service. Like Compose and Swarm, the objects managed by
Kubernetes are declared in YAML; for Kubernetes, the YAML declarations are
submitted to the cluster using the kubectl tool.

In addition to pods and Deployments, Kubernetes can manage many other types of
objects, like load balancers and authorization policies. The list of supported
APIs is continually evolving, and will vary depending on which version of
Kubernetes and which distribution a cluster is running. Custom resources can be
used to add APIs to a cluster to manage additional types of objects. KubeVirt
adds APIs to enable Kubernetes to run virtual machines, for example. The
complete list of APIs supported by a particular cluster can be discovered with
the kubectl api-versions command.

Unlike Compose, each of these objects is declared in a separate YAML document,
although multiple YAML documents can be inlined in the same file by separating
them with "---", as seen in the Kubernetes documentation. A complex application
might consist of many objects with their definitions spread across multiple
files; keeping all of these definitions in sync with each other when
maintaining such an application can be quite a chore. In order to make this
easier, some Kubernetes administrators have turned to templating tools like
Jsonnet.

Helm takes the templating approach a step further. Like Kubernetes, development
of Helm takes place under the aegis of the CNCF; it is billed as "the package
manager for Kubernetes". Helm generates YAML configurations for Kubernetes from
a collection of templates and variable declarations called a chart. Its
template language is distinct from the Jinja templates used by Ansible but
looks fairly similar to them; people who are familiar with Ansible Roles will
likely feel at home with Helm Charts.

Collections of Helm charts can be published in Helm repositories; Artifact Hub
provides a large directory of public Helm repositories. Administrators can add
these repositories to their Helm configuration and use the ready-made Helm
charts to deploy prepackaged versions of popular applications to their cluster.
Recent versions of Helm also support pushing and pulling charts to and from
container registries, giving administrators the option to store charts in the
same place that they store container images.

Kubernetes shows no signs of losing momentum any time soon. It is designed to
manage any type of resource; this flexibility, as demonstrated by the KubeVirt
virtual-machine controller, gives it the potential to remain relevant even if
containerized workloads should eventually fall out of favor. Development
proceeds at a healthy clip and new major releases come out regularly. Releases
are supported for a year; there doesn't seem to be a long-term support version
available. Upgrading a cluster is supported, but some prefer to bring up a new
cluster and migrate their services over to it.

Nomad
-----

Nomad is an orchestrator from HashiCorp, which is marketed as a simpler
alternative to Kubernetes. Nomad is an open source project, like Docker and
Kubernetes. It consists of a single binary called nomad, which can be used to
start a daemon called the agent and also serves as a CLI to communicate with an
agent. Depending on how it is configured, the agent process can run in one of
two modes. Agents running in server mode accept jobs and allocate cluster
resources for them. Agents running in client mode contact the servers to
receive jobs, run them, and report their status back to the servers. The agent
can also run in development mode, where it takes on the role of both client and
server to form a single-node cluster that can be used for testing purposes.

Creating a Nomad cluster can be quite simple. In Nomad's most basic mode of
operation, the initial server agent must be started, then additional nodes can
be added to the cluster using the nomad server join command. HashiCorp also
provides Consul, which is a general-purpose service mesh and discovery tool.
While it can be used standalone, Nomad is probably at its best when used in
combination with Consul. The Nomad agent can use Consul to automatically
discover and join a cluster, and can also perform health checks, serve DNS
records, and provide HTTPS proxies to services running on the cluster.

Nomad supports complex cluster topologies. Each cluster is divided into one or
more "data centers". Like Swarm, server agents within a single data center
communicate with each other using a protocol based on Raft; this protocol has
tight latency requirements, but multiple data centers may be linked together
using a gossip protocol that allows information to propagate through the
cluster without each server having to maintain a direct connection to every
other. Data centers linked together in this way can act as one cluster from a
user's perspective. This architecture gives Nomad an advantage when scaled up
to enormous clusters. Kubernetes officially supports up to 5,000 nodes and
300,000 containers, whereas Nomad's documentation cites example of clusters
containing over 10,000 nodes and 2,000,000 containers.

Like Kubernetes, Nomad doesn't include a container engine or runtime. It uses
task drivers to run jobs. Task drivers that use Docker and Podman to run
containers are included; community-supported drivers are available for other
container engines. Also like Kubernetes, Nomad's ambitions are not limited to
containers; there are also task drivers for other types of workloads, including
a fork/exec driver that simply runs a command on the host, a QEMU driver for
running virtual machines, and a Java driver for launching Java applications.
Community-supported task drivers connect Nomad to other types of workloads.

Unlike Docker or Kubernetes, Nomad eschews YAML in favor of HashiCorp
Configuration Language (HCL), which was originally created for another
HashiCorp project for provisioning cloud resources called Terraform. HCL is
used across the HashiCorp product line, although it has limited adoption
elsewhere. Documents written in HCL can easily be converted to JSON, but it
aims to provide a syntax that is more finger-friendly than JSON and less
error-prone than YAML.

HashiCorp's equivalent to Helm is called Nomad Pack. Like Helm, Nomad Pack
processes a directory full of templates and variable declarations to generate
job configurations. Nomad also has a community registry of pre-packaged
applications, but the selection is much smaller than what is available for Helm
at Artifact Hub.

Nomad does not have the same level of popularity as Kubernetes. Like Swarm, its
development appears to be primarily driven by its creators; although it has
been deployed by many large companies, HashiCorp is still very much the center
of the community around Nomad. At this point, it seems unlikely the project has
gained enough momentum to have a life independent from its corporate parent.
Users can perhaps find assurance in the fact that HashiCorp is much more
clearly committed to the development and promotion of Nomad than Docker is to
Swarm.

Conclusion

Swarm, Kubernetes, and Nomad are not the only container orchestrators, but they
are the three most viable. Apache Mesos can also be used to run containers, but
it was nearly mothballed in 2021; DC/OS is based on Mesos, but much like Docker
Enterprise Edition, the company that backed its development is now focused on
Kubernetes. Most "other" container orchestration projects, like OpenShift and
Rancher, are actually just enhanced (and certified) Kubernetes distributions,
even if they don't have Kubernetes in their name.

Despite (or perhaps, because of) its complexity, Kubernetes currently enjoys
the most popularity by far, but HashiCorp's successes with Nomad show that
there is still room for alternatives. Some users remain loyal to the simplicity
of Docker Swarm, but its future is uncertain. Other alternatives appear to be
largely abandoned at this point. It would seem that the landscape has largely
settled around these three players, but container orchestration is a still a
relatively immature area. Ten years ago, very little of this technology even
existed, and things are still evolving quickly. There are likely many exciting
new ideas and developments in container orchestration that are still to come.

Overlay FS
----------

The first is overlayfs. As the name might suggest, overlayfs allows overlaying
the files in one directory (the "upper" directory, in overlayfs parlance) on
top of the files in another (the "lower" directory.) This results in a mount
point that contains all of the files in both the upper and the lower
directories; if both directories contain a file with the same name, overlayfs
presents the version present in the upper directory. Any changes made to an
overlayfs mount are reflected in the upper directory. The functionality
provided by overlayfs is particularly valuable to container runtimes such as
Docker that store container images as a series of layers; overlayfs provides an
efficient way of constructing a container's root directory from these layers.
It has been a part of the kernel since version 3.18 in 2014.

Architecture of the CRI plugin

* https://github.com/containerd/containerd/blob/main/docs/cri/architecture.md
