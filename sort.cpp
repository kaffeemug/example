#include <bits/stdc++.h>
#include <algorithm>
using namespace std;


/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	
	int n;
	cin >> n;
		
	int number[1000];
	
	for(int i = 0 ; i < n ; i++){
		
		cin >> number[i];
		
	}
	
	sort(number,number+n);
	
	for(int i = 0 ; i < n ; i++){
		
		cout << number[i] <<endl;
		
	}
	
	
	return 0;
}