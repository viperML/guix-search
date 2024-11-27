{
  buildPythonPackage,
  lib,
  setuptools-scm,
  httpx,
  ansi,
}:
buildPythonPackage {
  name = "guix-search";
  src = lib.cleanSource ./.;
  build-system = [
    setuptools-scm
  ];
  pyproject = true;
  dependencies = [
    httpx
    ansi
  ];
}
