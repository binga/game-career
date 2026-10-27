import json
W=['bear','elk','salmon','hawk','fox']; HB=['mountain','forest','prairie','wetland','river']
# player: (name, [b,e,s,h,f], W_written, [(corr,bonus)x5], H_written, nature, total_written, {raw overrides})
G=[]
def g(photo,pos,date_raw,iso,date_conf,players,notes=(),prefix=None):
    G.append(dict(photo=photo,pos=pos,date_raw=date_raw,iso=iso,date_conf=date_conf,players=players,notes=list(notes),prefix=prefix))
P=lambda *a,**k:(a,k)
g(1,'c1r1','10-1-2026','2026-01-10','clear',[
 P('Sh',[10,10,10,18,16],64,[(8,3),(4,0),(4,0),(5,0),(7,3)],34,0,98),
 P('Ph',[10,29,10,7,11],67,[(7,1),(5,1),(8,1),(3,0),(6,1)],33,2,102,raw={'total':'102 (written over another digit)'}),
 P('Ni',[10,2,15,23,11],61,[(3,0),(4,0),(9,3),(10,3),(5,0)],37,0,98,raw={'forest':'"6-2" i.e. 6 corrected to 4'}),
 P('Ac',[0,16,15,11,12],54,[(3,0),(6,3),(4,0),(5,0),(3,0)],24,0,78,raw={'forest':'"4+2" i.e. 4 corrected to 6'})])
g(1,'c1r2','6-7-2026','2026-07-06','likely (middle digit read as 7; could conceivably be 1)',[
 P('Si',[10,18,4,8,10],50,[(9,3),(8,3),(4,0),(3,0),(3,0)],33,1,84),
 P('Ni',[10,6,13,11,5],45,[(2,0),(5,0),(4,0),(10,3),(6,0)],30,1,76),
 P('Ph',[10,9,2,18,7],46,[(7,1),(7,1),(7,0),(4,0),(5,0)],32,2,80),
 P('Pr',[10,6,11,5,10],42,[(5,0),(4,0),(8,1),(5,0),(8,3)],34,0,76),
 P('Va',[10,6,11,11,10],48,[(5,0),(4,0),(9,3),(5,0),(6,0)],32,0,80,raw={'name':'5th player squeezed onto the pad\'s outer border; name read as "Va"'})])
g(1,'c1r3','19-10-2026','2026-10-19','clear',[
 P('Ph',[8,16,5,12,15],56,[(6,1),(9,3),(4,0),(4,1),(3,0)],31,0,87),
 P('Sh',[13,4,20,9,11],57,[(5,0),(5,0),(6,1),(10,3),(6,1)],37,2,96,raw={'fox':'"9+2"'}),
 P('Ni',[13,14,7,9,8],51,[(7,3),(6,1),(10,3),(3,0),(8,3)],44,0,95,raw={'name':'"Ni" with hearts drawn under it','elk':'"12 +2"'})])
g(1,'c1r4','30-8-2026','2026-08-30','clear',[
 P('Ph',[11,16,15,5,10],57,[(4,0),(6,0),(9,3),(2,0),(7,1)],32,0,89),
 P('Ri',[11,7,10,18,9],55,[(5,1),(7,1),(2,0),(6,0),(10,3)],35,0,90,raw={'total':'90 (overwritten/bolded)'}),
 P('Sh',[11,7,15,11,9],53,[(7,3),(8,3),(7,1),(9,3),(1,0)],42,2,97),
 P('Ni',[11,23,12,5,9],60,[(4,0),(6,0),(6,0),(7,1),(6,0)],30,1,91)])
g(1,'c1r5','1-7-2026','2026-07-01','likely (leading "1" is a long stroke touching the frame; a hidden first digit is possible)',[
 P('Ni',[10,23,8,16,5],62,[(4,0),(10,2),(9,3),(5,0),(6,1)],40,3,105,raw={'prairie':'"3+6" = 9'}),
 P('Su',[20,4,11,12,6],53,[(10,3),(2,0),(3,0),(7,1),(10,3)],39,0,92),
 P('Ph',[10,9,13,12,11],55,[(5,1),(10,2),(4,1),(10,3),(4,0)],40,0,95)])
g(1,'c1r6','20-05-2026','2026-05-20','uncertain (day could be 20 or 30)',[
 P('Sh',[13,2,25,12,9],61,[(6,0),(8,3),(3,0),(7,3),(6,0)],36,2,99),
 P('Ra',[10,18,14,0,12],54,[(2,0),(6,0),(8,2),(5,0),(6,0)],29,4,97,raw={'habitat_subtotal':'29 (first digit overwritten)'}),
 P('Ro',[2,20,4,28,4],58,[(7,1),(4,0),(8,2),(2,0),(4,0)],28,0,86),
 P('Ph',[18,12,8,12,4],54,[(8,3),(6,0),(5,0),(5,0),(9,3)],37,0,91,raw={'habitat_subtotal':'37 (first digit overwritten)'})])
g(1,'c2r1','22-6-2026','2026-06-22','likely (last digit of year partly hidden by frame edge)',[
 P('Si',[10,16,9,9,16],60,[(4,0),(8,3),(10,3),(6,0),(5,0)],39,0,99),
 P('Su',[10,14,17,16,7],64,[(4,0),(6,0),(5,0),(6,0),(3,0)],24,4,92),
 P('Ni',[20,7,17,16,0],60,[(7,2),(5,0),(4,0),(9,3),(5,0)],35,1,96),
 P('Ph',[20,10,9,16,7],62,[(7,2),(7,1),(8,1),(7,1),(7,3)],44,2,108)])
g(1,'c2r2','2?-12-2025',None,'uncertain (day 24 or 27; month 12, year 2025 fairly clear)',[
 P('Sh',[12,21,0,16,8],57,[(7,2),(6,1),(5,0),(3,0),(6,1)],31,0,88),
 P('Ph',[7,8,8,9,10],42,[(3,0),(7,3),(8,3),(7,3),(7,3)],44,2,88),
 P('Ni',[7,12,13,9,8],49,[(7,2),(4,0),(5,0),(3,0),(5,0)],26,0,75)],
 notes=['Sh and Ph tied on 88; Cascadia tiebreaker (most nature tokens) favours Ph (2 vs 0).'])
g(1,'c2r3','?9-12-202?',None,'uncertain (looks like 29-12-2025 but first digit of day and last digit of year are faint)',[
 P('Ni',[19,11,0,12,6],48,[(9,3),(3,1),(2,0),(11,3),(4,1)],37,2,87),
 P('Sh',[4,23,9,15,7],58,[(5,0),(2,0),(4,1),(7,1),(9,3)],32,4,94),
 P('Ph',[0,10,21,3,5],39,[(5,0),(8,3),(13,3),(2,0),(3,0)],40,0,79)])
g(1,'c2r4','28-12-2025','2025-12-28','clear',[
 P('Ni',[13,10,0,18,11],52,[(5,0),(7,3),(6,1),(6,0),(3,0)],31,2,85,raw={'river':'"4-1" = 3'}),
 P('Ma',[7,11,12,7,6],43,[(7,1),(4,1),(4,0),(6,0),(8,3)],34,2,79),
 P('Sh',[2,16,12,27,7],64,[(8,3),(3,0),(5,0),(7,3),(5,0)],34,0,98),
 P('Si',[18,11,15,7,9],60,[(3,0),(3,0),(9,3),(6,0),(6,1)],31,2,93)])
g(1,'c2r5','30-12-2025','2025-12-30','clear',[
 P('Ni',[19,8,10,3,12],52,[(4,0),(8,2),(8,2),(2,0),(6,1)],33,8,93,raw={'wetland':'"3-1" = 2'}),
 P('Ph',[11,20,15,3,6],55,[(6,2),(6,0),(6,0),(6,2),(6,1)],35,8,98)])
g(1,'c2r6','4-1-2026','2026-01-04','clear',[
 P('Ph',[18,7,10,21,11],67,[(7,1),(6,1),(5,0),(7,0),(6,0)],33,1,101,raw={'nature':'"2-1" = 1','total':'"102-1" = 101'}),
 P('Ni',[4,18,10,29,8],69,[(11,3),(3,0),(7,0),(3,0),(6,0)],33,0,102),
 P('Si',[4,10,10,11,12],47,[(3,0),(5,0),(8,3),(9,3),(7,3)],41,0,88),
 P('Ma',[18,4,12,13,8],55,[(5,0),(8,3),(7,0),(8,1),(4,0)],36,None,None,raw={'nature':'"4" with "-3" above and "+2" beside: 4-3+2 = 3, or 4+2 = 6','total':'final digit is overwritten: 94 or 97'})])
g(1,'c3r1','12-?-2026',None,'uncertain (day 12 clear; month digit faint, probably 2; year probably 2026)',[
 P('Ni',[5,13,12,25,10],65,[(4,0),(6,1),(9,3),(5,0),(2,0)],30,2,97),
 P('Sh',[12,11,12,11,11],57,[(5,1),(7,3),(7,1),(8,2),(5,1)],40,3,100),
 P('Ph',[10,11,6,13,11],51,[(8,3),(5,0),(5,0),(8,2),(7,3)],41,0,92)])
g(1,'c3r2','26-1-2026','2026-01-26','likely',[
 P('Ni',[10,10,10,25,5],60,[(7,3),(3,0),(3,0),(6,1),(8,1)],32,0,92),
 P('Ph',[10,28,10,9,10],67,[(6,0),(5,0),(8,1),(3,0),(10,3)],36,0,103),
 P('Sh',[20,6,15,0,19],60,[(6,0),(9,3),(9,3),(8,3),(1,0)],42,2,104),
 P('Si',[10,10,12,22,11],63,[(5,0),(7,1),(4,0),(4,0),(6,0)],27,0,90,raw={'hawk':'"22" written heavily over another number (subtotal 63 implies 20)'})])
g(1,'c3r3','29/12/2025','2025-12-29','clear',[
 P('Ph',[10,16,8,8,20],62,[(6,0),(10,3),(5,0),(6,0),(4,0)],34,4,100),
 P('Si',[10,18,8,8,8],52,[(6,0),(3,0),(5,0),(8,3),(8,3)],36,6,94),
 P('Sh',[10,2,14,11,13],50,[(3,0),(7,1),(7,3),(7,1),(6,0)],35,0,85),
 P('Ni',[10,9,14,14,10],57,[(7,3),(2,0),(6,1),(6,0),(7,1)],33,2,92)])
g(1,'c3r4','29/12/2025','2025-12-29','likely (day 29, could be 24)',[
 P('Ma',[4,5,11,12,8],40,[(3,0),(5,0),(8,1),(4,0),(3,0)],24,0,64),
 P('Sh',[11,13,2,9,16],51,[(5,0),(6,2),(2,0),(6,0),(6,1)],28,2,81),
 P('Ni',[11,15,2,9,10],47,[(2,0),(5,0),(9,3),(2,0),(7,3)],31,2,80,raw={'mountain':'"3-1" = 2'}),
 P('Ph',[4,9,9,12,8],42,[(7,2),(6,2),(3,0),(6,0),(4,0)],30,8,80),
 P('Si',[11,5,15,9,4],44,[(7,2),(4,0),(5,0),(10,3),(4,0)],35,6,85,raw={'name':'5th player written on the outer border as "S?"; Phani confirmed it is Si (Sindhu)'})])
g(2,'c1r1','?-1-2026',None,'uncertain (day is a single digit, 7 or 9; month 1; year mostly hidden, assumed 2026)',[
 P('Ph',[13,4,8,21,9],55,[(8,3),(3,0),(10,3),(4,0),(5,1)],37,3,95),
 P('Ni',[10,7,25,15,7],64,[(4,0),(9,3),(6,1),(7,1),(3,0)],34,1,99),
 P('Si',[18,12,2,18,7],57,[(7,1),(7,1),(2,0),(10,3),(6,3)],40,1,98)])
g(2,'c1r2','18-10-2026','2026-10-18','clear',[
 P('Sh',[10,13,12,16,5],56,[(5,1),(6,1),(6,0),(5,0),(8,1)],33,2,91),
 P('Ph',[10,14,10,12,7],53,[(6,3),(5,0),(8,3),(6,1),(9,3)],45,0,98,raw={'habitat_subtotal':'"45" with 5 underlined and a small "1" beside it','total':'"98" with 8 underlined and a small "1" beside it'}),
 P('Ni',[10,7,15,12,12],56,[(3,0),(7,3),(6,0),(7,3),(6,0)],35,1,92)])
g(2,'c1r3','21-10-2026','2026-10-21','likely',[
 P('Ni',[10,23,4,5,14],56,[(8,2),(6,1),(6,2),(4,0),(9,1)],39,0,95,raw={'name':'"Ni" with hearts','forest_bonus':'"0+1" = 1'}),
 P('Ph',[18,4,16,12,11],61,[(2,0),(6,1),(5,0),(10,2),(9,1)],36,0,97)])
g(2,'c1r4','29-08-2026','2026-08-29','clear',[
 P('Sh',[10,13,14,12,2],51,[(2,0),(11,3),(5,0),(13,3),(2,0)],39,1,91),
 P('Ph',[6,18,0,27,6],57,[(9,3),(6,0),(8,3),(3,0),(6,0)],38,3,98),
 P('Ni',[13,15,13,3,12],56,[(7,0),(8,1),(6,0),(5,1),(8,3)],39,0,95),
 P('Ri',[10,11,12,9,13],55,[(7,0),(5,0),(7,1),(4,0),(6,0)],30,3,88)])
g(2,'c1r5','27-6-2026','2026-06-27','likely (day 27; 29 possible)',[
 P('Ph',[18,9,8,18,5],58,[(9,3),(5,0),(7,1),(3,0),(10,3)],41,0,99),
 P('Ri',[5,18,16,7,6],52,[(6,0),(8,2),(2,0),(8,3),(6,1)],36,0,88),
 P('Su',[16,5,16,18,3],58,[(7,1),(4,0),(7,1),(7,1),(3,0)],31,0,89),
 P('Ni',[5,11,16,25,7],64,[(3,0),(8,2),(7,1),(4,0),(5,0)],30,3,97,raw={'habitat_subtotal':'written 32; corrected to the cell sum 30 (confirmed by Phani)','total':'written 99; corrected to 64+30+3 = 97 (confirmed by Phani)'})])
g(2,'c1r6','12-2-2026','2026-02-12','clear',[
 P('Sh',[13,2,18,9,10],52,[(6,1),(6,0),(7,3),(8,3),(6,1)],41,0,93),
 P('Ph',[13,7,10,25,4],59,[(8,3),(6,0),(5,1),(5,0),(2,0)],30,0,89),
 P('Ni',[13,9,16,15,5],58,[(2,0),(8,3),(2,0),(6,1),(11,3)],36,2,96,raw={'prairie':'"3-1" = 2'})])
g(2,'c2r1','27-06-2026','2026-06-27','likely (day 27; 29 possible; same date as photo 2 c1r5 but different scores)',[
 P('Su',[11,21,12,6,11],61,[(6,1),(4,0),(6,1),(4,0),(5,0)],27,3,91),
 P('Ni',[19,2,12,6,8],47,[(9,3),(3,0),(5,0),(6,1),(6,1)],34,2,83),
 P('Ph',[4,9,12,12,14],51,[(3,0),(7,2),(9,3),(7,3),(7,3)],44,1,96),
 P('Ri',[11,14,15,12,5],57,[(4,0),(7,2),(4,0),(4,0),(3,0)],24,1,82)])
g(2,'c2r2','2?-1?-2025',None,'uncertain (looks like 27-11-2025 or 27/29-12-2025; very faint)',[
 P('Sh',[10,10,17,5,8],50,[(4,0),(3,0),(6,2),(2,0),(7,3)],27,0,77),
 P('Ph',[10,7,17,16,9],59,[(5,3),(3,0),(6,2),(6,3),(4,1)],33,0,92),
 P('Ni',[10,13,9,9,13],54,[(4,0),(10,3),(2,0),(5,1),(3,0)],28,2,84)])
g(2,'c2r3','28-12-2025','2025-12-28','likely',[
 P('Sh',[10,13,0,20,5],48,[(9,3),(2,0),(3,0),(8,1),(4,0)],30,2,80),
 P('Ph',[10,6,15,12,8],51,[(4,0),(6,3),(7,2),(10,3),(6,3)],44,4,99),
 P('Ni',[10,13,15,9,7],54,[(5,1),(5,1),(7,2),(7,0),(5,1)],34,2,90)])
g(2,'c2r4','29|12|2025','2025-12-29','clear',[
 P('Ni',[11,18,12,11,6],58,[(6,1),(6,0),(5,1),(6,2),(6,1)],34,4,96),
 P('Ph',[11,14,16,9,4],54,[(8,3),(11,3),(2,0),(6,2),(4,0)],39,0,93),
 P('Sh',[11,7,8,7,19],52,[(3,0),(8,1),(11,3),(1,0),(9,3)],39,0,91)])
g(2,'c2r5','31-12-2025','2025-12-31','clear',[
 P('Ph',[10,4,17,12,9],52,[(7,2),(4,0),(7,2),(10,2),(5,0)],39,6,97),
 P('Ni',[20,6,12,12,6],56,[(5,0),(10,2),(4,0),(6,0),(9,2)],38,4,98)],
 notes=['First player column left blank; Ph and Ni are in columns 2-3.'],prefix='Yay!')
g(2,'c2r6','2-1-2026','2026-01-02','clear',[
 P('Ph',[4,12,0,9,16],41,[(9,3),(8,3),(5,0),(5,0),(7,0)],40,4,85),
 P('Ni',[19,8,10,9,10],56,[(5,0),(4,0),(6,3),(6,3),(8,3)],38,8,102,raw={'habitat_subtotal':'"8" written in the habitat-subtotal row','nature':'"38" written in the nature-token row; values appear swapped between the two rows (56+38+8=102)'})],
 notes=['First player column left blank.','Ni habitat subtotal and nature tokens appear written in each other\'s rows; recorded as H=38, nature=8 (cells sum to 38 and 56+38+8=102).','Two-player game but majority bonuses written as 3 (official 2-player rule is 2; other 2-player pads use 2).'])
g(2,'c3r1','0?-02-2026',None,'uncertain (looks like 08-02-2026 or 09-02-2026; faint)',[
 P('Si',[11,8,10,9,18],56,[(9,2),(8,3),(6,0),(3,0),(4,0)],35,2,93),
 P('Ni',[11,18,12,12,7],60,[(5,0),(7,0),(7,3),(3,0),(7,1)],33,1,94),
 P('Ph',[11,6,12,16,14],59,[(3,0),(7,0),(6,0),(7,3),(9,3)],38,1,98),
 P('Ma',[19,12,15,5,9],60,[(9,2),(5,0),(5,0),(5,1),(5,0)],32,1,93)])
g(2,'c3r2','10-1-2026','2026-01-10','clear (same date as photo 1 c1r1 but different scores)',[
 P('Ph',[4,28,9,6,11],58,[(2,0),(5,0),(9,3),(3,0),(10,3)],35,2,95),
 P('Ni',[19,6,16,12,8],61,[(5,0),(6,1),(8,1),(8,1),(2,0)],32,0,93),
 P('Ac',[4,8,13,6,11],42,[(9,3),(5,0),(4,0),(7,0),(7,1)],36,1,79),
 P('Sh',[19,0,10,15,9],53,[(6,1),(10,3),(5,0),(9,3),(5,0)],42,0,95)],
 notes=['Ph and Sh tied on 95; Cascadia tiebreaker (most nature tokens) favours Ph (2 vs 0).'],prefix='"Om!" (word before the date, partly legible)')
g(2,'c3r3','29-12-2025','2025-12-29','likely (day 29, could be 27)',[
 P('Ni',[10,14,15,6,10],55,[(7,3),(8,3),(8,0),(2,0),(3,0)],34,8,97,raw={'nature':'"12" overwritten with "8"'}),
 P('Ph',[7,24,15,0,10],56,[(6,1),(7,1),(9,3),(7,1),(4,1)],40,4,100,raw={'nature':'earlier digit overwritten with "4"'}),
 P('Sh',[4,4,10,12,12],42,[(1,0),(4,0),(8,0),(9,3),(9,3)],37,6,85,raw={'total':'"90" crossed out, "85" written above'})])
g(2,'c3r4','30-12-2025','2025-12-30','clear (same date as photo 1 c2r5 but different scores)',[
 P('Ni',[12,10,17,9,13],61,[(10,None),(5,2),(8,1),(5,0),(6,0)],38,4,103,raw={'mountain_bonus':'written "3" with a stray "1"/tick beside it; unclear. Subtotal 38 implies 1'}),
 P('Ph',[10,7,8,24,3],52,[(4,0),(2,0),(8,1),(10,2),(8,2)],37,2,91,raw={'mountain_bonus':'"1-1" = 0','forest_bonus':'"1-1" = 0'})])

g(3,'c1r1','25-10-2026','2026-10-25','clear',[
 P('Ph',[4,8,8,22,7],49,[(7,2),(7,2),(5,1),(7,0),(5,1)],37,0,86),
 P('Ni',[11,23,17,5,6],62,[(4,0),(4,0),(5,1),(9,2),(5,1)],28,1,91)],
 notes=['Single pad from the photo uploaded on 25 Oct 2026.'])

g(4,'c1r1','27-10-2026','2026-10-27','clear',[
 P('Ni',[18,13,10,9,4],54,[(6,0),(9,2),(6,1),(6,1),(8,2)],41,0,95),
 P('Ph',[8,9,15,6,9],47,[(9,2),(6,0),(6,1),(6,1),(5,0)],36,0,83)],
 notes=['Single pad from the photo uploaded on 27 Oct 2026.'])

out=[]
issues=[]
for i,gm in enumerate(G):
    gid=f"p{gm['photo']}-{gm['pos']}"
    players=[];unc=[]
    for (a,k) in gm['players']:
        name,wl,Ww,hab,Hw,N,T=a; raw=k.get('raw',{})
        wsum=sum(wl)
        hsum=None if any(b is None for _,b in hab) else sum(c+b for c,b in hab)
        p=dict(name=name,
          wildlife=dict(zip(W,wl)),
          habitats={h:dict(corridor=c,bonus=b) for h,(c,b) in zip(HB,hab)},
          wildlife_subtotal_written=Ww, wildlife_subtotal_computed=wsum,
          habitat_corridor_total=sum(c for c,_ in hab), habitat_bonus_total=None if hsum is None else sum(b for _,b in hab),
          habitat_subtotal_written=Hw, habitat_subtotal_computed=hsum,
          nature_tokens=N, total_written=T)
        if raw: p['as_written_notes']=raw
        chk=[]
        if wsum!=Ww: chk.append(f"wildlife categories sum to {wsum}, written subtotal {Ww}")
        if hsum is not None and hsum!=Hw: chk.append(f"habitat cells sum to {hsum}, written subtotal {Hw}")
        if N is not None and T is not None and Ww+Hw+N!=T: chk.append(f"written W {Ww} + H {Hw} + nature {N} = {Ww+Hw+N}, written total {T}")
        p['arithmetic_ok']=not chk
        if chk: p['arithmetic_issues']=chk; issues.append((gid,name,chk))
        players.append(p)
    tot={p['name']:p['total_written'] for p in players if p['total_written'] is not None}
    mx=max(tot.values()); winners=[n for n,v in tot.items() if v==mx]
    out.append(dict(id=gid,date=gm['iso'],date_raw=gm['date_raw'],date_confidence=gm['date_conf'],date_prefix_text=gm['prefix'],
        source_photo=['photo1.jpg (c1a15e34….jpg)','photo2.jpg (01M5SFKR….jpg)','photo upload 25 Oct 2026 (single pad)','photo upload 27 Oct 2026 (single pad)'][gm['photo']-1],
        grid_position=dict(col=int(gm['pos'][1]),row=int(gm['pos'][3]),note='position in the photo as taken (landscape, pads sideways): col 1 = leftmost column of pads, row 1 = top'),
        crop=f"crops/p{gm['photo']}_{gm['pos']}.jpg", num_players=len(players), players=players,
        winners_by_written_total=winners, notes=gm['notes']))
BG={'p1-c2r2':('2025-12-24','day could be 24 or 27'),'p1-c2r3':('2025-12-29','reads most like 29-12-2025'),'p1-c3r1':('2026-02-12','day 12 clear; month probably 2 (same 3 players also played on 12-2-2026, photo 2 c1r6)'),
 'p2-c1r1':('2026-01-07','single-digit day 7 or 9, January'),'p2-c2r2':('2025-12-27','could be 27-11-2025 or 27/29-12-2025'),'p2-c3r1':('2026-02-08','could be 08 or 09 Feb')}
for o in out:
    if o['date']: o['date_best_guess']=o['date']
    else:
        o['date_best_guess'],why=BG[o['id']]; o['date_best_guess_basis']=why
    ps=[p for p in o['players'] if p['total_written'] is not None]
    mx=max(p['total_written'] for p in ps); tied=[p for p in ps if p['total_written']==mx]
    if len(tied)>1:
        mt=max(p['nature_tokens'] for p in tied)
        o['winner_after_nature_token_tiebreak']=[p['name'] for p in tied if p['nature_tokens']==mt]
    else: o['winner_after_nature_token_tiebreak']=[tied[0]['name']]
    for p in o['players']:
        if p['nature_tokens'] is None or p['total_written'] is None or p['habitat_subtotal_computed'] is None:
            p['arithmetic_ok']=None
            p.setdefault('arithmetic_issues',[]).append('cell unreadable/ambiguous; see as_written_notes')
out.sort(key=lambda x:(x['date_best_guess'],x['id']))
for n,o in enumerate(out,1): o['game_no']=n
json.dump(dict(schema=dict(wildlife_order=W,habitat_order=HB,habitat_cell='each habitat cell is split diagonally: upper-left = largest-corridor score, lower-right = majority bonus',
   row_order_on_pad='name, bear, elk, salmon, hawk, fox, wildlife subtotal (W), mountain, forest, prairie, wetland, river, habitat subtotal (H), nature tokens (pinecone icon), total'),
   games=out),open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'games.json'),'w'),indent=1)
print(len(out))
for x in issues: print(x)
from collections import Counter
c=Counter(p['name'] for g in out for p in g['players']); print(c)
for g in out: print(g['game_no'],g['date_best_guess'],g['date_raw'],g['id'],', '.join(f"{p['name']} {p['total_written']}" for p in g['players']),'| win:',g['winners_by_written_total'],g['winner_after_nature_token_tiebreak'])
