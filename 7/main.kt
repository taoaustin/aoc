import kotlin.collections.mutableMapOf
import java.io.File

class Hand(line: String) {
    val hand: String
    val bid: Int
    val typePower: Int
    val typePower2: Int

    init {
        val lineSplit = line.split(" ")
        hand = lineSplit[0]
        bid = lineSplit[1].toInt()
        typePower = determineRank(cardFreqMap())
        typePower2 = determineRank(cardFreqMap2())
    }

    private fun cardFreqMap(): Map<Char, Int> {
        var m = mutableMapOf<Char, Int>()
        for (c in hand) {
            m[c] = m.getOrDefault(c, 0) + 1
        }
        return m
    }

    private fun cardFreqMap2(): Map<Char, Int> {
        var m = mutableMapOf<Char, Int>()
        var jCount: Int = 0
        for (c in hand) {
            if (c != 'J') m[c] = m.getOrDefault(c, 0) + 1
            else jCount++
        }
        if (m.size == 0) m['J'] = 0
        val maxItem = m.maxBy { it.value }
        m[maxItem.key] = m.getOrDefault(maxItem.key, 0) + jCount
        return m
    }

    private fun determineRank(m: Map<Char, Int>): Int {
        if (m.size == 1) return 6
        else if (m.size == 5) return 0
        else if (m.size == 4) return 1
        else if (m.size == 2) {
            val filteredM = m.filter { (_, v) -> v > 3 }
            if (filteredM.size == 1) return 5
            return 4
        } else {
            val filteredM = m.filter { (_, v) -> v > 2 }
            if (filteredM.size == 1) return 3
            return 2
        }
    }
}

val cardMap = mapOf('2' to 2, '3' to 3, '4' to 4, '5' to 5, '6' to 6, '7' to 7, '8' to 8, '9' to 9, 'T' to 10, 'J' to 11, 'Q' to 12, 'K' to 13, 'A' to 14)
val cardMap2 = mapOf('2' to 2, '3' to 3, '4' to 4, '5' to 5, '6' to 6, '7' to 7, '8' to 8, '9' to 9, 'T' to 10, 'J' to -1, 'Q' to 12, 'K' to 13, 'A' to 14)

val handComparator = object : Comparator<Hand> {
    override fun compare(h1: Hand, h2: Hand): Int {
        if (h1.typePower != h2.typePower) {
            return h1.typePower - h2.typePower
        }
        for ((c1, c2) in h1.hand.zip(h2.hand)) {
            if (cardMap.getOrDefault(c1, 0) - cardMap.getOrDefault(c2, 0) != 0) {
                return cardMap.getOrDefault(c1, 0) - cardMap.getOrDefault(c2, 0)
            } 
        } 
        return 0
    }
}
val handComparator2 = object : Comparator<Hand> {
    override fun compare(h1: Hand, h2: Hand): Int {
        if (h1.typePower2 != h2.typePower2) {
            return h1.typePower2 - h2.typePower2
        }
        for ((c1, c2) in h1.hand.zip(h2.hand)) {
            if (cardMap2.getOrDefault(c1, -1) - cardMap2.getOrDefault(c2, -1) != 0) {
                return cardMap2.getOrDefault(c1, -1) - cardMap2.getOrDefault(c2, -1)
            } 
        } 
        return 0
    }
}

fun main() {
    val hands: List<Hand> = File("input.txt").readLines().map { line -> Hand(line) }
    val sortedHands: List<Hand> = hands.sortedWith(handComparator)
    var silver = sortedHands.foldIndexed(0) {i, acc, hand -> acc + (i + 1) * hand.bid }
    val sortedHands2: List<Hand> = hands.sortedWith(handComparator2)
    var gold = sortedHands2.foldIndexed(0) {i, acc, hand -> acc + (i + 1) * hand.bid }
    println("Part 1: $silver")
    println("Part 2: $gold")
}
