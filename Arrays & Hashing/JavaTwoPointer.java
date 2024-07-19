import java.util.Arrays;

/**
 * JavaTwoPointer
 */
public class JavaTwoPointer {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(new JavaTwoPointer().twoSum(new int[]{2,7,11,15}, 9)));
    }

    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        for (int i = 0; i < nums.length - 1; i++ ) {
            for (int j = 1; j < nums.length; j++) {
                if (i == j) {
                    continue;
                }
                System.out.println(i + " " + j);
                if (nums[i] + nums[j] == target) {
                    res[0] = i;
                    res[1] = j;
                    return res;
                }
            }
        }
        return res;
    }
}