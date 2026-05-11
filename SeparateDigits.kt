class Solution {
    fun separateDigits(nums: IntArray): IntArray {
        val l = mutableListOf<Int>()
        val stack = mutableListOf<Int>()
        for (n in nums) {
            var n = n
            while (n >= 10) {
                stack.add(n % 10)
                n = n.floorDiv(10)
            }
            l.add(n)
            while (stack.isNotEmpty()) {
                l.add(stack.removeAt(stack.size - 1))
            }
        }
        return l.toIntArray()
    }
}
