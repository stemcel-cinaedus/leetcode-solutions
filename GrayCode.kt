class Solution {
    fun grayCode(n: Int): List<Int> {
        val mask = 1 shl n
        val output = mutableListOf<Int>()
        for (i in 0 until mask) {
            output.add(i xor (i shr 1)) 
        }
        return output
    }
}
