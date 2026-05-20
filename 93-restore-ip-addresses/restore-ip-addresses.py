class Solution:
    def restoreIpAddresses(self, s: str):
        res = []
        
        def backtrack(start, path):
            # if 4 parts formed
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return
            
            # try segment lengths 1 to 3
            for l in range(1, 4):
                if start + l > len(s):
                    break
                
                part = s[start:start + l]
                
                # skip leading zero cases
                if part[0] == "0" and l > 1:
                    continue
                
                # check valid range
                if int(part) <= 255:
                    path.append(part)
                    backtrack(start + l, path)
                    path.pop()
        
        backtrack(0, [])
        return res