# AI Agent Project - Learning Objectives

## Functional Programming Mini-Quests

### 1. Prefer Pure Functions
- [ ] Every tool function (list files, read file, write file, run python) takes inputs
      and returns outputs with no hidden side effects.
- [ ] State lives at the edges (main loop), not buried inside helper functions.

    **Lesson opportunities:**
    - Ch2: Calculator App — your first tool function. Resist the urge to print inside it;
    return the result and let the caller decide what to do with it.
    - Ch2: List Files, Get File Content, Write Files, Run Python — each one is a chance
    to ask "does this function do exactly one thing and nothing else?"
    - Ch4: Agent Loop — this is where side effects (printing, API calls) belong.
    Keep them here and out of your tools.

---

### 2. Spot and Apply Function Composition
- [ ] When two or more operations are always chained together, compose them into
      a single pipeline rather than repeating the chain at call sites.
- [ ] Ask yourself: "Is this a sequence of transformations on data?" If yes, compose.

    **Lesson opportunities:**
    - Ch2: Validate Paths + List Files — path validation and directory listing are
    naturally sequential. Can you compose them rather than nesting them?
    - Ch3: Function Declaration + More Declarations — building the tool schema is a
    transformation from a Python function definition into a dict structure.
    Can you express that as a pipeline?
    - Ch4: Agent Loop — the loop itself is a composition of: get response -> parse tool
    call -> dispatch -> append result. Model it as a chain of transforms.

---

### 3. Use Higher-Order Functions Deliberately
- [ ] At least once, pass a function as an argument instead of using a conditional
      to select behaviour (e.g. dispatching tool calls).
- [ ] Identify one place where `map`, `filter`, or `functools.reduce` replaces an
      explicit loop.

    **Lesson opportunities:**
    - Ch2: List Files — filtering directory contents by type is a natural `filter` moment.
    - Ch3: Calling Functions — dispatching a tool call by name is a classic use case for
    a dict of `{name: function}` rather than a chain of `if/elif` statements.
    - Ch4: Agent Loop — building the message history from a list of tool results is a
    natural `map` moment.

---

### 4. Apply Currying / Partial Application Where It Reduces Noise
- [ ] If a function is repeatedly called with the same first argument(s), use
      `functools.partial` (or a closure) to pre-fill those arguments.
- [ ] Rule of thumb: if you find yourself writing a lambda just to fix an argument,
      reach for `partial` instead.

    **Lesson opportunities:**
    - Ch2: Validate Paths — the working directory is a fixed argument passed repeatedly
    to every tool. Consider partially applying it once at startup rather than
    threading it through every call.
    - Ch3: Calling Functions — when you build your tool dispatch map, `partial` can
    pre-bind the working directory into each tool function so the LLM-facing
    dispatcher only needs to pass the LLM-supplied arguments.
    - Ch4: Agent Loop — if you find yourself passing the same config (model name, system
    prompt) into every API call, that is a signal to partially apply it once.

---

### 5. Use Decorators for Cross-Cutting Concerns
- [ ] Identify at least one concern that applies to multiple functions uniformly
      (e.g. logging a function call, validating a path, timing execution).
- [ ] Implement it as a decorator rather than copy-pasting the logic.

    **Lesson opportunities:**
    - Ch2: List Files, Get File Content, Write Files, Run Python — all four tools need
    path validation. Instead of repeating the check inside each function, write a
    single `@validate_path` decorator and apply it to all four.
    - Ch1: Verbose Output — the verbose flag controls whether tool calls are printed.
    A `@log_if_verbose` decorator keeps that concern out of your tool logic entirely.
    - Ch3: Calling Functions — error handling around tool execution (catching exceptions
    and returning a structured error message) is another uniform concern that sits
    cleanly in a decorator.

---

### 6. Keep Data Transformations Explicit
- [ ] Message history is built by returning new lists, not by mutating a shared list
      inside helper functions.
- [ ] Tool results are transformed into the expected message format in one clear place.

    **Lesson opportunities:**
    - Ch1: Multiple Messages — this is the first time you build a message list.
    Establish the pattern of returning a new list (`[*messages, new_message]`)
    rather than calling `.append()` inside a helper.
    - Ch3: Calling Functions — converting a raw tool result into the message format the
    API expects is a pure transformation. Isolate it in a single function.
    - Ch4: Agent Loop — the loop accumulates history. If each iteration returns a new
    list rather than mutating a shared one, the data flow stays readable.

---

### 7. Minimise Verbosity
- [ ] After finishing each chapter, review your code and ask:
      "Can any block of 5+ lines be replaced by a single expression or a composed call?"
- [ ] Aim for functions that fit on one screen without scrolling.

    **Lesson opportunities:**
    - End of Ch2 — review all six tool functions together. Are any of them doing
    something another one already does?
    - End of Ch3 — review your function declaration schema builder. Is it a loop that
    could be a list comprehension?
    - End of Ch4 — do a final pass on the agent loop. Count your lines of state mutation;
    each one is a candidate for elimination.

---

## Course Chapters (for reference)
1. LLMs - API setup, token metadata, message history
2. Functions - the agent's tool implementations
3. Function Calling - wiring tools to the LLM
4. Agents - the main agent loop