#include <stdio.h>
#include <stdlib.h>

void foo(char* str) {
    char* temp = NULL;
    if (str[0] == 'a') {
        while(1){}
    } else if (str[0] == 'b') {
        free(NULL);
    } else if (str[0] == 'c') {
        putchar('p');
    } else {
        putchar(str[3]);
    }
}
int main() {
    int a = ((((('a'<<8)|'b')<<8)|'c')<<8)|'d';
    foo((char*)&a + 1);
    return 0;
}
