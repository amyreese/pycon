### Abstract



### Description



### Notes



### Ideas

- problem statement
	- large, mixed use monorepo, millions of files, not all python
	- includes third party code, as well as open source
	- want consistent, automatic formatting and import sorting
	- safe enough to apply without human review
- start with formatting
	- black
	- safety guarantees, validates CST after changes, compares AST before/after
	- opt-in list, "lint" rules to compare formatting on diffs
	- daily formatting codemod applied "off hours" and automatically rebase/merge
- import sorting
	- more difficult, requires changing AST
	- harder to reason about, potentially altering functionality
	- needs awareness of intervening statements, "boundaries", etc
	- existing solutions not based on CST, history of bugs and bad output
	- decided to write our own
- µsort
	- "minimal" import sorter built on top of LibCST
	- CST manipulation, moving elements, guaranteed valid syntax
	- LibCST makes it possible to consistently associate comments with imports
	- combine/merge/dedupe, and even split imports
	- move and reflow elements to fit line length, etc
	- configure "side effect modules" as implicit boundaries
- cautious rollout
	- start with biggest projects, ~30% of monorepo
	- visually reviewed changes to many thousands of files
	- depended on good test coverage across the repo
	- identified ~dozen modules with import time side effects
	- long tail taking too long
	- codemod remaining ~50% at once, flip switch to enforce on diffs
	- one complaint, no breakage
- µfmt
	- atomic formatting and sorting
	- consistent CI results without intermediary failures
	- behaves the same internally and externally
- final result
	- covers all first-party code in monorepo plus instagram
	- format modified files at diff time, but don't enforce it for landing
	- daily "catchup" codemod generated and shipped by robots
	- safe, reliable, fast enough, and low effort code quality wins