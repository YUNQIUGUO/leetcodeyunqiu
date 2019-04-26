class Solution {
public int maxEnvelopes(int[][] envelopes) {  
    
    if (envelopes.length == 0) {
        return 0;
    }
    // sort by the first element to reduce to 1D problem
    Arrays.sort(envelopes, (int[] a, int[] b ) -> {return Integer.compare(a[0], b[0]);});
    
    int[] L = new int[envelopes.length];
    for (int i = 0; i < L.length; ++i) {
        L[i] = 1;
    }
    int maxValue = 1;
    for (int i = 0; i < envelopes.length; ++i) {
        for (int j = 0; j < i; ++j) {
            if (envelopes[i][0] > envelopes[j][0] && envelopes[i][1] > envelopes[j][1])
            {
                L[i] = Math.max(L[i], L[j] + 1);
                maxValue = Math.max(maxValue, L[i]);
            }
        }
    }
    return maxValue;
}
}