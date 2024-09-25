
# Week 6: File Handling

## Objectives:
- Learn how to read from and write to files in Python.
- Use files to store data so it can be saved and used again later.

## Key Concepts:
1. **File I/O**: Input and output from files allow programs to read from or write to files on your computer.
   - **Opening a File**: You can open a file using the `open()` function.
     ```python
     file = open("data.txt", "w")
     ```
   - **Reading/Writing**: Use `file.read()` to read and `file.write()` to write to a file.
2. **Modes**: Files can be opened in different modes, such as `r` (read), `w` (write), or `a` (append).
3. **Closing Files**: It’s important to close files when finished using them.
   ```python
   file.close()
   ```

## Tasks:
1. Create a diary program where users can write entries that are saved to a file and read previous entries.
2. Extend the playlist manager so playlists can be saved and loaded from a file.
