ASM=nasm
ASMFLAGS=-f elf
GAS=as
LD=ld
LDFLAGS=-m elf_i386 -s
BINS=olleh olleh2

.PHONY: all

all: $(BINS)

%.o: %.asm
	$(ASM) $(ASMFLAGS) $<

att: att.s
	as -o att.o att.s
	ld -o att att.o

%: %.o
	$(LD) $(LDFLAGS) -s -o $@ $<

clean:
	rm -f *.o
	rm -f $(BINS)
