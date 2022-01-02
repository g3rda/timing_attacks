#include <iostream>
#include <time.h>
#include <chrono>
#include <thread>
#include <vector>
#include<bits/stdc++.h>

using namespace std;

timespec diff(timespec start, timespec end);

inline long long  mod_exp(long long base, long long exponent, long long modulus) {
  long long result = 1;
  base = base % modulus;
  while (exponent > 0) {
    if (exponent & 1 == 1) {
      result = (result * base) % modulus;
    }
    exponent = exponent >> 1;
    base = base * base % modulus;
  }
  return result;
}

int main() {
  vector < int > bit1, bit0;
  timespec time1, time2;
  int temp, r;
  const long long base = 0b11010010101110101001010, modulus = 0b1010010100100101001010101101;
  const long long exponent1 = 0b10101000101000101100010;
  const long long exponent0 = 0b10101000101000101000010;

  for (int i = 0; i < 10000; i++) {
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, & time1);
    r = mod_exp(base, exponent1, modulus);
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, & time2);
    bit1.push_back(diff(time1, time2).tv_nsec);
  }
  cout << bitset<int(log2(exponent1))+1>(exponent1)<<": " << * min_element(bit1.begin(), bit1.end()) << " ns"<<endl;

  for (int i = 0; i < 10000; i++) {
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, & time1);
    r = mod_exp(base, exponent0, modulus);
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, & time2);
    bit0.push_back(diff(time1, time2).tv_nsec);
  }
  cout << std::bitset<int(log2(exponent0))+1>(exponent0)<<": " << * min_element(bit0.begin(), bit0.end()) <<" ns"<< endl;

  return 0;
}

timespec diff(timespec start, timespec end) {
  timespec temp;
  if ((end.tv_nsec - start.tv_nsec) < 0) {
    temp.tv_sec = end.tv_sec - start.tv_sec - 1;
    temp.tv_nsec = 1000000000 + end.tv_nsec - start.tv_nsec;
  } else {
    temp.tv_sec = end.tv_sec - start.tv_sec;
    temp.tv_nsec = end.tv_nsec - start.tv_nsec;
  }
  return temp;
}
