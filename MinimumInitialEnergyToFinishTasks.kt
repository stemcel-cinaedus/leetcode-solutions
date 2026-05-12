class Solution {
    fun minimumEffort(tasks: Array<IntArray>): Int {
        val lower_bound = tasks.sumOf { it.first() }
        val upper_bound = tasks.sumOf { it.last() }
        val tasks = tasks.sortedByDescending { abs(it.first() - it.last()) }

        fun f(x: Int): Boolean {
            var x = x
            for (arr in tasks) {
                if (x >= arr[1]) {
                    x -= arr[0]
                } else {
                    return false
                }
            }
            return true
        }

        var m = lower_bound
        while (m <= upper_bound) {
            if (f(m)) {
                return m
            }
            m++ 
        }
        return upper_bound
    }
}
