import collections
import yaml
from os.path import join, dirname

static_dir = join(dirname(__file__), "static")

with open(join(static_dir, "columns.yml"), 'r') as f:
    quantity_list = yaml.load(f)

quantities = collections.OrderedDict([(q['column'], q) for q in quantity_list])

plot_quantities = [ q for q in quantities.keys() if quantities[q]['type'] == 'float' ]

bondtype_dict = collections.OrderedDict([
    ('0', "#1f77b4"),
    ('1', "#d62728"),
    ('2', "#ff7f0e"),
    ('3', "#2ca02c"),
    ('4', "#778899"),
    ('5', "#04f238"),
])

with open(join(static_dir, "filters.yml"), 'r') as f:
    filter_list = yaml.load(f)

with open(join(static_dir, "presets.yml"), 'r') as f:
    presets = yaml.load(f)

for k in presets.keys():
    if 'clr' not in presets[k].keys():
        presets[k]['clr'] = presets['default']['clr']

max_points = 70000
