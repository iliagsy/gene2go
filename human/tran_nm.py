def trans_nm():
    nmdct = dict()
    with open('LB-human-gene-name-mapping-mart_export-2.txt') as fh:
        for l in fh.readlines():
            t = l.strip().split(',')
            nmdct[t[0]] = t[1]
    nmlstold = []
    with open('../name_human_old.csv') as fh:
        nmlstold = [l.strip() for l in fh.readlines()]
    nmlstnew = []
    for gn in nmlstold:
        try:
            nmlstnew.append(nmdct[gn])
        except:
            pass
    with open('../name_human.csv', 'w') as fh:
        fh.writelines([nm+'\n' for nm in nmlstnew])


if __name__ == '__main__':
    trans_nm()
