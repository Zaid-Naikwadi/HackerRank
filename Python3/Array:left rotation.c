//problem statement link: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#include <stdio.h>

int main(int argc, char const *argv[])
{
	int arr[10];
	int arr1[10];
	int len;
	int d;
	printf("Enterlength of array\n");
	scanf("%d",&len);

	for(int i=0;i<len;++i){
		scanf("%d",&arr[i]);
	}

	printf("Enter number of times to be rotated\n");
	scanf("%d",&d);

	int cnt=0;
	for(int j=d;j<len;j++){
			arr1[j-d] = arr[j]; 
			cnt++;
		}

	
	for(int k=0;k<d;k++){
			arr1[cnt] = arr[k];
			cnt++;
		}


	printf("Rotated array:\n");
	for(int l=0;l<len;l++){
		printf("%d ",arr1[l]);
	}


	return 0;
}
