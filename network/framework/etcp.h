#ifndef __ETCP_H__
#define __ETCP_H__

void set_address( char *host, char *port, 
                 struct sockaddr_in *sap, char *protocol );

void error( int status, int err, char *format, ... );

SOCKET tcp_server( char *host, char *port );

SOCKET tcp_client( char *host, char *port );
#endif
