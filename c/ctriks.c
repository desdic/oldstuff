#include <stdio.h>
#include <stdint.h>

int main(void) {
    size_t sz = 0b11111101;

    printf("%llx %c",
            sz & ~ 7ULL,
            "mM"[!!(sz & 2)]);

    return 0;
}
