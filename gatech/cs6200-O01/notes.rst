Network Programming
===================

* https://beej.us/guide/bgnet/html/single/bgnet.html#theory


My First StructTM—struct addrinfo. This structure is a more recent invention, and is used to
prep the socket address structures for subsequent use. It's also used in host name lookups,
and service name lookups. That'll make more sense later when we get to actual usage, but
just know for now that it's one of the first things you'll call when making a connection.

.. code-block::

    struct addrinfo {
        int              ai_flags;     // AI_PASSIVE, AI_CANONNAME, etc.
        int              ai_family;    // AF_INET, AF_INET6, AF_UNSPEC
        int              ai_socktype;  // SOCK_STREAM, SOCK_DGRAM
        int              ai_protocol;  // use 0 for "any"
        size_t           ai_addrlen;   // size of ai_addr in bytes
        struct sockaddr *ai_addr;      // struct sockaddr_in or _in6
        char            *ai_canonname; // full canonical hostname

        struct addrinfo *ai_next;      // linked list, next node
    };



You'll load this struct up a bit, and then call getaddrinfo(). It'll return a pointer
to a new linked list of these structures filled out with all the goodies you need.


.. code-block::

    struct sockaddr {
        unsigned short    sa_family;    // address family, AF_xxx
        char              sa_data[14];  // 14 bytes of protocol address
    };


And this is the important bit: a pointer to a struct sockaddr_in can be cast to a
pointer to a struct sockaddr and vice-versa. So even though connect() wants a struct
sockaddr*, you can still use a struct sockaddr_in and cast it at the last minute!


.. code-block::

    // (IPv4 only--see struct sockaddr_in6 for IPv6)

    struct sockaddr_in {
        short int          sin_family;  // Address family, AF_INET
        unsigned short int sin_port;    // Port number
        struct in_addr     sin_addr;    // Internet address
        unsigned char      sin_zero[8]; // Same size as struct sockaddr
    };



*  the sin_port must be in Network Byte Order (by using htons()!)

.. code-block::

    // (IPv4 only--see struct in6_addr for IPv6)

    // Internet address (a structure for historical reasons)
    struct in_addr {
        uint32_t s_addr; // that's a 32-bit int (4 bytes)
    };


.. code-block::

    // (IPv6 only--see struct sockaddr_in and struct in_addr for IPv4)

    struct sockaddr_in6 {
        u_int16_t       sin6_family;   // address family, AF_INET6
        u_int16_t       sin6_port;     // port number, Network Byte Order
        u_int32_t       sin6_flowinfo; // IPv6 flow information
        struct in6_addr sin6_addr;     // IPv6 address
        u_int32_t       sin6_scope_id; // Scope ID
    };

    struct in6_addr {
        unsigned char   s6_addr[16];   // IPv6 address
    };


.. code-block::

    struct sockaddr_storage {
        sa_family_t  ss_family;     // address family

        // all this is padding, implementation specific, ignore it:
        char      __ss_pad1[_SS_PAD1SIZE];
    int64_t   __ss_align;
    char      __ss_pad2[_SS_PAD2SIZE];
    };



What's important is that you can see the address family in the ss_family field—check this to see if it's AF_INET
or AF_INET6 (for IPv4 or IPv6). Then you can cast it to a struct sockaddr_in or struct sockaddr_in6 if you wanna.



3.4. IP Addresses, Part Deux
----------------------------


The function you want to use, inet_pton(), converts an IP address in numbers-and-dots notation into either
a struct in_addr or a struct in6_addr depending on whether you specify AF_INET or AF_INET6. ("pton" stands
for "presentation to network"—you can call it "printable to network" if that's easier to remember.)


.. code-block::

    struct sockaddr_in sa; // IPv4
    struct sockaddr_in6 sa6; // IPv6

    inet_pton(AF_INET, "10.12.110.57", &(sa.sin_addr)); // IPv4
    inet_pton(AF_INET6, "2001:db8:63b3:1::3490", &(sa6.sin6_addr)); // IPv6


Now, the above code snippet isn't very robust because there is no error checking. See, inet_pton() returns -1
on error, or 0 if the address is messed up. So check to make sure the result is greater than 0 before using!


Network to printable.

.. code-block::

    // IPv4:

    char ip4[INET_ADDRSTRLEN];  // space to hold the IPv4 string
    struct sockaddr_in sa;      // pretend this is loaded with something

    inet_ntop(AF_INET, &(sa.sin_addr), ip4, INET_ADDRSTRLEN);

    printf("The IPv4 address is: %s\n", ip4);


    // IPv6:

    char ip6[INET6_ADDRSTRLEN]; // space to hold the IPv6 string
    struct sockaddr_in6 sa6;    // pretend this is loaded with something

    inet_ntop(AF_INET6, &(sa6.sin6_addr), ip6, INET6_ADDRSTRLEN);

    printf("The address is: %s\n", ip6);



getaddrinfo()—Prepare to launch!
--------------------------------

.. code-block::

    #include <sys/types.h>
    #include <sys/socket.h>
    #include <netdb.h>

    int getaddrinfo(const char *node,     // e.g. "www.example.com" or IP
                    const char *service,  // e.g. "http" or port number
                    const struct addrinfo *hints,
                    struct addrinfo **res);


socket()—Get the File Descriptor!
---------------------------------

.. code-block::


    #include <sys/types.h>
    #include <sys/socket.h>

    int socket(int domain, int type, int protocol);


Example.

.. code-block::

    int s;
    struct addrinfo hints, *res;

    // do the lookup
    // [pretend we already filled out the "hints" struct]
    getaddrinfo("www.example.com", "http", &hints, &res);

    // [again, you should do error-checking on getaddrinfo(), and walk
    // the "res" linked list looking for valid entries instead of just
    // assuming the first one is good (like many of these examples do.)
    // See the section on client/server for real examples.]

    s = socket(res->ai_family, res->ai_socktype, res->ai_protocol);


bind()—What port am I on?
-------------------------

Once you have a socket, you might have to associate that socket with a port on your local machine. (This is
commonly done if you're going to listen() for incoming connections on a specific port—multiplayer network games
do this when they tell you to "connect to 192.168.5.10 port 3490".) The port number is used by the kernel to
match an incoming packet to a certain process's socket descriptor. If you're going to only be doing a connect()
(because you're the client, not the server), this is probably be unnecessary. Read it anyway, just for kicks.

Here is the synopsis for the bind() system call:


.. code-block::

    #include <sys/types.h>
    #include <sys/socket.h>

    int bind(int sockfd, struct sockaddr *my_addr, int addrlen);


Example

.. code-block::

    struct addrinfo hints, *res;
    int sockfd;

    // first, load up address structs with getaddrinfo():

    memset(&hints, 0, sizeof hints);
    hints.ai_family = AF_UNSPEC;  // use IPv4 or IPv6, whichever
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_flags = AI_PASSIVE;     // fill in my IP for me

    getaddrinfo(NULL, "3490", &hints, &res);

    // make a socket:

    sockfd = socket(res->ai_family, res->ai_socktype, res->ai_protocol);

    // bind it to the port we passed in to getaddrinfo():

    bind(sockfd, res->ai_addr, res->ai_addrlen);


By using the AI_PASSIVE flag, I'm telling the program to bind to the IP of the
host it's running on. If you want to bind to a specific local IP address, drop
the AI_PASSIVE and put an IP address in for the first argument to getaddrinfo().


* Add code to your program allowing it to reuse the port

.. code-block::

    int yes=1;
    //char yes='1'; // Solaris people use this

    // lose the pesky "Address already in use" error message
    if (setsockopt(listener,SOL_SOCKET,SO_REUSEADDR,&yes,sizeof yes) == -1) {
        perror("setsockopt");
        exit(1);
    }


5.4. connect()
--------------

.. code-block::

    #include <sys/types.h>
    #include <sys/socket.h>

    int connect(int sockfd, struct sockaddr *serv_addr, int addrlen);



Example

.. code-block::

    struct addrinfo hints, *res;
    int sockfd;

    // first, load up address structs with getaddrinfo():

    memset(&hints, 0, sizeof hints);
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;

    getaddrinfo("www.example.com", "3490", &hints, &res);

    // make a socket:

    sockfd = socket(res->ai_family, res->ai_socktype, res->ai_protocol);

    // connect!

    connect(sockfd, res->ai_addr, res->ai_addrlen);


* You can now pass data back and forth on stream sockets! Whee! You're a Unix Network Programmer!
