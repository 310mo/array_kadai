import sys

def islms(t, i):
    if i>0 and t[i-1]=='L' and t[i]=='S':
        return True
    else:
        return False

def induced_sort(s, k, t, lmss):
    #print('k:')
    #print(k)
    #作業領域
    sa = [-1 for i in range(len(s))]

    #sは対象とする文字列、sに出現する文字種ごとのカウント
    bin = [0 for i in range(k)]
    for ss in s:
        #print(ss)
        ss_num = 0
        if type(ss) is str:
            ss_num = ord(ss)
        else:
            ss_num = ss
        #print(ss_num)
        bin[ss_num+1] += 1

    sum = 0
    c = 0
    for b in bin:
        if b==0:
            bin[c] = sum
        else:
            sum += b
            bin[c] = sum

        c += 1

    count = [0 for i in range(k)]
    #LMSのインデックスをビンの終わりの方から入れる
    for i in (reversed(lmss)):
        #ch = ord(s[i])
        ch = 0
        if type(ss) is str:
            ch = ord(s[i])
        else:
            ch = s[i]
        #chを入れるビンの終わり(bin[ch]-1)から詰めて入れる
        sa[bin[ch+1]-1-count[ch]] = i
        count[ch] += 1
    
    #saを昇順に走査
    count = [0 for i in range(k)]
    
    for i in sa:
        if i==-1:
            #まだ入っていない
            continue
        if i==0:
            #終端文字のとき
            continue
        if t[i-1]=='S':
            #L型のみが走査の対象なのでpass
            continue

        #saに入っているインデックスiについてi-1がL型であるとき、
        #文字列s[i-1]に対応するビンにi-1を頭から詰めて入れる
        #ch = ord(s[i-1])
        ch = 0
        if type(ss) is str:
            ch = ord(s[i-1])
        else:
            ch = s[i-1]
        sa[bin[ch]+count[ch]] = i-1 #LMSの部分を上書きする場合もある
        count[ch] += 1

    #saを逆順に走査
    count = [0 for i in range(k)]

    for i in (reversed(sa)):
        if i==-1:
            continue
        elif i==0:
            continue
        elif t[i-1]=='L':
            continue

        #saに入っているインデックスiについて、i-1がS型であるとき、
        #文字 s[i-1] に対応するビンに i-1 を終わりから詰めて入れる
        #ch = ord(s[i-1])
        ch = 0
        if type(ss) is str:
            ch = ord(s[i-1])
        else:
            ch = s[i-1]
        sa[bin[ch+1]-1-count[ch]] = i-1 #上書きすることもある
        count[ch] += 1
    #print(sa)
    
    return sa

def sa_is(s, k):
    #L型かS型か
    t = ['' for i in range(len(s))]

    #最後はS
    t[-1] = 'S'
    for i in reversed(range(0, len(s)-1)):
        if s[i] < s[i+1]:
            t[i] = 'S'
        elif s[i] > s[i+1]:
            t[i] = 'L'
        else:
            t[i] = t[i+1]
    #print(t)
    
    #LMSのインデックスだけを集めた配列
    lmss = []
    for i in range(len(s)):
        if islms(t, i):
            lmss.append(i)
    
    seed = lmss
    #print(seed)
    
    #1回目の induced sort
    sa = induced_sort(s, k, t, seed)

    #print(sa)

    
    #induced sort の結果から　LMS　の　suffix　だけ取り出す
    lms_suffix = []
    for i in range(len(sa)):
        if islms(t, sa[i]):
            lms_suffix.append(sa[i])
    #print('lms_suffix')
    #print(lms_suffix)
    
    #LMS のインデックス i に対して番号nums[i] を振る
    nums = [-1 for i in range(len(s))]

    #sa[0] の LMS は $ と決まっているので番号 0 を振っておく
    nums[sa[0]] = num = 0


    #隣り合う LMS を比べる
    for kk in range(len(lms_suffix)-1):
        i = lms_suffix[kk]
        j = lms_suffix[kk+1]

        diff = False
        #隣り合うLMS部分文字列の比較
        for d in range(len(s)):
            if s[i+d]!=s[j+d] or islms(t, i+d)!=islms(t, j+d):
                #LMS部分文字列の範囲で異なる文字列があった
                diff = True
                break
            elif d>0 and (islms(t, i+d) or islms(t, j+d)):
                #LMS部分文字列の終端に至った
                break

        #隣り合うLMS部分文字列が異なる場合は番号を増やす
        if diff:
            num += 1
        
        #LMSのインデックスjに番号numを振る
        nums[j] = num

    #numsの中に出現する番号のみを並べる
    nums_compact = []
    for n in nums:
        if n!=-1:
            nums_compact.append(n)

    #print(nums_compact)

    if num+1 < len(nums_compact):
        #番号の重複があるので再帰
        sa = sa_is(nums_compact, num+2)
    else:
        #番号の重複がない場合、suffix arrayを容易に求めることができる
        sa = [0 for i in range(len(nums_compact))]
        for i in range(len(nums_compact)):
            sa[nums_compact[i]] = i

    #print(sa)

    seed = []
    for i in sa:
        seed.append(lmss[i])
    
    #print(lmss)
    #print('seed:')
    #print(seed)

    sa = induced_sort(s, k, t, seed)

    return sa





f = open(sys.argv[1])
s = f.read() + '$'
#print(s)

k = 300
print(sa_is(s, k))  



