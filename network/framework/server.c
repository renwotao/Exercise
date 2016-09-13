#include <netinet/in.h>
#include "skel.h"

static void server(SOCKET s, struct sockaddr_in *peerp)
{
    send(s, "hello, world\n", 13, 0);
}
