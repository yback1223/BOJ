#include <stdio.h>

int main(void)
{
    int a, b;
    while(scanf("%d %d", &a, &b) == 2)
    {
        if (a == 0 && b == 0)
            return 0;
        printf("%d\n", a + b);
    }
}