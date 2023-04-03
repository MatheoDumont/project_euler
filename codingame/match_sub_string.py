
def match(brin, sequence):
    idx_brin = 0
    idx_seq = 0
    def f(idx_brin, idx_seq):
        print(f"{idx_brin}, {idx_seq}")
        if idx_seq == len(sequence):
            return True, idx_brin-idx_seq
        elif idx_brin == len(brin):
            return False
        
        if sequence[idx_seq] == brin[idx_brin]:
            return f(idx_brin+1, idx_seq+1)
        else:
            return f(idx_brin+1, 0)

    return f(0, 0)


if __name__ == "__main__":
    brin = "AAGTAACTCAGCTCATATGGCGAGCAA"
    seq = "AACTC"

    print(match(brin, seq))
