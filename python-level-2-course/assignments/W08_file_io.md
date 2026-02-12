# Week 8 – File I/O (PCAP 5.4–5.5)

**Module**: M08  
**Mini Project**: [mp08 File Persistence](../projects/mp08_file_persistence/)

## Learning focus

- I/O modes; open(); text vs binary; read(), write(), readline(), readlines(); errno; bytearray as buffer.

## Reading

- [M08 – File I/O](../modules/M08_File_IO.md)
- M08_Concepts.ipynb.

## Practice

1. Open file for writing, write a line, close; open for reading, read back.
2. Catch OSError and print e.errno; compare to errno.ENOENT.
3. Use with open(...) as f: f.readlines().

## Mini project

1. Read mp08 README. Implement save_text/load_text with OSError handling.
2. Save and load; try loading nonexistent file; confirm no crash.

## Checklist

- [ ] open(), read/write used
- [ ] Missing file handled (errno or try/except)
- [ ] Files closed (or with statement)
- [ ] mp08 save/load works
