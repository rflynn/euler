# ex: set ts=8 noet:

CFLAGS = -W -Wall -Os -std=c99 -pedantic
LDFLAGS =
BINS = 07 10

all: $(BINS) venv

07: 07.o miller-rabin.o
10: 10.o miller-rabin.o

venv:
	virtualenv -p python3 venv

clean:
	$(RM) $(BINS) *.o

