Name:		texlive-tikz-sfc
Version:	49424
Release:	2
Summary:	Symbols collection for typesetting Sequential Function Chart (SFC) diagrams (PLC programs)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tikz-sfc
License:	lppl1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-sfc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-sfc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains a collection of symbols for typesetting
Sequential Function Chart (SFC) diagrams in agreement with the
international standard IEC-61131-3/2013. It includes steps
(normal and initial), transitions, actions and actions
qualifiers (with and without time duration). It extends the
circuit library of TikZ and allows you to draw an SFC diagram
in same way you would draw any other circuit.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-sfc
%doc %{_texmfdistdir}/doc/latex/tikz-sfc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
