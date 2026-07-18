%global tl_name splitindex
%global tl_revision 79618
%global tl_bin_links splitindex:%{_texmfdistdir}/scripts/splitindex/splitindex.pl

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2c
Release:	%{tl_revision}.1
Summary:	Unlimited number of indexes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/splitindex
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/splitindex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/splitindex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/splitindex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(splitindex.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
SplitIndex consists of a LaTeX package, splitidx, and a small program,
splitindex. The package may be used to produce one index or several
indexes. Without splitindex (for example, using the index package), the
number of indexes is limited by the number of TeX's output streams. But
using the program you may use even more than 16 indexes: splitidx
outputs only a single file \jobname.idx and the program splits that file
into several raw index files and calls your favorite index processor for
each of the files.

