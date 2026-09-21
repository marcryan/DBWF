import json, os

BASE = '/media/SSD-Dev/_code/2026-varsity-roster-lookup'

# Map CIAC grade (9-12) to the app's year label
GRADE_TO_YEAR = {'12': 'Senior', '11': 'Junior', '10': 'Sophomore', '9': 'Freshman'}

SPORTS = [
    'football-boys',
    'soccer-boys',
    'soccer-girls',
    'field-hockey',
    'volleyball-girls',
]

# Human-friendly roster display titles
TITLES = {
    'football-boys':      'Football: Varsity Roster',
    'soccer-boys':        'Soccer (Boys): Varsity Roster',
    'soccer-girls':       'Soccer (Girls): Varsity Roster',
    'field-hockey':       'Field Hockey (Girls): Varsity Roster',
    'volleyball-girls':   'Volleyball (Girls): Varsity Roster',
}

def jersey_numbers(raw):
    """Extract valid jersey numbers (int 1..99) from a source number field.
    Handles single values like '45', dual values like '0,7' / '5,13', and empty.
    Returns a list (possibly empty if the source had no usable number)."""
    if not raw:
        return []
    out = []
    for part in str(raw).replace(' ', '').split(','):
        if part.isdigit():
            n = int(part)
            if 1 <= n <= 99:
                out.append(n)
    return out

for sport in SPORTS:
    src = os.path.join(BASE, f'roster_{sport}.json')
    with open(src) as f:
        data = json.load(f)

    players = []
    skipped = []
    for p in data.get('players', []):
        nums = jersey_numbers(p.get('number'))
        year = GRADE_TO_YEAR.get(p.get('grade'))
        if not nums or not year:
            # No valid jersey number (e.g. field-hockey managers) or unknown grade
            skipped.append(p)
            continue
        for n in nums:
            players.append({'number': n, 'name': p['name'], 'year': year})

    # Sort by jersey number, keep original order for ties
    players.sort(key=lambda x: x['number'])

    doc = {
        'settings': {'title': TITLES[sport], 'accentColor': '#1144EB'},
        'players': players,
    }

    out = os.path.join(BASE, f'roster-app-{sport}.json')
    with open(out, 'w') as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)

    # Report
    dups = {}
    for p in players:
        dups.setdefault(p['number'], []).append(p['name'])
    dup_nums = {k: v for k, v in dups.items() if len(v) > 1}
    summary = f'{out}: {len(players)} players'
    if dup_nums:
        summary += ' | DUPLICATE #: ' + json.dumps(dup_nums, ensure_ascii=False)
    print(summary)
    if skipped:
        print('   skipped (no 1-99 jersey or unknown grade):',
              ', '.join(f"{p.get('name')} [#{p.get('number')}, gr{p.get('grade')}]" for p in skipped))

# Report dual-number handling explicitly (volleyball)
print('\n-- dual number fields in source (expanded to one row per number) --')
for sport in SPORTS:
    data = json.load(open(os.path.join(BASE, f'roster_{sport}.json')))
    duals = [p for p in data.get('players', []) if ',' in str(p.get('number', ''))]
    if duals:
        print(f"{sport}: " + ', '.join(f"{p['name']} ({p.get('number')})" for p in duals))