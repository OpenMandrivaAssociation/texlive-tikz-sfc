%global tl_name tikz-sfc
%global tl_revision 49424

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	Symbols collection for typesetting Sequential Function Chart (SFC) diagrams (...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-sfc
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-sfc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-sfc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package contains a collection of symbols for typesetting Sequential
Function Chart (SFC) diagrams in agreement with the international
standard IEC-61131-3/2013. It includes steps (normal and initial),
transitions, actions and actions qualifiers (with and without time
duration). It extends the circuit library of TikZ and allows you to draw
an SFC diagram in same way you would draw any other circuit.

