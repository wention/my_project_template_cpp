## C and C++ checks

Formatting and static analysis use clang-format and clang-tidy with the repository's
`.clang-format` and `.clang-tidy`. Do not edit those files to make a check pass.

Before you finish a task that changes C or C++ code:

1. Generate the compilation database if `build/compile_commands.json` is missing:
   `cmake -B build -DCMAKE_EXPORT_COMPILE_COMMANDS=ON`
2. Stage your changes and run cpp-linter on the lines you changed:

       git add -A
       GITHUB_ACTIONS=false cpp-linter --version=21 --style=file --tidy-checks='' \
         --database=build --lines-changed-only=true --diff-base=origin/main

   If `origin/main` is missing, run `git fetch origin main` first.
3. Fix every finding it reports. `--fix` applies the clang-format fixes; fix clang-tidy findings
   by hand. Do not add `NOLINT` comments unless the task asks for them.
4. Repeat step 2. You are done when the log ends with `0 checks-failed`.
