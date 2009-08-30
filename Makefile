# ex: set ts=8 noet:

CFLAGS = -W -Wall -Os -std=c99 -pedantic
LDFLAGS =
BINS = 7 10

all: $(BINS)

7: 7.o miller-rabin.o
10: 10.o miller-rabin.o

clean:
	$(RM) $(BINS)

