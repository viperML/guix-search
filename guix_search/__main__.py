import httpx
import json
import argparse
from ansi.color import fg
from textwrap import indent


def main():
    parser = argparse.ArgumentParser("guix-search")
    parser.add_argument("query")
    parser.add_argument("-l", "--limit", default=20)
    parser.add_argument("-S", "--symbol", action="store_true")

    args = parser.parse_args()

    base = "https://toys.whereis.social"
    headers={"User-Agent": "curl/8.9.1", "Content-Type": "application/json"},

    if args.symbol:
        r = httpx.get(
            f"{base}/api/symbols?search={args.query}&page=1&limit={args.limit}",
            headers=headers,
        )
    else:
        r = httpx.get(
            f"{base}/api/packages?search={args.query}&page=1&limit={args.limit}",
            headers=headers,
        )

    res = json.loads(r.text)

    res = [elem for elem in res]
    res.reverse()

    print("Most relevant results at the bottom\n\n")

    for elem in res:
        if args.symbol:
            print(f"{fg.blue}{elem['signature']}{fg.default}")
            print(f"  Module: {fg.brightblack}({elem['module']}){fg.default}", end="")
            if elem["channel"] != "guix":
                print(f"@ {elem['channel']}", end="")
            print()
            doc = indent(elem['doc'], 4*" ")
            print(f"  Description:\n{fg.brightblack}{doc}{fg.default}")
            print()

        else:
            print(fg.blue, elem["name"], fg.default, end=" ", sep="")
            print("(", fg.green, elem["version"], fg.default, ")", sep="")
            print(f"  Synopsis: {fg.brightblack}{elem['synopsis']}{fg.default}")
            print(f"  Homepage: {fg.brightblack}{elem['homepage']}{fg.default}")
            print(f"  Module: {fg.brightblack}({elem['module']}){fg.default}", end=" ")
            if elem["channel"] != "guix":
                print(f"@ {elem['channel']}", end="")
            print()
            print()


if __name__ == "__main__":
    main()
