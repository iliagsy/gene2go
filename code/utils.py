from consts import *

def trans_ec(EC):
    if EC in Unrl_ecs:
        return '0'
    if EC in Exp_ecs:
        return 'experiment_evidence'
    if EC in Cmp_ecs:
        return 'computational_analysis'
    if EC in Nr_ecs:  # not reviewed
        return 'not_reviewed'
    return 'other_reviewed'
