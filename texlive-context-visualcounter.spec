Name:		texlive-context-visualcounter
Version:	47085
Release:	1
Summary:	Visual display of ConTeXt counters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/context-visualcounter
License:	bsd2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-visualcounter.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-visualcounter.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-visualcounter.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A typical document usually contains many counters: page
numbers, section numbers, itemizations, enumerations, theorems,
and so on. This module provides a visual display for such
counters.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/source
%doc %{_texmfdistdir}/source/context
%doc %{_texmfdistdir}/source/context/third
%doc %{_texmfdistdir}/source/context/third/visualcounter
%doc %{_texmfdistdir}/source/context/third/visualcounter/visualcounter.tex
%doc %{_texmfdistdir}/source/context/third/visualcounter/p-documentation.tex
%{_texmfdistdir}/tex
%{_texmfdistdir}/tex/context
%{_texmfdistdir}/tex/context/third
%{_texmfdistdir}/tex/context/third/visualcounter
%{_texmfdistdir}/tex/context/third/visualcounter/t-visualcounter.mkvi
%{_texmfdistdir}/doc
%doc %{_texmfdistdir}/doc/context
%doc %{_texmfdistdir}/doc/context/third
%doc %{_texmfdistdir}/doc/context/third/visualcounter
%doc %{_texmfdistdir}/doc/context/third/visualcounter/visualcounter.pdf
%doc %{_texmfdistdir}/doc/context/third/visualcounter/VERSION

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
