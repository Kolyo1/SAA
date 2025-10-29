#include <stdio.h>
#include <stdlib.h>
int isIn(int x , int arr[], int size){
    for(int i = 0; i < size; i++){
        if(arr[i] == x){
            return 1;
        }
    }
    return 0;
}
// 1
int main(){
int tDigits;
scanf("%d", &tDigits);
int sum = 0;
while(tDigits>0){
    sum += tDigits % 10;
    tDigits/=10;
}

printf("%d", sum);


// 2

int a, b;
scanf("%d %d", &a, &b);
printf("\n%d %d", a, b);
a = a + b;
b = a - b;
a = a - b;
printf("\n%d %d", a, b);

// 3

int n = 0;
int x = 2;
int xn;
while (x < 100){
    xn = 2*x*n + 10;
    x = xn;
    n++;
    printf("\n%d", xn);

}
printf("\n%d", xn);

// 4

int arr[] = {2 , -2, 3 , -3, 4, -4, 5, -5};
int size = sizeof(arr)/sizeof(arr[0]);
int count = 0;
for(int i = 0; i < size; i++){
    for(int j = i+1; j < size; j++){
        if((abs(arr[i]) == abs(arr[j])) && (arr[i] != arr[j])){
            count++;
    }
}
}
printf("%d", count);

// 5 

long long proz = 1;
int arr[] = {10, 20, 30, 40, 50, 60, 70, 80, 90};
int size = sizeof(arr)/sizeof(arr[0]);
int  results[20];
int size2 = 0;
for(int i = 0; i < size; i++){
    for(int j = i+1; j < size; j++){
        if(arr[i]+arr[j] <= 120){
            if(!isIn(arr[i],results,size2))results[size2++] = arr[i];
            if(!isIn(arr[j],results,size2))results[size2++] = arr[j];
    }
}
}

for (int i = 0; i < size2; i++){
    proz *= results[i];
}
printf("%lld\n", proz);   

// 6
int plosh[] = {1, 1, 2, 2, 2, 1, 1, 1, 2,2,2 };
int rn = 0;
int size3 = sizeof(plosh)/sizeof(plosh[0]);
int count1 = 0;
for (int i = 0; i < size; i++){
    if(plosh[i] == plosh[i+1]) {
        if(!rn){
            count1++;
            rn = 1;
        }
        else {
            rn = 0;
        }
    }
}
printf("%d", count1);
return 0;

}