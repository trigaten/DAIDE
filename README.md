# DAIDE

SUPPORTS most bot order related communication commands levels 0-30. Please make an issue if u want a new word (or a PR :) )

AND ORR XDO HLD MTO SUP CVY CTO VIA YES HUH FCT PRP

This library parses DAIDE strings into a recursive object model. It can also generate a string from the object model.

e.g. `"AND (order1) (order2)" -> AND([order1, order2])`

## Usage

(FFF are placeholders for a province)

```python
>>> from DAIDE import parse
>>> arrangement = parse('AND (XDO ((FFF FFF FFF) HLD)) (XDO ((FFF FFF FFF) HLD))')

>>> arrangement
<DAIDE.syntax.lvl30.binop.AND object at 0x7fb6623193c8>

# parsed objects are nested
>>> arrangement.arrangements
[<DAIDE.syntax.lvl20.xdo.XDO object at 0x7fb6622bd7f0>, <DAIDE.syntax.lvl20.xdo.XDO object at 0x7fb6622bd8d0>]

# generate string from DAIDE object
>>> str(arrangement)
'AND (XDO ((FFF FFF FFF) HLD)) (XDO ((FFF FFF FFF) HLD))'

# easily compose DAIDE keywords
>>> from DAIDE import Order, Unit, ORR, HLD
>>> arrangement = ORR([Order(Unit("FFF FFF FFF"), HLD()), Order(Unit("FFF FFF FFF"), HLD())])
>>> str(arrangement)
'ORR ((FFF FFF FFF) HLD) ((FFF FFF FFF) HLD)'
```

### Advanced

If you are not working with DAIDE style orders (e.g. Diplomacy Github uses shorthand order style), run the following at the beginning of your code:

```python
from DAIDE import config
config.ORDERS_DAIDE = False
```

## Installation

### From Github (easiest)

`pip install git+https://github.com/trigaten/DAIDE.git`

### From inside repo

`pip install -e .`

## Adding Syntax

All syntax words are represented as objects which implement 

a `parse()` function and `__str__`




