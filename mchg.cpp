#include<stdio.h>
#include<iostream>
#include<bits/stdc++.h>
#include<map>
#include <vector> 
#include<string>
using namespace std;
#define FOR(start,end) for(int i=start;i<end;i++)
#define lli long long int 
#define read(a) cin>>a;
#define readr(b,n) for(lli i=0;i<n;i++){cin>>b[i];}
#define printarr(arr,n) FOR(0,n){cout<<arr[i]<<" "; }cout<<endl;
const int MOD = 1000000007;
//#define st(t) std::to_string(t)
lli sumarr(lli arr[],lli n){
	lli sum=0;
	FOR(0,n){
		sum = sum+arr[i];
	}
	return sum;
}
//reverse
void reverse(lli arr[],lli n){
	lli mid = (lli)((n-1)/2);
	lli last = n-1;
	FOR(0,mid+1){
	lli temp = arr[last-i];
	arr[last-i] = arr[i];
	arr[i] = temp;	
	}
}
// deletion
int del(int arr[],int n,int index){
	if(n==0)
	return 0;
	FOR(index,n){
		arr[i] = arr[i+1];
	}
	return n-1;
}
int remove(int arr[],int n,int element){
	int temp = 0;
	int index;
	FOR(0,n){
	if(arr[i] == element){
		temp = i;
		break;
	}	
	}
	if(temp == 0)
	return n;
	else
	del(arr,n,temp);	
return n;
}

// A^N
lli power(lli a,lli n){
	if(n==0)
	return 1;
	lli half_power = power(a,(lli)n/2);
	if(n%2==0)
	return half_power*half_power;
	else
	return half_power*half_power*a;
}
// linear search
bool linear_search(long long int arr[],long long int n,long long int find){
	FOR(0,n){
		if(arr[i] == find)
		return true;
	}
	return false;
}
// binary search
lli binary_search(lli arr[],lli n,lli find){
	lli l = 0;
	lli r = n-1;
	while(l<=r){
		lli mid = l+(r-l)/2;
		if(arr[mid] ==  find)
			return mid;
		else{
			if(arr[mid]>find)
				r = mid-1;
			else
				l = mid+1;
		}
	}
	return -1; 
}
// insertion
lli append(lli arr[],lli n,lli element){
	arr[n] = element;
	return n+1;
}
// Start Area to write solution

void solve(){
	
	lli n;
	read(n)
	if(n%100 == 0){
		cout<<n/100;
		return;	
	}
	const int mx = 1e9+7;
	int arr[5] = {1,5,10,20,100};
	lli dp[n+1];
	memset(dp,mx,sizeof(dp));
	dp[0] = 0;
	for (int i = 1; i <= n; i++)
	{
		for(int x = 4;x>=0;x--){
			if(i-arr[x]>=0)
				dp[i] = min(dp[i],dp[i-arr[x]]+1);
		}
	}
	cout<<dp[n]<<endl;
}

// End Area to write solution
int main(){
	solve();
	return 0;
}

/*

3 6
1 3 4


*/

