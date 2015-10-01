#include <vector>
#include <unordered_map>
#include <queue>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> &T);

int main() {
  // int myints[] = {2,2,3,4,3,3,2,2,1,1,2,5};
  // int myints[] = {2,2};
  int myints[] = {9,1,4,9,0,4,8,9,0,1};
  vector<int> input (myints, myints + sizeof(myints) / sizeof(int) );
  vector<int> output = solution(input);
  cout << "result:"<<endl;
  for (int i = 0; i < output.size(); i++) {
    cout << output[i];
  }
  cout << endl;
  return 0;
}

vector<int> solution(vector<int> &T) {
  vector<int> empty;
  if (T.size() == 0) return empty;
    vector<int> res(T.size()-1, 0);

  unordered_map<int, vector<int> > hash;

  int capital = 0;
  for (int i = 0; i < T.size(); i++) {
    if (i == T[i]) {
      capital = i;
    }

    if (hash.find(i) == hash.end()) {
      vector<int> tmp;
      hash[i] = tmp;
    }
    hash[i].push_back(T[i]);
    if (hash.find(T[i]) == hash.end()) {
      vector<int> tmp;
      hash[T[i]] = tmp;
    }
    hash[T[i]].push_back(i);
  }

  queue<int> myQ;
  queue<int> distance;
  myQ.push(capital);
  distance.push(0);
  while (!myQ.empty()) {
    int node = myQ.front();
    myQ.pop();
    int path = distance.front();
    distance.pop();
    if (path > 0) {
      res[path-1] += 1;
    }
    vector<int> neighbors = hash[node];

    hash.erase(node);
    for (int i = 0; i < neighbors.size(); i++) {
      if (hash.find(neighbors[i])!= hash.end()) {
        myQ.push(neighbors[i]);
        distance.push(path+1);
      }
    }
  }
  return res;
}
