.. # ------------------( SEO                                 )------------------
.. # Metadata converted into HTML-specific meta tags parsed by search engines.
.. # Note that:
.. # * The "description" should be no more than 300 characters and ideally no
.. #   more than 150 characters, as search engines may silently truncate this
.. #   description to 150 characters in edge cases.

.. meta::
   :description lang=en:
     Beartype is an open-source pure-Python PEP-compliant constant-time runtime
     type checker emphasizing efficiency and portability.

.. # ------------------( SYNOPSIS                            )------------------

=================
|beartype-banner|
=================

|codecov-badge| |ci-badge| |rtd-badge|

**Beartype** is an `open-source <beartype license_>`__ `PEP-compliant
<Compliance_>`__ `near-real-time <beartype realtime_>`__ `pure-Python runtime
type checker <Usage_>`__ emphasizing efficiency, usability, and thrilling puns.

.. #FIXME: Once we actually receive a sponsor at this tier, please remove this
.. #placeholder as well as the icon links below. kthx
.. #The `Bear Team <beartype organization_>`__ gratefully thanks `our family of
.. #breathtaking GitHub Sponsors <beartype sponsorship_>`__:
.. #
.. #* **Your iconic URL here.** `Let us bestow you with eyeballs <beartype
.. #  sponsorship_>`__.
.. #FIXME: Once we actually receive a sponsor at this tier, please remove this
.. #placeholder as well as the icon links below. kthx
.. #    |icon-for-glorious-sponsor|

.. code-block:: bash

   # Install beartype.
   $ pip3 install beartype
   # So let's do this.
   $ python3

.. code-block:: python

   # Import the @beartype decorator.
   >>> from beartype import beartype

   # Annotate @beartype-decorated callables with type hints.
   >>> @beartype
   ... def quote_wiggum(lines: list[str]) -> None:
   ...     print('“{}”\n\t— Police Chief Wiggum'.format("\n ".join(lines)))

   # Call those callables with valid parameters.
   >>> quote_wiggum(["Okay, folks. Show's over!", "Nothing to see here. Show's…",])
   “Okay, folks. Show's over!
    Nothing to see here. Show's…”
      — Police Chief Wiggum

   # Call those callables with invalid parameters.
   >>> quote_wiggum([b"Oh, my God! A horrible plane crash!", b"Hey, everybody! Get a load of this flaming wreckage!",])
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "<string>", line 30, in quote_wiggum
     File "/home/springfield/beartype/lib/python3.9/site-packages/beartype/_decor/_code/_pep/_error/errormain.py", line 220, in get_beartype_violation
       raise exception_cls(
   beartype.roar.BeartypeCallHintParamViolation: @beartyped
   quote_wiggum() parameter lines=[b'Oh, my God! A horrible plane
   crash!', b'Hey, everybody! Get a load of thi...'] violates type hint
   list[str], as list item 0 value b'Oh, my God! A horrible plane crash!'
   not str.

   # ..................{ VALIDATORS  }..................
   # Squash bugs by refining type hints with validators.
   >>> from beartype.vale import Is  # <---- validator factory
   >>> from typing import Annotated  # <---------------- if Python ≥ 3.9.0
   # >>> from typing_extensions import Annotated   # <-- if Python < 3.9.0

   # Validators are type hints constrained by lambda functions.
   >>> ListOfStrings = Annotated[  # <----- type hint matching non-empty list of strings
   ...     list[str],  # <----------------- type hint matching possibly empty list of strings
   ...     Is[lambda lst: bool(lst)]  # <-- lambda matching non-empty object
   ... ]

   # Annotate @beartype-decorated callables with validators.
   >>> @beartype
   ... def quote_wiggum_safer(lines: ListOfStrings) -> None:
   ...     print('“{}”\n\t— Police Chief Wiggum'.format("\n ".join(lines)))

   # Call those callables with invalid parameters.
   >>> quote_wiggum_safer([])
   beartype.roar.BeartypeCallHintParamViolation: @beartyped
   quote_wiggum_safer() parameter lines=[] violates type hint
   typing.Annotated[list[str], Is[lambda lst: bool(lst)]], as value []
   violates validator Is[lambda lst: bool(lst)].

   # ..................{ AT ANY TIME }..................
   # Type-check anything against any type hint –
   # anywhere at anytime.
   >>> from beartype.door import (
   ...     is_bearable,  # <-------- like "isinstance(...)"
   ...     die_if_unbearable,  # <-- like "assert isinstance(...)"
   ... )
   >>> is_bearable(['The', 'goggles', 'do', 'nothing.'], list[str])
   True
   >>> die_if_unbearable([0xCAFEBEEF, 0x8BADF00D], ListOfStrings)
   beartype.roar.BeartypeDoorHintViolation: Object [3405692655, 2343432205]
   violates type hint typing.Annotated[list[str], Is[lambda lst: bool(lst)]],
   as list index 0 item 3405692655 not instance of str.

   # ..................{ GO TO PLAID }..................
   # Type-check anything in around 1µs (one millionth of
   # a second) – including this list of one million
   # 2-tuples of NumPy arrays.
   >>> from beartype.door import is_bearable
   >>> from numpy import array, ndarray
   >>> data = [(array(i), array(i)) for i in range(1000000)]
   >>> %time is_bearable(data, list[tuple[ndarray, ndarray]])
       CPU times: user 31 µs, sys: 2 µs, total: 33 µs
       Wall time: 36.7 µs
   True

Beartype brings Rust_- and `C++`_-inspired `zero-cost abstractions <zero-cost
abstraction_>`__ into the lawless world of `dynamically-typed`_ Python by
`enforcing type safety at the granular level of functions and methods
<Usage_>`__ against `type hints standardized by the Python community
<Compliance_>`__ in `O(1) non-amortized worst-case time with negligible constant
factors <Timings_>`__. If the prior sentence was unreadable jargon, `see our
friendly and approachable FAQ for a human-readable synopsis <Frequently Asked
Questions (FAQ)_>`__.

Beartype is `portably implemented <beartype codebase_>`__ in `Python 3
<Python_>`__, `continuously stress-tested <beartype tests_>`__ via `GitHub
Actions`_ **×** tox_ **×** pytest_ **×** Codecov_, and `permissively
distributed <beartype license_>`__ under the `MIT license`_. Beartype has *no*
runtime dependencies, `only one test-time dependency <pytest_>`__, and `only
one documentation-time dependency <Sphinx_>`__. Beartype supports `all actively
developed Python versions <Python status_>`__, `all Python package managers
<Install_>`__, and `multiple platform-specific package managers <Install_>`__.

    Beartype `powers quality assurance across the Python ecosystem <beartype
    dependents_>`__.

.. # ------------------( TABLE OF CONTENTS                  )------------------
.. # Blank line. By default, Docutils appears to only separate the subsequent
.. # table of contents heading from the prior paragraph by less than a single
.. # blank line, hampering this table's readability and aesthetic comeliness.

|

.. # Table of contents, excluding the above document heading. While the
.. # official reStructuredText documentation suggests that a language-specific
.. # heading will automatically prepend this table, this does *NOT* appear to
.. # be the case. Instead, this heading must be explicitly declared.

.. contents:: **Contents**
   :local:

.. # ------------------( DESCRIPTION                        )------------------

Install
=======

Let's install beartype with pip_:

.. code-block:: bash

   pip3 install beartype

Let's install beartype with Anaconda_:

.. code-block:: bash

   conda config --add channels conda-forge
   conda install beartype

`Commemorate this moment in time <Badge_>`__ with |bear-ified|, our
over\ *bear*\ ing project shield. What says quality like `a bear on a badge
<Badge_>`__, amirite?

Platform
--------

Beartype is also installable with platform-specific package managers, because
sometimes you just need this thing to work.

macOS
~~~~~

Let's install beartype with Homebrew_ on macOS_ courtesy `our third-party
tap <beartype Homebrew_>`__:

.. code-block:: bash

   brew install beartype/beartype/beartype

Let's install beartype with MacPorts_ on macOS_:

.. code-block:: bash

   sudo port install py-beartype

A big bear hug to `our official macOS package maintainer @harens <harens_>`__
for `packaging beartype for our Apple-appreciating audience <beartype
MacPorts_>`__.

Linux
~~~~~

Let's install beartype with ``emerge`` on Gentoo_ courtesy `a third-party
overlay <beartype Gentoo_>`__, because source-based Linux distributions are the
CPU-bound nuclear option:

.. code-block:: bash

   emerge --ask app-eselect/eselect-repository
   mkdir -p /etc/portage/repos.conf
   eselect repository enable raiagent
   emerge --sync raiagent
   emerge beartype

*What could be simpler?* O_o

Badge
-----

If you're feeling the quality assurance and want to celebrate, consider
signaling that you're now publicly *bear-*\ ified:

  YummySoft is now |bear-ified|!

All this magic and possibly more can be yours with:

* **Markdown**:

  .. code-block:: md

     YummySoft is now [![bear-ified](https://raw.githubusercontent.com/beartype/beartype-assets/main/badge/bear-ified.svg)](https://beartype.readthedocs.io)!

* **reStructuredText**:

  .. code-block:: rst

     YummySoft is now |bear-ified|!

     .. # See https://docutils.sourceforge.io/docs/ref/rst/directives.html#image
     .. |bear-ified| image:: https://raw.githubusercontent.com/beartype/beartype-assets/main/badge/bear-ified.svg
        :align: top
        :target: https://beartype.readthedocs.io
        :alt: bear-ified

* **Raw HTML**:

  .. code-block:: html

     YummySoft is now <a href="https://beartype.readthedocs.io"><img
       src="https://raw.githubusercontent.com/beartype/beartype-assets/main/badge/bear-ified.svg"
       alt="bear-ified"
       style="vertical-align: middle;"></a>!

Let a soothing pastel bear give your users the reassuring **OK** sign.

Overview
========

.. parsed-literal::

   Look for the bare necessities,
     the simple bare necessities.
   Forget about your worries and your strife.
                           — `The Jungle Book`_.

Beartype is a novel first line of defense. In Python's vast arsenal of
`software quality assurance (SQA) <SQA_>`__, beartype holds the `shield wall`_
against breaches in type safety by improper parameter and return values
violating developer expectations.

Beartype is unopinionated. Beartype inflicts *no* developer constraints
beyond `importation and usage of a single configuration-free decorator
<Cheatsheet_>`__. Beartype is trivially integrated into new and existing
applications, stacks, modules, and scripts already annotating callables with
`PEP-compliant industry-standard type hints <Compliance_>`__.

Beartype is zero-cost. Beartype inflicts *no* harmful developer tradeoffs,
instead stressing expense-free strategies at both:

* **Installation time.** Beartype has no install-time or runtime dependencies,
  `supports standard Python package managers <Install_>`__, and happily
  coexists with competing static type checkers and other runtime type checkers.
* **Runtime.** Thanks to aggressive memoization and dynamic code generation at
  decoration time, beartype guarantees `O(1) non-amortized worst-case runtime
  complexity with negligible constant factors <Timings_>`__.

Versus Static Type Checkers
---------------------------

Like `competing static type checkers <Static Type Checkers_>`__ operating at
the coarse-grained application level via ad-hoc heuristic type inference (e.g.,
Pyre_, mypy_, pyright_, pytype_), beartype effectively `imposes no runtime
overhead <Timings_>`__. Unlike static type checkers:

* Beartype operates exclusively at the fine-grained callable level of
  pure-Python functions and methods via the standard decorator design pattern.
  This renders beartype natively compatible with *all* interpreters and
  compilers targeting the Python language – including Brython_, PyPy_, Numba_,
  Nuitka_, and (wait for it) CPython_ itself.
* Beartype enjoys deterministic Turing-complete access to the actual callables,
  objects, and types being type-checked. This enables beartype to solve dynamic
  problems decidable only at runtime – including type-checking of arbitrary
  objects whose:

  * Metaclasses `dynamically customize instance and subclass checks
    <_isinstancecheck>`__ by implementing the ``__instancecheck__()`` and/or
    ``__subclasscheck__()`` dunder methods, including:

    * `PEP 3119`_-compliant metaclasses (e.g., `abc.ABCMeta`_).

  * Pseudo-superclasses `dynamically customize the method resolution order
    (MRO) of subclasses <_mro_entries>`__ by implementing the
    ``__mro_entries__()`` dunder method, including:

    * `PEP 560`_-compliant pseudo-superclasses.

  * Classes dynamically register themselves with standard abstract base classes
    (ABCs), including:

    * `PEP 3119`_-compliant third-party virtual base classes.
    * `PEP 3141`_-compliant third-party virtual number classes (e.g., SymPy_).

  * Classes are dynamically constructed or altered, including by:

    * Class decorators.
    * Class factory functions and methods.
    * Metaclasses.
    * Monkey patches.

Versus Runtime Type Checkers
----------------------------

Unlike `comparable runtime type checkers <Runtime Type Checkers_>`__ (e.g.,
pydantic_, typeguard_), beartype decorates callables with dynamically generated
wrappers efficiently type-checking each parameter passed to and value returned
from those callables in constant time. Since "performance by default" is our
first-class concern, generated wrappers are guaranteed to:

* Exhibit `O(1) non-amortized worst-case time complexity with negligible
  constant factors <Timings_>`__.
* Be either more efficient (in the common case) or exactly as efficient minus
  the cost of an additional stack frame (in the worst case) as equivalent
  type-checking implemented by hand, *which no one should ever do.*

Frequently Asked Questions (FAQ)
================================

What is beartype?
-----------------

Why, it's the world's first ``O(1)`` runtime type checker in any
`dynamically-typed`_ lang... oh, *forget it.*

You know typeguard_? Then you know beartype – more or less. beartype is
typeguard_'s younger, faster, and slightly sketchier brother who routinely
ingests performance-enhancing anabolic nootropics.

What is typeguard?
------------------

**Okay.** Work with us here, people.

You know how in low-level `statically-typed`_ `memory-unsafe <memory
safety_>`__ languages that no one should use like C_ and `C++`_, the compiler
validates at compilation time the types of all values passed to and returned
from all functions and methods across the entire codebase?

.. code-block:: bash

   $ gcc -Werror=int-conversion -xc - <<EOL
   #include <stdio.h>
   int main() {
       printf("Hello, world!");
       return "Goodbye, world.";
   }
   EOL
   <stdin>: In function ‘main’:
   <stdin>:4:11: error: returning ‘char *’ from a function with return type
   ‘int’ makes integer from pointer without a cast [-Werror=int-conversion]
   cc1: some warnings being treated as errors

You know how in high-level `duck-typed <duck typing_>`__ languages that
everyone should use instead like Python_ and Ruby_, the interpreter performs no
such validation at any interpretation phase but instead permits any arbitrary
values to be passed to or returned from any function or method?

.. code-block:: bash

   $ python3 - <<EOL
   def main() -> int:
       print("Hello, world!");
       return "Goodbye, world.";
   main()
   EOL

   Hello, world!

Runtime type checkers like beartype_ and typeguard_ selectively shift the dial
on type safety in Python from `duck <duck typing_>`__ to `static typing
<statically-typed_>`__ while still preserving all of the permissive benefits of
the former as a default behaviour.

.. code-block:: bash

   $ python3 - <<EOL
   from beartype import beartype
   @beartype
   def main() -> int:
       print("Hello, world!");
       return "Goodbye, world.";
   main()
   EOL

   Hello, world!
   Traceback (most recent call last):
     File "<stdin>", line 6, in <module>
     File "<string>", line 17, in main
     File "/home/leycec/py/beartype/beartype/_decor/_code/_pep/_error/errormain.py", line 218, in get_beartype_violation
       raise exception_cls(
   beartype.roar.BeartypeCallHintPepReturnException: @beartyped main() return
   'Goodbye, world.' violates type hint <class 'int'>, as value 'Goodbye,
   world.' not int.

When should I use beartype?
---------------------------

Use beartype to assure the quality of Python code beyond what tests alone
can assure. If you have yet to test, do that first with a pytest_-based test
suite, tox_ configuration, and `continuous integration (CI) <continuous
integration_>`__. If you have any time, money, or motivation left, `annotate
callables with PEP-compliant type hints <Compliance_>`__ and `decorate those
callables with the @beartype.beartype decorator <Usage_>`__.

Prefer beartype over other runtime and static type checkers whenever you
lack control over the objects passed to or returned from your callables –
*especially* whenever you cannot limit the size of those objects. This includes
common developer scenarios like:

* You are the author of an **open-source library** intended to be reused by a
  general audience.
* You are the author of a **public app** accepting as input or generating as
  output sufficiently large data internally passed to or returned from app
  callables.

If none of the above apply, prefer beartype over static type checkers
whenever:

* You want to `check types decidable only at runtime <Versus Static Type
  Checkers_>`__.
* You want to write code rather than fight a static type checker, because
  `static type inference <type inference_>`__ of a `dynamically-typed`_
  language is guaranteed to fail and frequently does. If you've ever cursed the
  sky after suffixing working code incorrectly typed by mypy_ with non-portable
  vendor-specific pragmas like ``# type: ignore[{unreadable_error}]``,
  beartype was written for you.
* You want to preserve `dynamic typing`_, because Python is a
  `dynamically-typed`_ language. Unlike beartype, static type checkers
  enforce `static typing`_ and are thus strongly opinionated; they believe
  `dynamic typing`_ is harmful and emit errors on `dynamically-typed`_ code.
  This includes common use patterns like changing the type of a variable by
  assigning that variable a value whose type differs from its initial value.
  Want to freeze a variable from a ``set`` into a ``frozenset``? That's sad,
  because static type checkers don't want you to. In contrast:

    **Beartype never emits errors, warnings, or exceptions on dynamically-typed
    code,** because Python is not an error.

    **Beartype believes dynamic typing is beneficial by default,** because
    Python is beneficial by default.

    **Beartype is unopinionated.** That's because beartype `operates
    exclusively at the higher level of pure-Python callables <Versus Static
    Type Checkers_>`__ rather than the lower level of individual statements
    *inside* pure-Python callables. Unlike static type checkers, beartype
    can't be opinionated about things that no one should be.

If none of the above *still* apply, still use beartype. It's `free
as in beer and speech <gratis versus libre_>`__, `cost-free at installation-
and runtime <Overview_>`__, and transparently stacks with existing
type-checking solutions. Leverage beartype until you find something that
suites you better, because beartype is *always* better than nothing.

Why should I use beartype?
--------------------------

The idea of beartype is that it never costs you anything. It might not do
as much as you'd like, but it will always do *something* – which is more than
Python's default behaviour, which is to do *nothing* and ignore type hints
altogether. This means you can always safely add beartype to any Python
package, module, app, or script regardless of size, scope, funding, or audience
and never worry about your backend Django_ server taking a nosedive on St.
Patty's Day just because your frontend React_ client helpfully sent a 5MB JSON
file serializing a doubly-nested list of integers.

The idea of typeguard_ is that it does *everything.* If you annotate a function
decorated by typeguard_ as accepting a triply-nested list of integers and pass
that function a list of 1,000 nested lists of 1,000 nested lists of 1,000
integers, *every* call to that function will check *every* integer transitively
nested in that list – even if that list never changes. Did we mention that list
transitively contains 1,000,000,000 integers in total?

.. code-block:: bash

   $ python3 -m timeit -n 1 -r 1 -s '
   from typeguard import typechecked
   @typechecked
   def behold(the_great_destroyer_of_apps: list[list[list[int]]]) -> int:
       return len(the_great_destroyer_of_apps)
   ' 'behold([[[0]*1000]*1000]*1000)'

   1 loop, best of 1: 6.42e+03 sec per loop

Yes, ``6.42e+03 sec per loop == 6420 seconds == 107 minutes == 1 hour, 47
minutes`` to check a single list once. Yes, it's an uncommonly large list, but
it's still just a list. This is the worst-case cost of a single call to a
function decorated by a naïve runtime type checker.

What does beartype do?
----------------------

Generally, as little as it can while still satisfying the accepted definition
of "runtime type checker." Specifically, beartype performs a `one-way
random walk over the expected data structure of objects passed to and returned
from @beartype-decorated functions and methods <That's Some Catch, That
Catch-22_>`__. Basically, beartype type-checks randomly sampled data.

Consider `the prior example of a function annotated as accepting a
triply-nested list of integers passed a list containing 1,000 nested lists each
containing 1,000 nested lists each containing 1,000 integers <Why should I use
beartype?_>`__.

When decorated by typeguard_, every call to that function checks every integer
nested in that list.

When decorated by beartype, every call to the same function checks only a
single random integer contained in a single random nested list contained in a
single random nested list contained in that parent list. This is what we mean
by the quaint phrase "one-way random walk over the expected data structure."

.. code-block:: bash

   $ python3 -m timeit -n 1024 -r 4 -s '
   from beartype import beartype
   @beartype
   def behold(the_great_destroyer_of_apps: list[list[list[int]]]) -> int:
      return len(the_great_destroyer_of_apps)
   ' 'behold([[[0]*1000]*1000]*1000)'

   1024 loops, best of 4: 13.8 usec per loop

``13.8 usec per loop == 13.8 microseconds = 0.0000138 seconds`` to transitively
check only a random integer nested in a single triply-nested list passed to
each call of that function. This is the worst-case cost of a single call to a
function decorated by an ``O(1)`` runtime type checker.

.. _beartype realtime:

What does "near-real-time" even mean?
-------------------------------------

Beartype type-checks objects at runtime in around **1µs** (i.e., one
microsecond, one millionth of a second), the standard high-water mark for
`real-time software <real-time_>`__:

.. code-block:: python

   # Let's check a list of 181,320,382 integers in ~1µs.
   >>> from beartype import beartype
   >>> def sum_list_unbeartyped(some_list: list) -> int:
   ...     return sum(some_list)
   >>> sum_list_beartyped = beartype(sum_list_unbeartyped)
   >>> %time sum_list_unbeartyped([42]*0xACEBABE)
   CPU times: user 3.15 s, sys: 418 ms, total: 3.57 s
   Wall time: 3.58 s  # <-- okay.
   Out[20]: 7615456044
   >>> %time sum_list_beartyped([42]*0xACEBABE)
   CPU times: user 3.11 s, sys: 440 ms, total: 3.55 s
   Wall time: 3.56 s  # <-- woah.
   Out[22]: 7615456044

Beartype does *not* contractually guarantee this performance, as the above
example demonstrates. Under abnormal processing loads (e.g., leycec_'s arthritic
Athlon™ II X2 240, because you can't have enough redundant 2's in a product
line) or when passed edge-case type hints (e.g., classes whose metaclasses
implement stunningly bad ``__isinstancecheck__()`` dunder methods), worst-case
performance could exceed this average-case near-instantaneous response time.

Beartype is therefore *not* real-time_; beartype is merely `near-real-time (NRT)
<near-real-time_>`__, also variously referred to as "pseudo-real-time,"
"quasi-real-time," or simply "high-performance." Real-time_ software guarantees
performance with a scheduler forcibly terminating tasks exceeding some deadline.
That's bad in most use cases. The outrageous cost of enforcement harms
real-world performance, stability, and usability.

Thus NRT. It's like an NFT – only wonderful rather than not. That must be what
the "F" stands for.

How do I type-check...
----------------------

...yes? Go on.

...Boto3 types?
~~~~~~~~~~~~~~~

**tl;dr:** You just want bearboto3_, a well-maintained third-party package
cleanly integrating beartype **+** Boto3_. But you're not doing that.
You're reading on to find out why you want bearboto3_, aren't you? I *knew* it.

Boto3_ is the official Amazon Web Services (AWS) Software Development Kit (SDK)
for Python. Type-checking Boto3_ types is decidedly non-trivial, because Boto3_
dynamically fabricates unimportable types from runtime service requests. These
types *cannot* be externally accessed and thus *cannot* be used as type hints.

**H-hey!** Put down the hot butter knife. Your Friday night may be up in
flames, but we're gonna put out the fire. It's what we do here. Now, you have
two competing solutions with concomitant tradeoffs. You can type-check Boto3_
types against either:

* **Static type checkers** (e.g., mypy_, pyright_) by importing Boto3_ stub
  types from an external third-party dependency (e.g., mypy-boto3_), enabling
  context-aware code completion across compliant IDEs (e.g., PyCharm_, `VSCode
  Pylance <Pylance_>`__). Those types are merely placeholder stubs; they do
  *not* correspond to actual Boto3_ types and thus break runtime type checkers
  (including beartype) when used as type hints.
* **Beartype** by fabricating your own `PEP-compliant beartype validators
  <Beartype Validators_>`__, enabling beartype to validate arbitrary
  objects against actual Boto3_ types at runtime when used as type hints. You
  already require beartype, so no additional third-party dependencies are
  required. Those validators are silently ignored by static type checkers; they
  do *not* enable context-aware code completion across compliant IDEs.

"B-but that *sucks*! How can we have our salmon and devour it too?", you demand
with a tremulous quaver. Excessive caffeine and inadequate gaming did you no
favors tonight. You know this. Yet again you reach for the hot butter knife.

**H-hey!** You can, okay? You can have everything that market forces demand.
Bring to *bear* :superscript:`cough` the combined powers of `PEP 484-compliant
type aliases <type aliases_>`__, the `PEP 484-compliant "typing.TYPE_CHECKING"
boolean global <typing.TYPE_CHECKING_>`__, and `beartype validators <Beartype
Validators_>`__ to satisfy both static and runtime type checkers:

.. code-block:: python

   # Import the requisite machinery.
   from beartype import beartype
   from boto3 import resource
   from boto3.resources.base import ServiceResource
   from typing import TYPE_CHECKING

   # If performing static type-checking (e.g., mypy, pyright), import boto3
   # stub types safely usable *ONLY* by static type checkers.
   if TYPE_CHECKING:
       from mypy_boto3_s3.service_resource import Bucket
   # Else, @beartime-based runtime type-checking is being performed. Alias the
   # same boto3 stub types imported above to their semantically equivalent
   # beartype validators accessible *ONLY* to runtime type checkers.
   else:
       # Import even more requisite machinery. Can't have enough, I say!
       from beartype.vale import IsAttr, IsEqual
       from typing import Annotated   # <--------------- if Python ≥ 3.9.0
       # from typing_extensions import Annotated   # <-- if Python < 3.9.0

       # Generalize this to other boto3 types by copy-and-pasting this and
       # replacing the base type and "s3.Bucket" with the wonky runtime names
       # of those types. Sadly, there is no one-size-fits all common base class,
       # but you should find what you need in the following places:
       # * "boto3.resources.base.ServiceResource".
       # * "boto3.resources.collection.ResourceCollection".
       # * "botocore.client.BaseClient".
       # * "botocore.paginate.Paginator".
       # * "botocore.waiter.Waiter".
       Bucket = Annotated[ServiceResource,
           IsAttr['__class__', IsAttr['__name__', IsEqual["s3.Bucket"]]]]

   # Do this for the good of the gross domestic product, @beartype.
   @beartype
   def get_s3_bucket_example() -> Bucket:
       s3 = resource('s3')
       return s3.Bucket('example')

You're welcome.

...NumPy arrays?
~~~~~~~~~~~~~~~~

Beartype fully supports `typed NumPy arrays <NumPy Type Hints_>`__. Because
beartype cares.

...mock types?
~~~~~~~~~~~~~~

Beartype fully relies upon the `isinstance() builtin <isinstance_>`__ under the
hood for its low-level runtime type-checking needs. If you can fool
``isinstance()``, you can fool beartype. Can you fool beartype into believing
an instance of a mock type is an instance of the type it mocks, though?

**You bet your bottom honey barrel.** In your mock type, just define a new
``__class__()`` property returning the original type: e.g.,

.. code-block:: python

   >>> class OriginalType: pass
   >>> class MockType:
   ...     @property
   ...     def __class__(self) -> OriginalType: return OriginalType
   >>> from beartype import beartype
   >>> @beartype
   ... def muh_func(self, muh_arg: OriginalType): print('Yolo, bro.')
   >>> muh_func(MockType())
   Yolo, bro.

This is why we beartype.

...under VSCode?
~~~~~~~~~~~~~~~~

**Beartype fully supports VSCode out-of-the-box** – especially via Pylance_,
Microsoft's bleeding-edge Python extension for VSCode. Chortle in your joy,
corporate subscribers and academic sponsors! All the intellisense you can
tab-complete and more is now within your honey-slathered paws. Why? Because...

Beartype laboriously complies with pyright_, Microsoft's in-house static
type-checker for Python. Pylance_ enables pyright_ as its default static
type-checker. Beartype thus complies with Pylance_, too.

Beartype *also* laboriously complies with mypy_, Python's official static
type-checker. VSCode users preferring mypy_ to pyright_ may switch Pylance_ to
type-check via the former. Just:

#. `Install mypy <mypy install_>`__.
#. `Install the VSCode Mypy extension <VSCode Mypy extension_>`__.
#. Open the *User Settings* dialog.
#. Search for ``Type Checking Mode``.
#. Browse to ``Python › Analysis: Type Checking Mode``.
#. Switch the "default rule set for type checking" to ``off``.

|VSCode-Pylance-type-checking-setting|

:superscript:`Pretend that reads "off" rather than "strict". Pretend we took
this screenshot.`

There are tradeoffs here, because that's just how the code rolls. On:

* The one paw, pyright_ is *significantly* more performant than mypy_ under
  Pylance_ and supports type-checking standards currently unsupported by mypy_
  (e.g., recursive type hints).
* The other paw, mypy_ supports a vast plugin architecture enabling third-party
  Python packages to describe dynamic runtime behaviour statically.

Beartype: we enable hard choices, so that you can make them for us.

...under [insert-IDE-name-here]?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Beartype fully complies with mypy_, pyright_, `PEP 561`_, and other community
standards that govern how Python is statically type-checked. Modern Integrated
Development Environments (IDEs) support these standards - hopefully including
your GigaChad IDE of choice.

...with type narrowing?
~~~~~~~~~~~~~~~~~~~~~~~

Beartype fully supports `type narrowing`_ with the `PEP 647`_-compliant
typing.TypeGuard_ type hint. In fact, beartype supports type narrowing of *all*
PEP-compliant type hints and is thus the first maximal type narrower.

Specifically, the `procedural beartype.door.is_bearable() function
<is_bearable_>`__ and `object-oriented beartype.door.TypeHint.is_bearable()
method <beartype.door_>`__ both narrow the type of the passed test object (which
can be *anything*) to the passed type hint (which can be *anything*
PEP-compliant). Both soft-guarantee runtime performance on the order of less
than 1µs (i.e., less than one millionth of a second), preserving runtime
performance and your personal sanity.

Calling either `is_bearable() <is_bearable_>`__ *or* `TypeHint.is_bearable()
<beartype.door_>`__ in your code enables beartype to symbiotically eliminate
false positives from static type-checkers checking that code, substantially
reducing static type-checker spam that went rotten decades ago: e.g.,

.. code-block:: python

   # Import the requisite machinery.
   from beartype.door import is_bearable

   def narrow_types_like_a_boss_with_beartype(lst: list[int | str]):
       '''
       This function eliminates false positives from static type-checkers
       like mypy and pyright by narrowing types with ``is_bearable()``.

       Note that decorating this function with ``@beartype`` is *not*
       required to inform static type-checkers of type narrowing. Of
       course, you should still do that anyway. Trust is a fickle thing.
       '''

       # If this list contains integers rather than strings, call another
       # function accepting only a list of integers.
       if is_bearable(lst, list[int]):
           # "lst" has been though a lot. Let's celebrate its courageous story.
           munch_on_list_of_strings(lst)  # mypy/pyright: OK!
       # If this list contains strings rather than integers, call another
       # function accepting only a list of strings.
       elif is_bearable(lst, list[str]):
           # "lst": The Story of "lst." The saga of false positives ends now.
           munch_on_list_of_strings(lst)  # mypy/pyright: OK!

   def munch_on_list_of_strings(lst: list[str]): ...
   def munch_on_list_of_integers(lst: list[int]): ...

Beartype: *because you no longer care what static type-checkers think.*
