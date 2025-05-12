# Makefile for KAS-XMSS C reference
CC = gcc
CFLAGS = -Wall -O2
LDFLAGS = -lssl -lcrypto

all: kas_xmss

kas_xmss: kas_xmss.c
	$(CC) $(CFLAGS) -o kas_xmss kas_xmss.c $(LDFLAGS)

clean:
	rm -f kas_xmss
