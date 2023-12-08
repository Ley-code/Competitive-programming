class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        idxof1 = []
        result = [0]*len(boxes)
        for i in range(len(boxes)):
            if boxes[i] == "1":
                idxof1.append(i)
        for j in range(len(boxes)):
            for idx in idxof1:
                result[j] += abs(j-idx)
        return result