class Solution {
  public int numSteps(String s) {
    int ans = 0;
    StringBuilder sb = new StringBuilder(s);

    // All the trailing 0s can be popped by 1 step.
    while (sb.charAt(sb.length() - 1) == '0') {
      sb.deleteCharAt(sb.length() - 1);
      ++ans;
    }

    if (sb.toString().equals("1"))
      return ans;

    ++ans;

    for (final char c : sb.toString().toCharArray())
      ans += c == '1' ? 1 : 2;

    return ans;
  }
}