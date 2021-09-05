import requests
URL = 'https://kr.whatismymmr.com/api/v1/summoner?name='

def Rank(search='hide on bush'):
    Read_Json = requests.get(f"{URL}{search}").json()
    _avg = Read_Json['ranked']['avg']
    _err = Read_Json['ranked']['err']
    _warn = Read_Json['ranked']['warn']
    _closestRank = Read_Json['ranked']['closestRank']
    _percentile = Read_Json['ranked']['percentile']
    if _avg == None:
        print(_avg, _err, _warn, _closestRank, _percentile)
        return '데이터가 충분하지 않습니다.', None
    if _percentile < 50:
        _percentile = '하위 ' + str(_percentile)
    else:
        _percentile = '상위 ' + str(_percentile)
    print(_avg, _err, _warn, _closestRank, _percentile)
    return (f'[MMR]\n{_avg}±{_err}\n\n{_closestRank}의 {_percentile}%의 소환사들과 비슷합니다.'), f'{_avg}±{_err}'

def Normal(search='hide on bush'):
    Read_Json = requests.get(f"{URL}{search}").json()
    _avg = Read_Json['normal']['avg']
    _err = Read_Json['normal']['err']
    _warn = Read_Json['normal']['warn']
    _closestRank = Read_Json['normal']['closestRank']
    _percentile = Read_Json['normal']['percentile']
    if _avg == None:
        print(_avg, _err, _warn, _closestRank, _percentile)
        return '데이터가 충분하지 않습니다.', None
    if _percentile < 50:
            _percentile = '하위 ' + str(_percentile)
    else:
        _percentile = '상위 ' + str(_percentile)
    __avg = f'{_avg}±{_err}'
    print(_avg, _err, _warn, _closestRank, _percentile)
    return f'[MMR]\n{_avg}±{_err}\n\n{_closestRank}의 {_percentile}%의 소환사들과 비슷합니다.', f'{_avg}±{_err}'

def ARAM(search='hide on bush'):
    Read_Json = requests.get(f"{URL}{search}").json()
    _avg = Read_Json['ARAM']['avg']
    _err = Read_Json['ARAM']['err']
    _warn = Read_Json['ARAM']['warn']
    _closestRank = Read_Json['ARAM']['closestRank']
    _percentile = Read_Json['ARAM']['percentile']
    if _avg == None:
        print(_avg, _err, _warn, _closestRank, _percentile)
        return '데이터가 충분하지 않습니다.', None
    if _percentile < 50:
            _percentile = '하위 ' + str(_percentile)
    else:
        _percentile = '상위 ' + str(_percentile)
    print(_avg, _err, _warn, _closestRank, _percentile)
    return (f'[MMR]\n{_avg}±{_err}\n\n{_closestRank}의 {_percentile}%의 소환사들과 비슷합니다.'), f'{_avg}±{_err}'
