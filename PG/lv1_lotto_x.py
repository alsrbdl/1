def solution(lottos, win_nums):
    zero=lottos.count(0)
    correct=len(set(win_nums) & set(lottos))
    high_rank=7-zero-correct
    low_rank=7-correct
    if (low_rank>=7):
        low_rank=6
    answer = [high_rank, low_rank]
    return answer