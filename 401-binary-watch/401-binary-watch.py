class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(12):
            for m in range(60):
                if h.bit_count() + m.bit_count() == turnedOn:
                    if m < 10:
                        res.append(f"{h}:0{m}")
                    else:
                        res.append(f"{h}:{m}")
        return res            