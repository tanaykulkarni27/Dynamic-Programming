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
bool binary_search(lli arr[],lli l,lli r,lli find){
if(l>=r)
	return 0;
int mid = (int)l+(r)/2;
cout<<mid<<"\n";  
if(arr[l] == find || arr[r] == find || arr[mid] == find)
return 1;

if(arr[l]<find){
return binary_search(arr,mid,r,find);
}
else
return binary_search(arr,l,mid,find);
}
// insertion
lli append(lli arr[],lli n,lli element){
	arr[n] = element;
	return n+1;
}
// Start Area to write solution

void solve(){
	int n;
	read(n)
	int k;
	read(k)
	int dp[n+1];
	memset(dp,0,sizeof(dp));
	for(int i = 0;i<=n;i++){
		for (int j = 1; j <= k; ++j)
		{
			if (i == 0)
				dp[i] = 1;
			else if(i-j>=0)
				dp[i] += dp[i-j];
		}
	}
	cout<<dp[n]<<"\n";
}
// End Area to write solution
int main(){
	int t;
	read(t)
	FOR(1,t+1){
	cout<<"Case #"<<i<<": ";
	solve();
	}
	return 0;
}

/*

*/

