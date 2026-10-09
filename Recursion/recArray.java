
package recu;
import java.util.*;

public class recArray {

    static int print(int [] arr,int idx){
        if(idx==arr.length-1){
            return arr[idx];
        }
        System.out.println(arr[idx]);
        return print(arr,idx+1);

    }

    static int sum(int [] arr,int idx,int total){
        if(idx==arr.length-1){
            return arr[idx]+total;
        }

        return sum(arr,idx+1,total+=arr[idx]);
    }

    static int max(int[] arr,int idx,int grt){
        if(idx==arr.length-1){
            return grt;
        }
        grt=Math.max(arr[idx],grt);
        return max(arr,idx+1,grt);

    }

    static int count(int [] arr,int idx,int countt){
        if(idx==arr.length-1){
            return countt;
        }
        if(arr[idx]==5){
            countt+=1;
        }
        return count(arr,idx+1,countt);
    }

    static boolean sorted(int [] arr,int idx){
        if(idx== arr.length-1){
            return true;
        }
        if(arr[idx]>arr[idx+1]){
            return false;
        }
        return sorted(arr,idx+ 1);
    }

    static boolean search(int [] arr,int idx,int target){
        if(arr[idx]==target){
            return true;
        }
        if(idx==arr.length-1 && arr[idx]!=target){
            return false;
        }
        return search(arr,idx+1,target);
    }

    static boolean pal(String s,int low,int high){
        if(low>=high){
            return true;
        }
        if(s.charAt(low)!=s.charAt(high)){
            return false;
        }

        return pal(s,low+1,high-1);
    }

    public static void main(String[] args) {
        int[] nums={5,4,8,9,6};

        System.out.println(print(nums,0));
        System.out.println(sum(nums,0,0));
        System.out.println(max(nums,0,0));
        System.out.println(count(nums,0,0));
        System.out.println(sorted(nums,0));
        System.out.println(search(nums,0,8));

        String p="madamm";
        System.out.println(pal(p,0,p.length()-1));
    }
}

