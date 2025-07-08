# Syntax & Indentation Error Fixing Checklist: env_validator.py

This document tracks the detailed process for fixing syntax and indentation errors in `env_validator.py` as part of the Lavagante project organization and code quality roadmap.

---

## File: `config/env_validator.py`

### Error Summary
- **Error:** `unindent does not match any outer indentation level`
- **Location:** See error output (e.g., line 127)
- **Likely Causes:**
  - Inconsistent use of tabs and spaces
  - Misaligned code blocks (functions, loops, conditionals)
  - Unclosed or improperly indented code blocks

---

## Step-by-Step Fixing Checklist

- [x] **Backup original file**
    - Used backup utility or manual copy
- [x] **Check for inconsistent use of tabs and spaces**
    - Searched for mixed indentation
    - Converted all tabs to spaces (PEP8: 4 spaces per indent)
- [x] **Ensure all code blocks have consistent indentation**
    - Inspected all function, loop, and conditional blocks
    - Fixed any misaligned code
- [x] **Verify all function definitions and loops have proper indentation**
    - Checked for missing/extra indents after `def`, `for`, `if`, etc.
- [x] **Run `black` on the fixed file to validate**
    - Command: `black config/env_validator.py`
    - Confirmed no errors
- [x] **Run syntax validation utility**
    - Used `utilities/validate_python_file.py` to check for syntax errors
- [x] **Document fixes in error tracking**
    - Updated `docs/error_tracking.md` with details

---

## Fixes Applied
- Converted all tabs to spaces
- Fixed indentation in all code blocks
- Verified all function and loop headers are followed by properly indented code
- Ran `black` and confirmed formatting
- Ran syntax validation utility (no errors)

---

## Verification
- [x] File imports without error
- [x] Passes syntax validation
- [x] Passes formatting with `black`
- [x] Documented in error tracking

---

## Notes & Best Practices
- Always use 4 spaces per indentation level (no tabs)
- Run `black` and syntax validation after each fix
- Document all changes for future reference

---

## Next Steps
- Continue with next high-priority file: `src/testing/test_qa_system.py`
- Repeat checklist and documentation process
