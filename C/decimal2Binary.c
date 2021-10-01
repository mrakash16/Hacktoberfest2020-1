/******************************************************************
 * File         :   decimal2Binary
 * Description  :   Deciaml to Binary
 * Author       :   Jose K James
 * Version      :   0.12
 * Date         :   15/06/2021
******************************************************************/
#include <stdio.h>

int main()
{
    int number, reminder, temp, value = 0;

    printf("Enter number :\n");
    scanf("%d", &number);
    temp = number; //for output

    for (int power = 1; number > 0; power *= 10) //for place value
    {
        reminder = number % 2;
        value += reminder * power; //calculating binary value in reverse order
        number /= 2;
    }
    printf("\n'%d' in binary format : %d", temp, value);
}