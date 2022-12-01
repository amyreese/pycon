### Abstract

Consistent formatting and code style is a key component of readable and maintainable code, but enforcing it on a rapidly growing codebase can be daunting. No one wants to review or even think about code style, but everyone appreciates code that is well formatted and follows best practices. The hard part is keeping it that way!

We'll look at general tactics for safely modifying code at scale and enforcing positive code style, while minimizing both the risk to a production codebase and the level of effort needed to maintain it. We'll approach these topics from the lens of a large monorepo, but everything discussed will be equally useful and applicable to open source projects, big and small!

### Description

We'll start the talk by looking at what defines a healthy codebase, from simple formatting and code style to tech debt and deprecated code. We'll cover the difficulties traditionally associated with maintaining code health, particularly within large projects and monorepos. We'll set some basic goals for automating code changes, and how that benefits the overall health of the codebase and makes developers more productive in the long term.

The first piece of the puzzle is general code formatting. We'll talk about black, how it uses syntax trees to guarantee robust and safe changes, and how we can maintain consistent formatting even when developers are actively committing unformatted code. We'll look at sorting imports and other collection literals, and the unique dangers this poses in a Python codebase. We'll see how those risks can be mitigated with robust design, and break down the open source tool called µsort, which we use to sort imports at scale in our own large monorepo.

Then we'll dive into the deep end and discuss linters and codemods that can automatically provide suggested changes, and how to build intelligent, targeted lint rules. We'll showcase tools, including LibCST and Fixit, which use a concrete syntax tree to automate fixes and codemods, and look at how they can empower developers to reduce tech debt and make sweeping improvements to the entire codebase.

We'll finish with a high level discussion of tactics and strategies to deploy all of these tools in codebases both big and small, and how to automate their usage without endangering production, burdening developers, or overloading testing infrastructure.

### Notes

**Audience**

This talk is primarily targeted towards developers maintaining codebases with many contributors, especially monorepos, but all of the tools discussed are equally applicable to small projects. 

**Experience**

Many of these tools are ones that I have built or contributed to, and the advice comes from my experience in a language foundation team supporting Python developers at a large tech company.

**Outline (25 minutes)**

- Introduction (4 minutes)
	- code health and monorepos
	- safety requirements needed
	- goals for automation
- Code formatting (4 minutes)
	- how does black work
	- why a CST makes this safe
	- keeping code formatted
	- dealing with generated code
- Import sorting (7 minutes)
	- why this is risky
	- how can we do this safely
	- introduce µsort, how it works
	- combine with black -> µfmt
- Linting (6 minutes)
	- different types of lint rules
	- focus on rules with fixes
	- introduce Fixit, how it works
	- examples of custom lint rules
	- transforming lint into codemods
- Tactics (4 minutes)
	- how to apply changes safely
	- keeping change sets small
	- minimizing code churn

---

### Initial Ideas

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