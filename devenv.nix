{ pkgs, lib, config, inputs, ... }:

{
  packages = with pkgs; [ ruff emmet-language-server ] ++ (with pkgs.python312Packages; [
    python-lsp-server
  ]);

  languages.python = {
    enable = true;
    package = pkgs.python312;
    poetry = {
      enable = true;
      activate.enable = true;
    };
  };
}
