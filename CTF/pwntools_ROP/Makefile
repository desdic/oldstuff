CC=gcc
NOSTACK+=-fno-stack-protector -z execstack
CFLAGS+=-g -m32 -Wall -Wextra -ansi
SOURCES=$(wildcard *.c)
EXECUTABLE=rop1 rop2 rop3
OBJECTS=$(EXECUTABLE:%=%.o)

all: $(EXECUTABLE)

%: %.c
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm -f $(EXECUTABLE) $(OBJECTS)

