#ifndef __SKEL_H__
#define __SKEL_H__

/* UNIX version */
#define INIT()          program_name = \
                        trrchr( argv[ 0 ], '/' ) ) ? \
                        rogram_name++ : \
                        program_name = argv[ 0 ] )
#define EXIT(s)         xit( s )
#define CLOSE(s)        f (　close( s ) ) error( 1, errno, \
                        close failed" )
#define set_errno(e)    errno = ( e )
#define isvalidsock(s)  ( ( s ) >= 0 )

typedef int SOCKET;
#endif /* __SKEL_H__ */ 
