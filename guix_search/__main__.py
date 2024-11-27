import httpx
import json
import argparse
from ansi.color import fg


def main():
    parser = argparse.ArgumentParser("guix-search")
    parser.add_argument("query")
    parser.add_argument("-l", "--limit", default=20)

    args = parser.parse_args()

    r = httpx.get(
        f"https://toys.whereis.social/api/packages?search={args.query}&page=1&limit={args.limit}",
        headers={"User-Agent": "curl/8.9.1", "Content-Type": "application/json"},
    )

    res = json.loads(r.text)

    res = [elem for elem in res]
    res.reverse()

    print("Most relevant results at the bottom\n\n")

    for elem in res:
        print(fg.blue, elem["name"], fg.default, end=" ", sep="")
        print("(", fg.green, elem["version"], fg.default, ")", sep="")
        print(f"  Synopsis: {elem['synopsis']}")
        print(f"  Homepage: {elem['homepage']}")
        print(f"  Module: ({elem['module']})", end=" ")
        if elem["channel"] != "guix":
            print(f"@ {elem['channel']}", end="")
        print()
        print()


if __name__ == "__main__":
    main()
