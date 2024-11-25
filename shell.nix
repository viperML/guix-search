with import <nixpkgs> { };
mkShell {
  packages = [
    (python3.withPackages (pp: [
      pp.httpx
      pp.python-lsp-server
      pp.black
      pp.ansi
    ]))
    ruff
  ];
}
