class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []

        output = [pairs.copy()]

        for j in range(1, len(pairs)):
            i = j - 1

            while i >= 0 and pairs[i].key > pairs[i + 1].key:
                pairs[i], pairs[i + 1] = pairs[i + 1], pairs[i]
                i -= 1

            output.append(pairs.copy())

        return output