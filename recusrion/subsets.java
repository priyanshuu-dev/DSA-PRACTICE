// #leetcode 78
import java.util.*;
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<Integer> curr = new ArrayList<>();
        List<List<Integer>> ans = new ArrayList<>();


        sub(nums,0,curr,ans);
        return ans;

}
     private void sub(int[] arr, int idx,List<Integer> curr,List<List<Integer>> ans){
        if(idx==arr.length){
            ans.add(new ArrayList<> (curr));
            return;
        }

        curr.add(arr[idx]);
        sub(arr,idx+1,curr,ans);

        curr.remove(curr.size()-1);
        sub(arr,idx+1,curr,ans);
     }
}