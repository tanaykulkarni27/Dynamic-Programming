/*
	Author :- Tanay Kulkarni
	Date   :- 18-4-2021
	Time   :- 17:13:54.486547
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
int mat[100][100];
map<pair<int,int>,int>ms;
int MaxPath(int x,int y){
	if(x<=-1 || y <=-1)
		return 0;
	pair<int,int> key = {x,y};
	if(ms[key]){
		return ms[key];
	}
	else{
		int a = mat[y][x]+MaxPath(x-1,y);
		int b = mat[y][x]+MaxPath(x,y-1);
		ms[key] = max(a,b);
		return ms[key];
	}
}
void testcase(){
	
	int n ;
	cin>>n;
	for(int i = 0;i<n;i++){
		for(int j = 0;j<n;j++){
			cin>>mat[i][j];
		}
	}
	cout<<MaxPath(n-1,n-1);
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
