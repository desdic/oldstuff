NASM=nasm
ELFFLAGS=-f elf
DOSFLAGS=-fbin -DDOS
LD=ld
LDFLAGS=-m elf_i386 -s
BINS=pong.com

.PHONY: all

all: $(BINS)

pong.com: pong.asm
	$(NASM) $< $(DOSFLAGS) -o $@

pong: pong.asm
	$(NASM) $< $(ELFFLAGS) -o $@.o
	$(LD) $(LDFLAGS) -s -o $@ $@.o

clean:
	rm -f *.o
	rm -f $(BINS)
