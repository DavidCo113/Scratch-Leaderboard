from modules import scratchtools

followers = scratchtools.getfollowercount

print('Getting follower count...')

followerList = list()

followerList.append(followers('griffpatch').followercount)
print()
print('1...')
followerList.append(followers('Will_Wam').followercount)
print('2...')
followerList.append(followers('WazzoTV').followercount)
print('3...')
followerList.append(followers('ceebee').followercount)
print('4...')
followerList.append(followers('griffpatch_tutor').followercount)
print('5...')
followerList.append(followers('Hobson-TV').followercount)
print('6...')
followerList.append(followers('Dhilly').followercount)
print('7...')
followerList.append(followers('ScratchCat').followercount)
print('8...')
followerList.append(followers('-BoyMcBoy-').followercount)
print('9...')
followerList.append(followers('FunnyAnimatorJimTV').followercount)
print('10...')
followerList.append(followers('DerpAnimation').followercount)
print('11...')
followerList.append(followers('theChAOTiC').followercount)
print('12...')
followerList.append(followers('atomicmagicnumber').followercount)
print('13...')
followerList.append(followers('Scratchteam').followercount)
print('14...')
followerList.append(followers('ipzy').followercount)
print('15...')
followerList.append(followers('huntedskelly').followercount)
print('16...')
followerList.append(followers('Rosyda').followercount)
print('17...')
followerList.append(followers('yunnie2005').followercount)
print('18...')
followerList.append(followers('kevin_eleven_1234').followercount)
print('19...')
followerList.append(followers('TNTsquirrel').followercount)
print('20!')

print()
print('Getting previous follower count...')
with open('previousfollowers.txt') as f:
    previous = f.read().splitlines()

print()
print('Saving...')

with open('previousfollowers.txt', 'w') as f:
    for item in followerList:
        f.write("%s\n" % item)

print()
print('Doing math...')
increase = list()
increase.append(followerList[0] - int(previous[0]))
increase.append(followerList[1] - int(previous[1]))
increase.append(followerList[2] - int(previous[2]))
increase.append(followerList[3] - int(previous[3]))
increase.append(followerList[4] - int(previous[4]))
increase.append(followerList[5] - int(previous[5]))
increase.append(followerList[6] - int(previous[6]))
increase.append(followerList[7] - int(previous[7]))
increase.append(followerList[8] - int(previous[8]))
increase.append(followerList[9] - int(previous[9]))
increase.append(followerList[10] - int(previous[10]))
increase.append(followerList[11] - int(previous[11]))
increase.append(followerList[12] - int(previous[12]))
increase.append(followerList[13] - int(previous[13]))
increase.append(followerList[14] - int(previous[14]))
increase.append(followerList[15] - int(previous[15]))
increase.append(followerList[16] - int(previous[16]))
increase.append(followerList[17] - int(previous[17]))
increase.append(followerList[18] - int(previous[18]))
increase.append(followerList[19] - int(previous[19]))

posiNegi = list()
for item in increase:
    if item >= 0:
        posiNegi.append('+')
    else:
        posiNegi.append('-')

print('Generating wiki article...')

article = list()

article.append('== <nowiki/> ==')
article.append('{| class="article-table"')
article.append('!Rank')
article.append('!User')
article.append('!')
article.append('!Past Followers')
article.append('!Current Followers')
article.append('!Follower Increase')
article.append('|-')
article.append('|1')
article.append('|griffpatch')
article.append('|')
article.append('|{:,d}'.format(int(previous[0])))
article.append('|{:,d}'.format(followerList[0]))
article.append('|<nowiki>' + posiNegi[0] + '{:,d}</nowiki>'.format(increase[0]))
article.append('|-')
article.append('|2')
article.append('|Will_Wam')
article.append('|')
article.append('|{:,d}'.format(int(previous[1])))
article.append('|{:,d}'.format(followerList[1]))
article.append('|<nowiki>' + posiNegi[1] + '{:,d}</nowiki>'.format(increase[1]))
article.append('|-')
article.append('|3')
article.append('|WazzoTV')
article.append('|')
article.append('|{:,d}'.format(int(previous[2])))
article.append('|{:,d}'.format(followerList[2]))
article.append('|<nowiki>' + posiNegi[2] + '{:,d}</nowiki>'.format(increase[2]))
article.append('|-')
article.append('|4')
article.append('|ceebee (Scratch team)')
article.append('|')
article.append('|{:,d}'.format(int(previous[3])))
article.append('|{:,d}'.format(followerList[3]))
article.append('|<nowiki>' + posiNegi[3] + '{:,d}</nowiki>'.format(increase[3]))
article.append('|-')
article.append('|5')
article.append('|griffpatch_tutor')
article.append('|')
article.append('|{:,d}'.format(int(previous[4])))
article.append('|{:,d}'.format(followerList[4]))
article.append('|<nowiki>' + posiNegi[4] + '{:,d}</nowiki>'.format(increase[4]))
article.append('|-')
article.append('|6')
article.append('|Hobson-TV')
article.append('|')
article.append('|{:,d}'.format(int(previous[5])))
article.append('|{:,d}'.format(followerList[5]))
article.append('|<nowiki>' + posiNegi[5] + '{:,d}</nowiki>'.format(increase[5]))
article.append('|-')
article.append('|7')
article.append('|Dhilly')
article.append('|')
article.append('|{:,d}'.format(int(previous[6])))
article.append('|{:,d}'.format(followerList[6]))
article.append('|<nowiki>' + posiNegi[6] + '{:,d}</nowiki>'.format(increase[6]))
article.append('|-')
article.append('|8')
article.append('|ScratchCat (Scratch team)')
article.append('|')
article.append('|{:,d}'.format(int(previous[7])))
article.append('|{:,d}'.format(followerList[7]))
article.append('|<nowiki>' + posiNegi[7] + '{:,d}</nowiki>'.format(increase[7]))
article.append('|-')
article.append('|9')
article.append('|<nowiki>-BoyMcBoy-</nowiki>')
article.append('|')
article.append('|{:,d}'.format(int(previous[8])))
article.append('|{:,d}'.format(followerList[8]))
article.append('|<nowiki>' + posiNegi[8] + '{:,d}</nowiki>'.format(increase[8]))
article.append('|-')
article.append('|10')
article.append('|FunnyAnimatorJimTV')
article.append('|')
article.append('|{:,d}'.format(int(previous[9])))
article.append('|{:,d}'.format(followerList[9]))
article.append('|<nowiki>' + posiNegi[9] + '{:,d}</nowiki>'.format(increase[9]))
article.append('|-')
article.append('|11')
article.append('|DerpAnimation')
article.append('|')
article.append('|{:,d}'.format(int(previous[10])))
article.append('|{:,d}'.format(followerList[10]))
article.append('|<nowiki>' + posiNegi[10] + '{:,d}</nowiki>'.format(increase[10]))
article.append('|-')
article.append('|12')
article.append('|theChAOTiC')
article.append('|')
article.append('|{:,d}'.format(int(previous[11])))
article.append('|{:,d}'.format(followerList[11]))
article.append('|<nowiki>' + posiNegi[11] + '{:,d}</nowiki>'.format(increase[11]))
article.append('|-')
article.append('|13')
article.append('|atomicmagicnumber')
article.append('|')
article.append('|{:,d}'.format(int(previous[12])))
article.append('|{:,d}'.format(followerList[12]))
article.append('|<nowiki>' + posiNegi[12] + '{:,d}</nowiki>'.format(increase[12]))
article.append('|-')
article.append('|14')
article.append('|Scratchteam (Scratch team)')
article.append('|')
article.append('|{:,d}'.format(int(previous[13])))
article.append('|{:,d}'.format(followerList[13]))
article.append('|<nowiki>' + posiNegi[13] + '{:,d}</nowiki>'.format(increase[13]))
article.append('|-')
article.append('|15')
article.append('|ipzy (new Scratch team)')
article.append('|')
article.append('|{:,d}'.format(int(previous[14])))
article.append('|{:,d}'.format(followerList[14]))
article.append('|<nowiki>' + posiNegi[14] + '{:,d}</nowiki>'.format(increase[14]))
article.append('|-')
article.append('|16')
article.append('|huntedskelly')
article.append('|')
article.append('|{:,d}'.format(int(previous[15])))
article.append('|{:,d}'.format(followerList[15]))
article.append('|<nowiki>' + posiNegi[15] + '{:,d}</nowiki>'.format(increase[15]))
article.append('|-')
article.append('|17')
article.append('|Rosyda')
article.append('|')
article.append('|{:,d}'.format(int(previous[16])))
article.append('|{:,d}'.format(followerList[16]))
article.append('|<nowiki>' + posiNegi[16] + '{:,d}</nowiki>'.format(increase[16]))
article.append('|-')
article.append('|18')
article.append('|yunnie2005')
article.append('|')
article.append('|{:,d}'.format(int(previous[17])))
article.append('|{:,d}'.format(followerList[17]))
article.append('|<nowiki>' + posiNegi[17] + '{:,d}</nowiki>'.format(increase[17]))
article.append('|-')
article.append('|19')
article.append('|kevin_eleven_1234')
article.append('|')
article.append('|{:,d}'.format(int(previous[18])))
article.append('|{:,d}'.format(followerList[18]))
article.append('|<nowiki>' + posiNegi[18] + '{:,d}</nowiki>'.format(increase[18]))
article.append('|-')
article.append('|20')
article.append('|TNTsquirrel')
article.append('|')
article.append('|{:,d}'.format(int(previous[19])))
article.append('|{:,d}'.format(followerList[19]))
article.append('|<nowiki>' + posiNegi[19] + '{:,d}</nowiki>'.format(increase[19]))
article.append('|}[[Category:The only page]]')

print('Saving...')

with open('article.txt', 'w') as f:
    for item in article:
        f.write("%s\n" % item)

print('Done!')