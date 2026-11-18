file_name="test.cpp"
echo '#include <iostream>

using namespace std;

int main() {
  int x;
  cin >> x;
  switch (x) {' >$file_name

for i in {54845..100000}; do
  solution=$(echo $i | python3 palindromic_sums.py)
  echo "    case $i :
  cout << $(echo '"'$solution'"') << '\n';
      return 0;" >>$file_name
  echo $i
done

echo "  }
}" >>$file_name
