let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-22.11";
  pkgs = import nixpkgs {
    config = { };
    overlays = [ ];
  };

in pkgs.mkShell {
  packages = with pkgs; [
    (pkgs.python3.withPackages (ps: with ps; [
      pillow
    ]))];

  shellHook = ''
  '';
}
