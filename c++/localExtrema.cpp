#include <vector>
#include <iostream>
using namespace std;

int solution(vector<int> &A);

int main() {
  // int myints[] = {2,2,3,4,3,3,2,2,1,1,2,5};
  // int myints[] = {2,2};
  int myints[] = {1,2,3,4,5};
  vector<int> input (myints, myints + sizeof(myints) / sizeof(int) );
  cout << solution(input);
  return 0;
}

int solution(vector<int> &A) {
  if (A.size() == 0) return 0;
  if (A.size() == 1) return 1;

  int i = 0, j = 1;
  while (j < A.size()) {
    if (A[j] == A[i]) {
      j++;
    } else {
      i++;
      A[i] = A[j];
      j++;
    }
  }
  int end = i + 1;

  i = 0;
  int count = 0;
  while (i < end) {
    if (i == 0) count++;
    else if (i == end - 1) count++;
    else if ((A[i] > A[i-1] && A[i] > A[i+1]) || (A[i] < A[i-1] && A[i] < A[i+1])) {
      count++;
    }
    i++;
  }
  return count;
}
