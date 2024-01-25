#include <stdio.h>
#include <math.h>


int convert_to_base(int num_to_convert, int source_base, int target_base){
    int value_to_convert;
    value_to_convert = 0;
    int mod;
    int i;
    i = 0;
    while (num_to_convert > 0){
        mod = num_to_convert % 16;
        num_to_convert = num_to_convert / 16;
        if (mod>=source_base){
            return -1;
        }
        value_to_convert += mod * (int)pow(source_base, i++);
    }


    int result;
    result = 0;
    i = 0;
    while (value_to_convert > 0){
        mod = value_to_convert % target_base;
        value_to_convert = value_to_convert / target_base;
        result += mod * (int)pow(16, i++);
    }

    return result;
}


int main() {
    int source_base, target_base, num_to_convert;

    printf("enter the source base:\n");
    if (!scanf("%d", &source_base) || source_base < 2 ||  source_base > 16)
    {
        printf("Invalid source base!");
        return 1;
    }

    printf("enter the target base:\n");
    if (!scanf("%d", &target_base) || target_base < 2 ||  target_base > 16)
    {
        printf("Invalid target base!");
        return 1;
    }

    printf("enter a number in base %d:\n", source_base);
    if (!scanf("%x", &num_to_convert))
    {
        printf("Invalid input number!!");
        return 1;
    }

    int result;
    result = convert_to_base(num_to_convert, source_base, target_base);
    if (result != -1){
        printf("The number in base %d is:\n%x", target_base, result);
    }
    else{
        printf("Invalid input number!");
    }

    return 0;
}

