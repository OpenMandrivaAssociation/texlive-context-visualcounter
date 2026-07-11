%global tl_name context-visualcounter
%global tl_revision 47085

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Visual display of ConTeXt counters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-visualcounter
License:	bsd2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-visualcounter.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-visualcounter.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-visualcounter.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(context)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A typical document usually contains many counters: page numbers, section
numbers, itemizations, enumerations, theorems, and so on. This module
provides a visual display for such counters.

