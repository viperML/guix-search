{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs?ref=nixos-unstable";
  outputs =
    { self, nixpkgs }:
    {
      packages.x86_64-linux.default =
        nixpkgs.legacyPackages.x86_64-linux.python3.pkgs.callPackage ./package.nix
          { };
    };
}
