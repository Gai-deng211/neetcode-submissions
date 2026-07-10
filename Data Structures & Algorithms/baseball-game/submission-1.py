class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for op in operations:
            if op.lstrip("-").isdigit():
                records.append(int(op))
            elif op == "+":
                records.append(records[-2] + records[-1])
            elif op == "D":
                records.append(records[-1] * 2)
            elif op == "C":
                records.pop()
        return sum(records)
                
