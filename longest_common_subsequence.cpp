/*
	Author :- Tanay Kulkarni
	Date   :- 18-4-2021
	Time   :- 18:11:12.551448
	Name   :- solve.cpp 
*/
#include<bits/stdc++.h>
using namespace std;
void debug(string j){
cout<<"| Value : "<<j<<" |\n";
}
void debug(int j){
cout<<"| Value : "<<j<<" |\n";
}
void debug(int i,string j){
cout<<"Iteration "<<i<<": "<<j<<"\n";
}
void debug(int i,int j){
cout<<"Iteration "<<i<<": "<<j<<"\n";
}
string a ="tasdas" ,b = "sdfas";
int lcs(int n,int m){
	if(n == 0 || m == 0)
		return 0;
	if(a[n-1] == b[m-1])
		return 1+lcs(n-1,m-1);
	else{
		int a = lcs(n-1,m);
		int b = lcs(n,m-1);
		return max(a,b);
	}
}
void testcase(){
	
	cin>>a>>b;
	int n = a.length();
	int m = b.length();
	cout<<lcs(n,m);
	puts("");
}
int main(){
int t;
cin>>t;
for(int i = 1;i<=t;i++){
		cout<<"Case #"<<i<<": ";
		testcase();
}
return 0;
}
