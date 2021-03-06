from modules import scratchtools

followers = scratchtools.getfollowercount

print('Getting previous follower count...')
with open('previousfollowers.txt') as f:
    previous = f.read().splitlines()

print()
print('Getting follower count...')

followerList = list()
users = ['griffpatch', 'Will_Wam', 'WazzoTV', 'ceebee', 'griffpatch_tutor', 'Hobson-TV', 'Dhilly', 'ScratchCat', '-BoyMcBoy-', 'FunnyAnimatorJimTV', 'DerpAnimation', 'theChAOTiC', 'atomicmagicnumber', 'Scratchteam', 'ipzy', 'huntedskelly', 'sharkyshar', 'Rosyda', 'yunnie2005', 'kevin_eleven_1234']

followerList.append({'followers': followers('griffpatch').followercount, 'previous': previous[0], 'name': 'griffpatch'})
print()
print('1...')
followerList.append({'followers': followers('Will_Wam').followercount, 'previous': previous[1], 'name': 'Will_Wam'})
print('2...')
followerList.append({'followers': followers('WazzoTV').followercount, 'previous': previous[2], 'name': 'WazzoTV'})
print('3...')
followerList.append({'followers': followers('ceebee').followercount, 'previous': previous[3], 'name': 'ceebee'})
print('4...')
followerList.append({'followers': followers('griffpatch_tutor').followercount, 'previous': previous[4], 'name': 'griffpatch_tutor'})
print('5...')
followerList.append({'followers': followers('Hobson-TV').followercount, 'previous': previous[5], 'name': 'Hobson-TV'})
print('6...')
followerList.append({'followers': followers('Dhilly').followercount, 'previous': previous[6], 'name': 'Dhilly'})
print('7...')
followerList.append({'followers': followers('ScratchCat').followercount, 'previous': previous[7], 'name': 'ScratchCat'})
print('8...')
followerList.append({'followers': followers('-BoyMcBoy-').followercount, 'previous': previous[8], 'name': '-BoyMcBoy-'})
print('9...')
followerList.append({'followers': followers('FunnyAnimatorJimTV').followercount, 'previous': previous[9], 'name': 'FunnyAnimatorJimTV'})
print('10...')
followerList.append({'followers': followers('DerpAnimation').followercount, 'previous': previous[10], 'name': 'DerpAnimation'})
print('11...')
followerList.append({'followers': followers('theChAOTiC').followercount, 'previous': previous[11], 'name': 'theChAOTiC'})
print('12...')
followerList.append({'followers': followers('atomicmagicnumber').followercount, 'previous': previous[12], 'name': 'atomicmagicnumber'})
print('13...')
followerList.append({'followers': followers('Scratchteam').followercount, 'previous': previous[13], 'name': 'Scratchteam'})
print('14...')
followerList.append({'followers': followers('ipzy').followercount, 'previous': previous[14], 'name': 'ipzy'})
print('15...')
followerList.append({'followers': followers('huntedskelly').followercount, 'previous': previous[15], 'name': 'huntedskelly'})
print('16...')
followerList.append({'followers': followers('sharkyshar').followercount, 'previous': previous[16], 'name': 'sharkyshar'})
print('17...')
followerList.append({'followers': followers('Rosyda').followercount, 'previous': previous[17], 'name': 'Rosyda'})
print('18...')
followerList.append({'followers': followers('yunnie2005').followercount, 'previous': previous[18], 'name': 'yunnie2005'})
print('19...')
followerList.append({'followers': followers('kevin_eleven_1234').followercount, 'previous': previous[19], 'name': 'kevin_eleven_1234'})
print('20!')
print()

print('Sorting...')
def srt(e):
    return e['followers']

followerList.sort(key=srt, reverse=True)

print()
print('Saving...')

with open('previousfollowers.txt', 'w') as f:
    for item in followerList:
        f.write("%s\n" % item)

print()
print('Doing math...')
increase = list()
increase.append(followerList[0]['followers'] - int(followerList[0]['previous']))
increase.append(followerList[1]['followers'] - int(followerList[1]['previous']))
increase.append(followerList[2]['followers'] - int(followerList[2]['previous']))
increase.append(followerList[3]['followers'] - int(followerList[3]['previous']))
increase.append(followerList[4]['followers'] - int(followerList[4]['previous']))
increase.append(followerList[5]['followers'] - int(followerList[5]['previous']))
increase.append(followerList[6]['followers'] - int(followerList[6]['previous']))
increase.append(followerList[7]['followers'] - int(followerList[7]['previous']))
increase.append(followerList[8]['followers'] - int(followerList[8]['previous']))
increase.append(followerList[9]['followers'] - int(followerList[9]['previous']))
increase.append(followerList[10]['followers'] - int(followerList[10]['previous']))
increase.append(followerList[11]['followers'] - int(followerList[11]['previous']))
increase.append(followerList[12]['followers'] - int(followerList[12]['previous']))
increase.append(followerList[13]['followers'] - int(followerList[13]['previous']))
increase.append(followerList[14]['followers'] - int(followerList[14]['previous']))
increase.append(followerList[15]['followers'] - int(followerList[15]['previous']))
increase.append(followerList[16]['followers'] - int(followerList[16]['previous']))
increase.append(followerList[17]['followers'] - int(followerList[17]['previous']))
increase.append(followerList[18]['followers'] - int(followerList[18]['previous']))
increase.append(followerList[19]['followers'] - int(followerList[19]['previous']))

posiNegi = list()
for item in increase:
    if item >= 0:
        posiNegi.append('+')
    else:
        posiNegi.append('')

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
article.append('|{:,d}'.format(int(followerList[0]['previous'])))
article.append('|{:,d}'.format(followerList[0]['followers']))
article.append('|<nowiki>' + posiNegi[0] + '{:,d}</nowiki>'.format(increase[0]))
article.append('|-')
article.append('|2')
article.append('|Will_Wam')
article.append('|')
article.append('|{:,d}'.format(int(followerList[1]['previous'])))
article.append('|{:,d}'.format(followerList[1]['followers']))
article.append('|<nowiki>' + posiNegi[1] + '{:,d}</nowiki>'.format(increase[1]))
article.append('|-')
article.append('|3')
article.append('|WazzoTV')
article.append('|')
article.append('|{:,d}'.format(int(followerList[2]['previous'])))
article.append('|{:,d}'.format(followerList[2]['followers']))
article.append('|<nowiki>' + posiNegi[2] + '{:,d}</nowiki>'.format(increase[2]))
article.append('|-')
article.append('|4')
article.append('|ceebee (Scratch team)')
article.append('|')
article.append('|{:,d}'.format(int(followerList[3]['previous'])))
article.append('|{:,d}'.format(followerList[3]['followers']))
article.append('|<nowiki>' + posiNegi[3] + '{:,d}</nowiki>'.format(increase[3]))
article.append('|-')
article.append('|5')
article.append('|griffpatch_tutor')
article.append('|')
article.append('|{:,d}'.format(int(followerList[4]['previous'])))
article.append('|{:,d}'.format(followerList[4]['followers']))
article.append('|<nowiki>' + posiNegi[4] + '{:,d}</nowiki>'.format(increase[4]))
article.append('|-')
article.append('|6')
article.append('|Hobson-TV')
article.append('|')
article.append('|{:,d}'.format(int(followerList[5]['previous'])))
article.append('|{:,d}'.format(followerList[5]['followers']))
article.append('|<nowiki>' + posiNegi[5] + '{:,d}</nowiki>'.format(increase[5]))
article.append('|-')
article.append('|7')
article.append('|Dhilly')
article.append('|')
article.append('|{:,d}'.format(int(followerList[6]['previous'])))
article.append('|{:,d}'.format(followerList[6]['followers']))
article.append('|<nowiki>' + posiNegi[6] + '{:,d}</nowiki>'.format(increase[6]))
article.append('|-')
article.append('|8')
article.append('|ScratchCat (Scratch team)')
article.append('|')
article.append('|{:,d}'.format(int(followerList[7]['previous'])))
article.append('|{:,d}'.format(followerList[7]['followers']))
article.append('|<nowiki>' + posiNegi[7] + '{:,d}</nowiki>'.format(increase[7]))
article.append('|-')
article.append('|9')
article.append('|<nowiki>-BoyMcBoy-</nowiki>')
article.append('|')
article.append('|{:,d}'.format(int(followerList[8]['previous'])))
article.append('|{:,d}'.format(followerList[8]['followers']))
article.append('|<nowiki>' + posiNegi[8] + '{:,d}</nowiki>'.format(increase[8]))
article.append('|-')
article.append('|10')
article.append('|FunnyAnimatorJimTV')
article.append('|')
article.append('|{:,d}'.format(int(followerList[9]['previous'])))
article.append('|{:,d}'.format(followerList[9]['followers']))
article.append('|<nowiki>' + posiNegi[9] + '{:,d}</nowiki>'.format(increase[9]))
article.append('|-')
article.append('|11')
article.append('|DerpAnimation')
article.append('|')
article.append('|{:,d}'.format(int(followerList[10]['previous'])))
article.append('|{:,d}'.format(followerList[10]['followers']))
article.append('|<nowiki>' + posiNegi[10] + '{:,d}</nowiki>'.format(increase[10]))
article.append('|-')
article.append('|12')
article.append('|theChAOTiC')
article.append('|')
article.append('|{:,d}'.format(int(followerList[11]['previous'])))
article.append('|{:,d}'.format(followerList[11]['followers']))
article.append('|<nowiki>' + posiNegi[11] + '{:,d}</nowiki>'.format(increase[11]))
article.append('|-')
article.append('|13')
article.append('|atomicmagicnumber')
article.append('|')
article.append('|{:,d}'.format(int(followerList[12]['previous'])))
article.append('|{:,d}'.format(followerList[12]['followers']))
article.append('|<nowiki>' + posiNegi[12] + '{:,d}</nowiki>'.format(increase[12]))
article.append('|-')
article.append('|14')
article.append('|Scratchteam (Scratch team)')
article.append('|')
article.append('|{:,d}'.format(int(followerList[13]['previous'])))
article.append('|{:,d}'.format(followerList[13]['followers']))
article.append('|<nowiki>' + posiNegi[13] + '{:,d}</nowiki>'.format(increase[13]))
article.append('|-')
article.append('|15')
article.append('|ipzy (new Scratch team)')
article.append('|')
article.append('|{:,d}'.format(int(followerList[14]['previous'])))
article.append('|{:,d}'.format(followerList[14]['followers']))
article.append('|<nowiki>' + posiNegi[14] + '{:,d}</nowiki>'.format(increase[14]))
article.append('|-')
article.append('|16')
article.append('|huntedskelly')
article.append('|')
article.append('|{:,d}'.format(int(followerList[15]['previous'])))
article.append('|{:,d}'.format(followerList[15]['followers']))
article.append('|<nowiki>' + posiNegi[15] + '{:,d}</nowiki>'.format(increase[15]))
article.append('|-')
article.append('|17')
article.append('|sharkyshar')
article.append('|')
article.append('|{:,d}'.format(int(followerList[16]['previous'])))
article.append('|{:,d}'.format(followerList[16]['followers']))
article.append('|<nowiki>' + posiNegi[16] + '{:,d}</nowiki>'.format(increase[16]))
article.append('|-')
article.append('|18')
article.append('|Rosyda')
article.append('|')
article.append('|{:,d}'.format(int(followerList[17]['previous'])))
article.append('|{:,d}'.format(followerList[17]['followers']))
article.append('|<nowiki>' + posiNegi[17] + '{:,d}</nowiki>'.format(increase[17]))
article.append('|-')
article.append('|19')
article.append('|yunnie2005')
article.append('|')
article.append('|{:,d}'.format(int(followerList[18]['previous'])))
article.append('|{:,d}'.format(followerList[18]['followers']))
article.append('|<nowiki>' + posiNegi[18] + '{:,d}</nowiki>'.format(increase[18]))
article.append('|-')
article.append('|20')
article.append('|kevin_eleven_1234')
article.append('|')
article.append('|{:,d}'.format(int(followerList[19]['previous'])))
article.append('|{:,d}'.format(followerList[19]['followers']))
article.append('|<nowiki>' + posiNegi[19] + '{:,d}</nowiki>'.format(increase[19]))

article.append('|}[[Category:The only page]]')

print('Saving...')

with open('article.txt', 'w') as f:
    for item in article:
        f.write("%s\n" % item)

print('Done!')
