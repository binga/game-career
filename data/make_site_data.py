#!/usr/bin/env python3
"""Build site/data.js + site/data.json from games.json and players.json.
Every number on the site comes from here. Re-run after any correction:
    python3 make_site_data.py
"""
import json, math, os, statistics as st
from collections import defaultdict
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = json.load(open(os.path.join(HERE, 'games.json')))
NAMES = {k: v for k, v in json.load(open(os.path.join(HERE, 'players.json'))).items() if not k.startswith('_')}
W = SRC['schema']['wildlife_order']
H = SRC['schema']['habitat_order']
MAIN_MIN_GAMES = 5  # players with at least this many games get a trend label

def mean(xs):
    xs = [x for x in xs if x is not None]
    return round(sum(xs) / len(xs), 2) if xs else None

def r2(x):
    return None if x is None else round(x, 2)

def linfit(ys):
    n = len(ys)
    xs = list(range(1, n + 1))
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx
    return slope, my - slope * mx

def pearson(a, b):
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    sa = math.sqrt(sum((x - ma) ** 2 for x in a)); sb = math.sqrt(sum((y - mb) ** 2 for y in b))
    if sa == 0 or sb == 0:
        return None
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / (sa * sb)

def hab_score(p, h):
    c = p['habitats'][h]
    if c['corridor'] is None or c['bonus'] is None:
        return None
    return c['corridor'] + c['bonus']

def date_uncertain(g):
    return g['date'] is None or (g.get('date_confidence') or '').lower().startswith('uncertain')

# ---------- games ----------
games = []
for g in sorted(SRC['games'], key=lambda g: g['game_no']):
    winners = g['winner_after_nature_token_tiebreak']
    scored = [p for p in g['players'] if p['total_written'] is not None]
    # finish order: total desc, then nature tokens desc (official tiebreak)
    order = sorted(scored, key=lambda p: (-p['total_written'], -(p['nature_tokens'] or 0)))
    pos = {}
    for i, p in enumerate(order):
        key = (p['total_written'], p['nature_tokens'] or 0)
        prev = order[i - 1] if i else None
        if prev and (prev['total_written'], prev['nature_tokens'] or 0) == key:
            pos[p['name']] = pos[prev['name']]
        else:
            pos[p['name']] = i + 1
    # JSON winner field is authoritative for 1st place
    for w in winners:
        pos[w] = 1
    rows = []
    for p in g['players']:
        t = p['total_written']
        others = [q['total_written'] for q in scored if q['name'] != p['name']]
        rows.append({
            'id': p['name'],
            'total': t,
            'pos': pos.get(p['name']),
            'win': p['name'] in winners,
            'margin': (t - max(others)) if (t is not None and others) else None,
            'wildlife': {k: p['wildlife'][k] for k in W},
            'habitats': {h: {'corridor': p['habitats'][h]['corridor'], 'bonus': p['habitats'][h]['bonus']} for h in H},
            'w_sub': p['wildlife_subtotal_written'],
            'h_sub': p['habitat_subtotal_written'],
            'nature': p['nature_tokens'],
            'notes': p.get('as_written_notes') or {},
            'issues': p.get('arithmetic_issues') or [],
        })
    rows.sort(key=lambda r: (r['pos'] is None, r['pos'] or 99, -(r['total'] or 0)))
    tops = sorted([r['total'] for r in rows if r['total'] is not None], reverse=True)
    games.append({
        'no': g['game_no'], 'id': g['id'],
        'date': g['date'] or g['date_best_guess'],
        'date_uncertain': date_uncertain(g),
        'date_raw': g['date_raw'], 'date_note': g.get('date_confidence'),
        'n': g['num_players'], 'winners': winners,
        'tied_on_total': len(g['winners_by_written_total']) > 1,
        'win_margin': (tops[0] - tops[1]) if len(tops) > 1 else None,
        'notes': g.get('notes') or [],
        'players': rows,
    })

# ---------- per-player ----------
appear = defaultdict(list)
for g in games:
    for r in g['players']:
        appear[r['id']].append((g, r))

# group averages per player-row
all_rows = [r for g in games for r in g['players']]
group = {
    'wildlife': {k: mean([r['wildlife'][k] for r in all_rows]) for k in W},
    'habitats': {h: mean([None if r['habitats'][h]['bonus'] is None else r['habitats'][h]['corridor'] + r['habitats'][h]['bonus'] for r in all_rows]) for h in H},
    'nature': mean([r['nature'] for r in all_rows]),
    'avg_score': mean([r['total'] for r in all_rows]),
}

def trend_label(slope10, n):
    if n < MAIN_MIN_GAMES:
        return f'Only {n} game{"s" if n != 1 else ""}, too few for a trend'
    if abs(slope10) < 1.5:
        return f'Steady (about {slope10:+.1f} points per 10 games)'
    return f'{"Improving" if slope10 > 0 else "Declining"} by ~{abs(slope10):.1f} points per 10 games'

players = {}
for pid, lst in appear.items():
    sc = [(g, r) for g, r in lst if r['total'] is not None]
    totals = [r['total'] for _, r in sc]
    wins = sum(1 for _, r in lst if r['win'])
    series = [{'no': g['no'], 'date': g['date'], 'approx': g['date_uncertain'], 'score': r['total'], 'pos': r['pos'], 'n': g['n'], 'win': r['win']} for g, r in sc]
    roll = []
    for i in range(len(totals)):
        w = totals[max(0, i - 4): i + 1]
        roll.append(round(sum(w) / len(w), 2))
    if len(totals) >= 2:
        slope, icpt = linfit(totals)
        trend_pts = [round(icpt + slope * (i + 1), 2) for i in range(len(totals))]
    else:
        slope, trend_pts = 0.0, totals[:]
    best = max(sc, key=lambda x: (x[1]['total'], -x[0]['no'])) if sc else None
    worst = min(sc, key=lambda x: (x[1]['total'], x[0]['no'])) if sc else None
    wl = {k: mean([r['wildlife'][k] for _, r in lst]) for k in W}
    hb = {h: mean([None if r['habitats'][h]['bonus'] is None else r['habitats'][h]['corridor'] + r['habitats'][h]['bonus'] for _, r in lst]) for h in H}
    # favourite = biggest edge over group average (relative), ties -> raw avg
    wl_edge = {k: (wl[k] - group['wildlife'][k]) for k in W if wl[k] is not None}
    hb_edge = {h: (hb[h] - group['habitats'][h]) for h in H if hb[h] is not None}
    top_animals = sorted(W, key=lambda k: -(wl[k] or 0))[:2]
    top_habitat = max(H, key=lambda h: hb[h] or 0)
    h2h = {}
    for g, r in sc:
        for o in g['players']:
            if o['id'] == pid or o['total'] is None:
                continue
            d = h2h.setdefault(o['id'], {'w': 0, 'l': 0, 't': 0, 'games': 0})
            d['games'] += 1
            if r['pos'] < o['pos']: d['w'] += 1
            elif r['pos'] > o['pos']: d['l'] += 1
            else: d['t'] += 1
    last5 = mean(totals[-5:]) if totals else None
    players[pid] = {
        'id': pid, 'name': NAMES.get(pid, pid),
        'games': len(lst), 'scored_games': len(sc), 'wins': wins,
        'win_pct': round(100 * wins / len(lst), 1),
        'avg': mean(totals), 'best': max(totals) if totals else None, 'worst': min(totals) if totals else None,
        'avg_pos': mean([r['pos'] for _, r in sc]),
        'avg_margin': mean([r['margin'] for _, r in sc]),
        'last5_avg': last5,
        'first_date': lst[0][0]['date'], 'last_date': lst[-1][0]['date'],
        'series': series, 'rolling5': roll, 'trend_line': trend_pts,
        'slope_per10': round(slope * 10, 2),
        'trend_label': trend_label(slope * 10, len(totals)),
        'main': len(lst) >= MAIN_MIN_GAMES,
        'wildlife_avg': wl, 'habitat_avg': hb,
        'wildlife_edge': {k: r2(v) for k, v in wl_edge.items()},
        'habitat_edge': {h: r2(v) for h, v in hb_edge.items()},
        'avg_w_sub': mean([r['w_sub'] for _, r in lst]),
        'avg_h_sub': mean([r['h_sub'] for _, r in lst]),
        'avg_nature': mean([r['nature'] for _, r in lst]),
        'top_animals': top_animals, 'top_habitat': top_habitat,
        'signature_animal': max(wl_edge, key=wl_edge.get) if wl_edge else None,
        'signature_habitat': max(hb_edge, key=hb_edge.get) if hb_edge else None,
        'h2h': dict(sorted(h2h.items(), key=lambda kv: -kv[1]['games'])),
        'best_game': {'no': best[0]['no'], 'date': best[0]['date'], 'score': best[1]['total'], 'pos': best[1]['pos'], 'n': best[0]['n']} if best else None,
        'worst_game': {'no': worst[0]['no'], 'date': worst[0]['date'], 'score': worst[1]['total']} if worst else None,
        'unscored_games': [g['no'] for g, r in lst if r['total'] is None],
    }

# ---------- insights ----------
ins = {}
scored_rows = [(g, r) for g in games for r in g['players'] if r['total'] is not None]

# winning score by month
by_month = defaultdict(list)
for g in games:
    by_month[g['date'][:7]].append(max(r['total'] for r in g['players'] if r['total'] is not None))
ins['win_score_by_month'] = [{'month': m, 'avg': mean(v), 'games': len(v)} for m, v in sorted(by_month.items())]
ws = [max(r['total'] for r in g['players'] if r['total'] is not None) for g in games]
half = len(ws) // 2
ins['win_score_halves'] = {'first_n': half, 'first_avg': mean(ws[:half]), 'second_n': len(ws) - half, 'second_avg': mean(ws[half:])}
ins['win_score_series'] = [{'no': g['no'], 'date': g['date'], 'score': s} for g, s in zip(games, ws)]
s, _ = linfit(ws); ins['win_score_slope_per10'] = round(s * 10, 2)
avg_series = [mean([r['total'] for r in g['players'] if r['total'] is not None]) for g in games]
s2, _ = linfit(avg_series); ins['avg_score_slope_per10'] = round(s2 * 10, 2)

# category vs winning: avg in winning rows vs others, and correlation with total
def cat_vals(r, cat):
    if cat in W: return r['wildlife'][cat]
    if cat == 'nature': return r['nature']
    c = r['habitats'][cat]
    return None if c['bonus'] is None else c['corridor'] + c['bonus']
cats = []
for cat in W + H + ['nature']:
    pairs = [(cat_vals(r, cat), r) for g, r in scored_rows if cat_vals(r, cat) is not None]
    wv = [v for v, r in pairs if r['win']]; lv = [v for v, r in pairs if not r['win']]
    corr = pearson([v for v, _ in pairs], [r['total'] for _, r in pairs])
    cats.append({'cat': cat, 'kind': 'wildlife' if cat in W else ('nature' if cat == 'nature' else 'habitat'),
                 'win_avg': mean(wv), 'rest_avg': mean(lv), 'diff': r2(mean(wv) - mean(lv)), 'corr_total': r2(corr),
                 'zeros': sum(1 for v, _ in pairs if v == 0), 'n': len(pairs), 'max': max(v for v, _ in pairs)})
ins['categories'] = cats

# by player count
pc = defaultdict(lambda: {'games': 0, 'scores': [], 'win': []})
for g in games:
    d = pc[g['n']]; d['games'] += 1
    t = [r['total'] for r in g['players'] if r['total'] is not None]
    d['scores'] += t; d['win'].append(max(t))
ins['by_player_count'] = [{'n': n, 'games': d['games'], 'avg_score': mean(d['scores']), 'avg_win': mean(d['win'])} for n, d in sorted(pc.items())]

# records
hi = max(scored_rows, key=lambda x: (x[1]['total'], -x[0]['no']))
lo = min(scored_rows, key=lambda x: (x[1]['total'], x[0]['no']))
ins['highest'] = {'player': hi[1]['id'], 'score': hi[1]['total'], 'no': hi[0]['no'], 'date': hi[0]['date']}
ins['lowest'] = {'player': lo[1]['id'], 'score': lo[1]['total'], 'no': lo[0]['no'], 'date': lo[0]['date']}
ins['highest_list'] = [{'player': r['id'], 'score': r['total'], 'no': g['no'], 'date': g['date']} for g, r in sorted(scored_rows, key=lambda x: (-x[1]['total'], x[0]['no']))[:5]]
big = max(games, key=lambda g: (g['win_margin'] or -1, -g['no']))
ins['biggest_margin'] = {'no': big['no'], 'date': big['date'], 'margin': big['win_margin'], 'winner': big['winners'][0],
                         'runner_up': big['players'][1]['id']}
ins['closest'] = [{'no': g['no'], 'date': g['date'], 'winners': g['winners'], 'margin': g['win_margin'],
                   'players': [r['id'] for r in g['players'] if r['total'] == max(x['total'] for x in g['players'] if x['total'] is not None)]}
                  for g in games if g['win_margin'] == 0]
ins['one_point_games'] = sum(1 for g in games if g['win_margin'] == 1)
# best single category scores
cell = []
for g, r in scored_rows:
    for k in W:
        if r['wildlife'][k] is not None: cell.append((r['wildlife'][k], k, r['id'], g['no'], g['date']))
cell.sort(key=lambda x: (-x[0], x[3]))
ins['best_wildlife_cells'] = [{'pts': c[0], 'animal': c[1], 'player': c[2], 'no': c[3], 'date': c[4]} for c in cell[:5]]
# pair rivalries
pairs = defaultdict(lambda: {'games': 0, 'a': 0, 'b': 0, 't': 0})
for g in games:
    ps = [r for r in g['players'] if r['total'] is not None]
    for x, y in combinations(sorted(ps, key=lambda r: r['id']), 2):
        d = pairs[(x['id'], y['id'])]; d['games'] += 1
        if x['pos'] < y['pos']: d['a'] += 1
        elif x['pos'] > y['pos']: d['b'] += 1
        else: d['t'] += 1
ins['rivalries'] = [{'a': a, 'b': b, 'games': d['games'], 'a_wins': d['a'], 'b_wins': d['b'], 'ties': d['t']} for (a, b), d in sorted(pairs.items(), key=lambda kv: -kv[1]['games'])[:6]]
# score composition
ins['composition'] = {'wildlife': mean([r['w_sub'] for _, r in scored_rows]), 'habitat': mean([r['h_sub'] for _, r in scored_rows]),
                      'nature': mean([r['nature'] for _, r in scored_rows]), 'total': mean([r['total'] for _, r in scored_rows])}
# win share
ins['wins_table'] = sorted([{'player': p['id'], 'wins': p['wins'], 'games': p['games']} for p in players.values() if p['wins']], key=lambda x: -x['wins'])
ins['tiebreaks'] = sum(1 for g in games if g['tied_on_total'])
ins['n_games'] = len(games); ins['n_rows'] = len(all_rows)
ins['date_range'] = [games[0]['date'], games[-1]['date']]
ins['streaks'] = {}
for pid in players:
    best = cur = 0
    for g in games:
        ids = [r['id'] for r in g['players']]
        if pid not in ids: continue
        cur = cur + 1 if pid in g['winners'] else 0
        best = max(best, cur)
    ins['streaks'][pid] = best
top_streak = max(ins['streaks'].items(), key=lambda kv: kv[1])
ins['longest_streak'] = {'player': top_streak[0], 'wins': top_streak[1]}

out = {'generated_from': 'games.json', 'wildlife': W, 'habitats': H, 'names': NAMES,
       'group': group, 'games': games, 'players': players, 'insights': ins}
site = os.environ.get('SITE_DIR', os.path.join(HERE, 'site'))
json.dump(out, open(os.path.join(site, 'data.json'), 'w'), indent=1)
with open(os.path.join(site, 'data.js'), 'w') as f:
    f.write('// Generated by make_site_data.py from games.json. Do not edit by hand.\nwindow.CASCADIA = ')
    json.dump(out, f, separators=(',', ':'))
    f.write(';\n')
print(f"{len(games)} games, {len(all_rows)} rows, {len(players)} players -> site/data.js")
for p in sorted(players.values(), key=lambda p: -p['games']):
    print(f"{p['id']:3} G{p['games']:3} W{p['wins']:3} {p['win_pct']:5}% avg {p['avg']} best {p['best']} worst {p['worst']} pos {p['avg_pos']} margin {p['avg_margin']} last5 {p['last5_avg']} | {p['trend_label']} | top {p['top_animals']} {p['top_habitat']}")
