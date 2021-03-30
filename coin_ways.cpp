#include<bits/stdc++.h>
using namespace std;	
#define read(a) cin>>a;
/*

	coin problem where our task is to
	calculate the total number of ways to produce a sum x using the coins. For
	example, if coins = {1,3,4} and x = 5, there are a total of 6 ways:

*/
int ways(int n){
	
	int coins[3] = {1,3,4};
	int dp[n+1];
	for(int i = 0;i<n+1;i++)
		dp[i] = 0;
	dp[0] = 1;
	for(int i = 0;i<n+1;i++){
		for(int j : coins){
			if(i-j>=0)
				dp[i] += dp[i-j];
		}
	}
	return dp[n];	
}
int main(){
	int n;
	read(n)
	cout<<ways(n)<<"\n";
    return 0;
}
