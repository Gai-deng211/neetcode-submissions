class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for op in operations:
            if op.lstrip("-").isdigit():
                records.append(int(op))
            elif op == "+" and len(records) > 1:
                records.append(records[-2] + records[-1])
            elif op == "D" and records:
                records.append(records[-1] * 2)
            elif op == "C" and records:
                records.pop()
        return sum(records)
                
