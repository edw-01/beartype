#!/usr/bin/env python3
# --------------------( LICENSE                            )--------------------
# Copyright (c) 2014-2022 Beartype authors.
# See "LICENSE" for further details.

'''
**Beartype configuration enumerations** (i.e., public enumerations whose members
may be passed as initialization-time parameters to the
:meth:`beartype._conf.confcls.BeartypeConf.__init__` constructor to configure
:mod:`beartype` with optional runtime type-checking behaviours).

Most of the public attributes defined by this private submodule are explicitly
exported to external users in our top-level :mod:`beartype.__init__` submodule.
This private submodule is *not* intended for direct importation by downstream
callers.
'''

# ....................{ IMPORTS                            }....................
from enum import (
    Enum,
    auto as next_enum_member_value,
    unique as die_unless_enum_member_values_unique,
)

# ....................{ ENUMERATIONS                       }....................
#FIXME: Document us up in "README.rst", please.
@die_unless_enum_member_values_unique
class BeartypeStrategy(Enum):
    '''
    Enumeration of all kinds of **type-checking strategies** (i.e., competing
    procedures for type-checking objects passed to or returned from
    :func:`beartype.beartype`-decorated callables, each with concomitant
    tradeoffs with respect to runtime complexity and quality assurance).

    Strategies are intentionally named according to `conventional Big O
    notation <Big O_>`__ (e.g., :attr:`BeartypeStrategy.On` enables the
    ``O(n)`` strategy). Strategies are established per-decoration at the
    fine-grained level of callables decorated by the :func: `beartype.beartype`
    decorator by either:

    * Calling a high-level convenience decorator establishing that strategy
      (e.g., :func:`beartype.conf.beartype_On`, enabling the ``O(n)`` strategy
      for all callables decorated by that decorator).
    * Setting the :attr:`BeartypeConfiguration.strategy` variable of the
      :attr:`BeartypeConfiguration` object passed as the optional ``conf``
      parameter to the lower-level core :func: `beartype.beartype` decorator.

    Strategies enforce and guarantee their corresponding runtime complexities
    (e.g., ``O(n)``) across all type checks performed for all callables
    enabling those strategies. For example, a callable decorated with the
    :attr:`BeartypeStrategy.On` strategy will exhibit linear runtime complexity
    as its type-checking overhead.

    .. _Big O:
       https://en.wikipedia.org/wiki/Big_O_notation

    Attributes
    ----------
    O0 : EnumMemberType
        **No-time strategy** (i.e, disabling type-checking for a decorated
        callable by reducing :func:`beartype.beartype` to the identity
        decorator for that callable). Although seemingly useless, this strategy
        enables users to selectively blacklist (prevent) callables from being
        type-checked by our as-yet-unimplemented import hook. When implemented,
        that hook will type-check all callables within a package or module
        *except* those callables explicitly decorated by this strategy.
    O1 : EnumMemberType
        **Constant-time strategy** (i.e., the default ``O(1)`` strategy,
        type-checking a single randomly selected item of each container). As
        the default, this strategy need *not* be explicitly enabled.
    Ologn : EnumMemberType
        **Logarithmic-time strategy** (i.e., the ``O(log n)` strategy,
        type-checking a randomly selected number of items ``log(len(obj))`` of
        each container ``obj``). This strategy is **currently unimplemented.**
        (*To be implemented by a future beartype release.*)
    On : EnumMemberType
        **Linear-time strategy** (i.e., an ``O(n)`` strategy, type-checking
        *all* items of a container). This strategy is **currently
        unimplemented.** (*To be implemented by a future beartype release.*)
    '''

    O0 = next_enum_member_value()
    O1 = next_enum_member_value()
    Ologn = next_enum_member_value()
    On = next_enum_member_value()
