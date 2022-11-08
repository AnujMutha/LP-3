/*
Name: Anuj Mahendra Mutha
Class:BE-4
Batch : R4
Lab Assignment No: 01 
Title: Write a program non-recursive and recursive program to calculate Fibonacci numbers and 
analyze their time and space complexity.
*/

//Non-Recursive code (Part-1)
#include<iostream>
using namespace std;

int main()
{
	int n,a=0,b=1,fib;
	cout<<"Enter length of series"<<endl;
	cin>>n;
	if(n<=1)
	{
		return n;
	}
	while(a<n)
	{
		cout<<a<<endl;
		fib=a+b;
		a=b;
		b=fib;
	}
	return 0;
}
/*
Output :
Enter length of series
10
0
1
1
2
3
5
8
*/
//Non-Recursive code (Part-2)

/*
#include <iostream>
using namespace std;
int fibbonacci(int n) {
   if(n == 0)
   {
      return 0;
   } 
   else if(n == 1) 
   {
      return 1;
   } 
   else 
   {
      return (fibbonacci(n-1) + fibbonacci(n-2));
   }
}
int main()
{
    int n;
    cout<<"Enter length for fibonacci series";
    cin>>n;
    printf("Fibbonacci of %d: " , n);
    for(int i = 0; i < n ; i++) 
    {
        printf("%d ",fibbonacci(i));            
    }
    return 0;  
}
//Output : 
Enter length for fibonacci series10
Fibbonacci of 10: 0 1 1 2 3 5 8 13 21 34 
*/