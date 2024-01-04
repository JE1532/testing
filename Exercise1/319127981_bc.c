#include <stdio.h>
#include <math.h>


int convert_to_decimal_base(int num_to_convert, int source_base)
{
    if (source_base == 10)
    {
        return num_to_convert;
    }

    int decimal_num = 0;
    for (int i= 0; num_to_convert != 0; i++)
    {
        int lsd = num_to_convert % 10;
        decimal_num += lsd * pow(source_base, i);
        num_to_convert /= 10;
    }
    return decimal_num;
}
int convert_base(int num_to_convert, int source_base, int target_base) {
    return 0;
}


int main() {
    int source_base, target_base, num_to_convert;

    printf("enter the source base: ");
    if (!scanf("%d", &source_base) || source_base < 2 ||  source_base > 16)
    {
        printf("Invalid source base!");
        return 1;
    }

    printf("enter the target base: ");
    if (!scanf("%d", &target_base) || target_base < 2 ||  target_base > 16)
    {
        printf("Invalid target base!");
        return 1;
    }

    printf("enter a number in base %d: ", source_base);
    if (!scanf("%d", &num_to_convert))
    {
        printf("Invalid target base!");
        return 1;
    }


    printf("The number in base %d is: %d", target_base, convert_base(num_to_convert, source_base, target_base));

    return 0;
}
