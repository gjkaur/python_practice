"""Practice: Strings (PCAP 3.1-3.3).

Complete the functions. Run main() to test.
"""


def ord_chr_roundtrip(s: str) -> tuple[int, str]:
    """Return (ord(first char), chr(ord(first char)))."""
    if not s:
        raise ValueError("string must be non-empty")
    code = ord(s[0])
    return (code, chr(code))


def join_with_separator(words: list[str], sep: str) -> str:
    """Join words with sep (e.g. join_with_separator(['a','b','c'], '-') -> 'a-b-c')."""
    return sep.join(words)


def split_and_join(s: str, split_on: str, join_with: str) -> str:
    """Split s on split_on, then join the parts with join_with. E.g. 'a b c' split on ' ' join with '-' -> 'a-b-c'."""
    return join_with.join(s.split(split_on))


def find_first_last(s: str, sub: str) -> tuple[int, int]:
    """Return (s.find(sub), s.rfind(sub))."""
    return (s.find(sub), s.rfind(sub))


def main() -> None:
    print("ord_chr_roundtrip('A'):", ord_chr_roundtrip("A"))
    print("join_with_separator(['a','b','c'], '-'):", join_with_separator(["a", "b", "c"], "-"))
    print("split_and_join('one two three', ' ', '-'):", split_and_join("one two three", " ", "-"))
    print("find_first_last('sub and sub', 'sub'):", find_first_last("sub and sub", "sub"))


if __name__ == "__main__":
    main()
