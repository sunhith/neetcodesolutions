s += str(len(st))+'#'+st
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        ptr = 0
        res = []
        while ptr < len(s):
            ptr2 = ptr+1
            while s[ptr2]!='#':
                ptr2+=1
            l = int(s[ptr:ptr2])
            string = s[ptr2+1:ptr2+l+1]
            res.append(string)
            ptr = ptr2+l+1
        return res