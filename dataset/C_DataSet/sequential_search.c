#include<stdio.h>
#include<stdlib.h>

int seq_search(int arr[], int n, int ele) {
	int i;
	for(i=0;i<n;i++)
		if(arr[i]==ele)
			return i;
	return -1;
}

int main()
{
	int i, num, element;
	int a[1000];

	scanf("%d", &num);
	for(i=0;i<num;i++)
		scanf("%d",&a[i]);
	scanf("%d", &element);
	printf("Search index: %d\n", seq_search(a, num, element));

}
