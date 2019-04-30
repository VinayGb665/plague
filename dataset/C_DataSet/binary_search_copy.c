#include<stdio.h>
#include<stdlib.h>

int binary_search(int l, int r, int *arr, int ele) {
	int mid = (l+r)/2;
	if(ele==arr[mid])
		return mid;
	else {
		if(l>=r)
			return -1;
		else if(arr[mid]>ele)
			return binary_search(l,mid-1,arr,ele);
		else
			return binary_search(mid+1,r,arr,ele);
	}
}

int main() {
	int *a=(int *)malloc(sizeof(int)*1000);
	int n,i,x;
	scanf("%d", &n);
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	scanf("%d", &x);
	printf("Search index: %d\n",binary_search(0,n-1,a,x));
}
