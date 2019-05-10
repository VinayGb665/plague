#include<stdio.h>
#include<stdlib.h>


int main()
{
	int i, num, element;
	int a[1000];

	scanf("%d", &num);
	for(i=0;i<num;i++)
		scanf("%d",&a[i]);
	scanf("%d", &element);
	int i;
	for(i=0;i<num;i++)
		if(a[i] == element)
			return i;
	return -1;

}
