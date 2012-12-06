#include <stdlib.h>
#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main() {
  int t;
  scanf("%d", &t);
  char equation[1001];
  while (t > 0) {
    int s = 1; // side of equation -> right = -1
    int z = 1; // sign of term -> - = 2
    int l = 0; // current number
    int x = 0; // sum of x's
    int c = 0; // sum of constants
    scanf("%s", equation);
    strcat(equation, "=");
    for (int i = 0; i < strlen(equation) ; i++) {
      if (equation[i] == '=') {
        c += l*z*s;
        l = 0;
        s = -1;
        z = 1;    
      }
      else if (equation[i] == '-') {
        c += l*z*s;
        l = 0;
        z = -1;
      }
      else if (equation[i] == '+') {
        c += l*z*s;
        l = 0;
        z = 1;
      }
      else if (equation[i] == 'x') {
        if (l == 0) {
          l = 1;
        }
        x += l*z*s;
        l = 0;
      }
      else { // if char in '0123456789':
        l = 10*l + (equation[i] - '0');
      }
    }
    if (x == 0) {
      printf("NIE\n");
    }
    else {
      printf("%d\n",int(-(float(c)) / x));
    }
    t -= 1;
  }
  return 0;
}
