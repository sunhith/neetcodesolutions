res[i] = prod[i-1]
            else:
                res[i] = prod[i-1]*rev_prod[i+1]

        return res