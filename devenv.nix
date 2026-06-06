{ pkgs, lib, config, inputs, ... }:

{
packages = with pkgs; [
	python314
	python314Packages.pygame
];

  scripts.hello.exec = ''
    echo "Hello world"
  '';

}
