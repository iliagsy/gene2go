# coding: utf-8
from utils import *

def cut(gaf):
    # gene association file
    newdata = []
    with open(gaf) as fh:
        for line in fh.readlines():
            if line.startswith('!'): continue
            fds = line.split('\t')
            ec = trans_ec(fds[6])
            if ec == '0': continue
            # newdata.append((fds[2].upper(), fds[4], trans_ec(fds[6])))
            newdata.append((fds[2].upper(), fds[4], ec))
    nmset = set([e[0] for e in newdata])
    for sp_ in ('fly', 'human', 'worm'):
        try:
            gaf.index(sp_)
            sp = sp_
            break
        except:
            pass
    nmf = '../name_{}.csv'.format(sp)
    with open(nmf) as fh:
        nmlstmy = [l.strip().upper() for l in fh.readlines()]
        nmsetmy = set(nmlstmy)
    print len(nmset & nmsetmy), len(nmsetmy)
    golstmy = []
    for l in newdata:
        if l[0] not in nmsetmy: continue
        golstmy.append(l)
    if sp == 'human':
        golstmy = tran_human(golstmy)
    with open('../links/links_{}.txt'.format(sp), 'w') as fh:
        try:
            fh.writelines(['\t'.join(t)+'\n' for t in golstmy])
        except:
            print sp; exit()
    return golstmy


def tran_human(golstmy):
    dct = {}
    with open('../human/LB-human-gene-name-mapping-mart_export-2.txt') as fh:
        for l in fh.readlines():
            t = l.strip().split(',')
            dct[t[1].upper()] = t[0]
    res = []
    for e in golstmy:
        nm = e[0]
        go = list(e[1:])
        res_e = tuple([dct[nm]] + go)
        res.append(res_e)
    return res


if __name__ == '__main__':
    cut('../worm/LB-worm-gene_association.WS220.wb.txt')
    cut('../fly/LB-flybase-5.45-gene_association.fb.txt')
    cut('../human/goa_human.gaf')
