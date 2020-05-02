# Regular Expressions Cheatsheet
| Operator | Behaviour |
|----------|-----------|
|`.` | Wildcard, matches *any* character |
| `^abc`| Matches some pattern *abc* at the start of a string |
| `abc$` | Matches some pattern *abc* at the end of a string |
| `[abc]` | Matches one of a set of characters |
| `[A-Z0-9]` | Matches one of a range of characters |
| `ed|ing|s` | Matches one of the specified strings (disjunction) |
| `*` | Zero or more of previous items, e.g. `a*`, `[a-z]*` (also known as *Kleene Closure* |
| `+` | One or more of previous item, e.g. `a+`, `[a-z]+` |
| `?` | Zero or one of the previous item (i.e. optional), e.g. `a?`, `[a-z]?`
| `{n}` | Exactly *n* repeats where *n* is a non-negative integer |
| `{n,}` | At least *n* repeats |
| `{, n}` | No more than *n* repeats |
| `{m,n}` | At least *m* and no more than *n* repeats |
| `a(b|c)+` | Parentheses that indicate the scope of the operators |