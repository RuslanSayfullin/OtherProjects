#include <stdio.h>

// gcc -fPIC -shared -o libexample.so libexample.c
// -fPIC — генерация позиционно‑независимого кода (требуется для динамических библиотек).
// -shared — создание shared object

int add(int a, int b) {
    return a + b;
}

void print_message(const char* msg) {
    printf("Message: %s\n", msg);
}