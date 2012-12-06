#include <stdlib.h>
#include <iostream>
#include <cmath>
#include <stdio.h>

using namespace std;
int main()
{
  int t, n, m;
  cin >> t;
  for (int i = 0; i < t; i++) {
    cin >> n >> m;
    int c = 0;
    for (int j = 0; j < n; j++) {
      int p;
      cin >> p;
      c += 86400 / p;
    }
    printf("%d\n", (int)ceil(((float)c)/m));
  }
  return 0;
}
