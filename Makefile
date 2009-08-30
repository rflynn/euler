# ex: set ts=8 noet:

CFLAGS = -W -Wall -Os -std=c99 -pedantic
LDFLAGS =
BINS = 7

all: $(BINS)

clean:
	$(RM) $(BINS)

