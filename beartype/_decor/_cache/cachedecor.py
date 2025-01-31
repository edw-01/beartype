#!/usr/bin/env python3
# --------------------( LICENSE                            )--------------------
# Copyright (c) 2014-2022 Beartype authors.
# See "LICENSE" for further details.

'''
**Memoized beartype decorator.**

This private submodule defines the core :func:`beartype.beartype` decorator,
conditionally imported (in order):

#. Into the parent :mod:`beartype._decor.decormain`
   submodule if this decorator is *not* currently reducing to a noop (e.g., due
   to ``python3 -O`` optimization).
#. Into the root :mod:`beartype.__init__` submodule if the :mod:`beartype`
   package is *not* currently being installed by :mod:`setuptools`.

This private submodule is literally the :func:`beartype.beartype` decorator,
despite *not* actually being that decorator (due to being unmemoized).

This private submodule is *not* intended for importation by downstream callers.
'''

# ....................{ IMPORTS                            }....................
from beartype.roar import BeartypeConfException
from beartype.typing import (
    Dict,
    Optional,
)
from beartype._conf.confcls import (
    BEARTYPE_CONF_DEFAULT,
    BeartypeConf,
)
from beartype._conf.confenum import BeartypeStrategy
from beartype._data.datatyping import (
    BeartypeConfedDecorator,
    BeartypeReturn,
    BeartypeableT,
)
from beartype._decor.decorcore import beartype_object

# ....................{ DECORATORS                         }....................
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# CAUTION: Synchronize the signature of this non-identity decorator with the
# identity decorator defined by the "beartype._decor.decormain" submodule.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# CAUTION: Documentation for this decorator intentionally resides in the parent
# "beartype._decor.decormain" submodule.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def beartype(
    # Optional positional or keyword parameters.
    obj: Optional[BeartypeableT] = None,

    # Optional keyword-only parameters.
    *,
    conf: BeartypeConf = BEARTYPE_CONF_DEFAULT,
) -> BeartypeReturn:

    # If "conf" is *NOT* a configuration, raise an exception.
    if not isinstance(conf, BeartypeConf):
        raise BeartypeConfException(
            f'{repr(conf)} not beartype configuration.')
    # Else, "conf" is a configuration.
    #
    # If passed an object to be decorated, this decorator is in decoration
    # rather than configuration mode. In this case, decorate this object with
    # type-checking configured by this configuration.
    #
    # Note this branch is typically *ONLY* entered when the "conf" parameter
    # is *NOT* explicitly passed and thus defaults to the default
    # configuration. While callers may technically run this decorator in
    # decoration mode with a non-default configuration, doing so would be both
    # highly irregular *AND* violate PEP 561-compliance by violating the
    # decorator overloads declared above. Nonetheless, we're largely permissive
    # here; callers that are doing this are sufficiently intelligent to be
    # trusted to violate PEP 561-compliance if they so choose. So... *shrug*
    elif obj is not None:
        return beartype_object(obj, conf)
    # Else, we were passed *NO* object to be decorated. In this case, this
    # decorator is in configuration rather than decoration mode.

    # Private decorator (possibly previously generated and cached by a prior
    # call to this decorator also in configuration mode) generically applying
    # this configuration to any beartypeable object passed to that decorator
    # if a prior call to this public decorator has already been passed the same
    # configuration (and thus generated and cached this private decorator) *OR*
    # "None" otherwise (i.e., if this is the first call to this public
    # decorator passed this configuration in configuration mode). Phew!
    beartype_confed_cached = _bear_conf_to_decor.get(conf)

    # If a prior call to this public decorator has already been passed the same
    # configuration (and thus generated and cached this private decorator),
    # return this private decorator for subsequent use in decoration mode.
    if beartype_confed_cached:
        return beartype_confed_cached
    # Else, this is the first call to this public decorator passed this
    # configuration in configuration mode.
    #
    # If this configuration enables the no-time strategy performing *NO*
    # type-checking, define only the identity decorator reducing to a noop.
    elif conf.strategy is BeartypeStrategy.O0:
        #FIXME: This requires augmentation. We can't just return a pure
        #identity decorator. Instead, we need to return a minimal
        #quasi-identity decorator that:
        #* Monkey-patches the passed callable with our "__beartype_wrapped =
        #  True" (or whatever that is) dunder boolean to prevent repeated
        #  decorations be non-O(0) @beartype decorations.
        #* Cache PEP 585-compliant type hints to reduce space costs.
        def beartype_confed(obj: BeartypeableT) -> BeartypeableT:
            '''
            Return the passed **beartypeable** (i.e., pure-Python callable or
            class) as is *without* type-checking that beartypeable under a
            beartype configuration enabling the **no-time strategy** (i.e.,
            :attr:`beartype.BeartypeStrategy.O0`) passed to a prior call to the
            :func:`beartype.beartype` decorator.

            Parameters
            ----------
            obj : BeartypeableT
                Beartypeable to be preserved as is.

            Returns
            ----------
            BeartypeableT
                This beartypeable unmodified.

            See Also
            ----------
            :func:`beartype.beartype`
                Further details.
            '''

            return obj
    # Else, this configuration enables a positive-time strategy performing at
    # least the minimal amount of type-checking. In this case, define a private
    # decorator generically applying this configuration to any beartypeable
    # object passed to this decorator.
    else:
        def beartype_confed(obj: BeartypeableT) -> BeartypeableT:
            '''
            Decorate the passed **beartypeable** (i.e., pure-Python callable or
            class) with optimal type-checking dynamically generated unique to
            that beartypeable under the beartype configuration passed to a
            prior call to the :func:`beartype.beartype` decorator.

            Parameters
            ----------
            obj : BeartypeableT
                Beartypeable to be decorated.

            Returns
            ----------
            BeartypeableT
                Either:

                * If the passed object is a class, this existing class
                  embellished with dynamically generated type-checking.
                * If the passed object is a callable, a new callable wrapping
                  that callable with dynamically generated type-checking.

            See Also
            ----------
            :func:`beartype.beartype`
                Further details.
            '''

            # Decorate this object with type-checking configured by this
            # configuration.
            return beartype_object(obj, conf)

    # Cache this private decorator against this configuration.
    _bear_conf_to_decor[conf] = beartype_confed

    # Return this private decorator.
    return beartype_confed

# ....................{ SINGLETONS                         }....................
_bear_conf_to_decor: Dict[BeartypeConf, BeartypeConfedDecorator] = {}
'''
Non-thread-safe **beartype decorator cache.**

This cache is implemented as a singleton dictionary mapping from each
**beartype configuration** (i.e., self-caching dataclass encapsulating all
flags, options, settings, and other metadata configuring the current decoration
of the decorated callable or class) to the corresponding **configured beartype
decorator** (i.e., closure created and returned from the
:func:`beartype.beartype` decorator when passed a beartype configuration via
the optional ``conf`` parameter rather than an object to be decorated via
the optional ``obj`` parameter).

Caveats
----------
**This cache is not thread-safe.** Although rendering this cache thread-safe
would be trivial, doing so would needlessly reduce efficiency. This cache is
merely a runtime optimization and thus need *not* be thread-safe.
'''
