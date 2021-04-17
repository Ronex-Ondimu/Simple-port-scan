#!/usr/bin/python3
import socket
import argparse

def soct(host):
    
    #s=socket.socket(socket.AF_INET,socket.sock_STREAM)
    for i in range(1,1000):
        
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result= s.connect_ex((host,i)) 
       # print(result)
        socket.setdefaulttimeout(1)        
        if result==0:                 
                print('port {} open'.format(i))
        s.close()

                 
if __name__=='__main__':
    parser=argparse.ArgumentParser(prog='PROG',description='simple port scan')
    parser.add_argument('host',type=str,help='target ip')
    args=parser.parse_args()
    soct(args.host)
