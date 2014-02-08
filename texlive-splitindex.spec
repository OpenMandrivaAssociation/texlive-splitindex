# revision 26313
# category Package
# catalog-ctan /macros/latex/contrib/splitindex
# catalog-date 2012-04-22 23:21:05 +0200
# catalog-license lppl
# catalog-version 1.1a
Name:		texlive-splitindex
Version:	1.1a
Release:	4
Summary:	Unlimited number of indexes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/splitindex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/splitindex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/splitindex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/splitindex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-splitindex.bin = %{EVRD}

%description
SplitIndex consists of a LaTeX package, splitidx, and a small
program, splitindex. The package may be used to produce one
index or several indexes. Without splitindex (for example,
using the index package), the number of indexes is limited by
the number of TeX's output streams. But using the program you
may use even more than 16 indexes: splitidx outputs only a
single file \jobname.idx and the program splits that file into
several raw index files and calls your favorite index processor
for each of the files.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/splitindex
%{_texmfdistdir}/scripts/splitindex/perl/splitindex.pl
%{_texmfdistdir}/tex/latex/splitindex/splitidx.sty
%{_texmfdistdir}/tex/latex/splitindex/splitindex.tex
%doc %{_texmfdistdir}/doc/latex/splitindex/README
%doc %{_texmfdistdir}/doc/latex/splitindex/install.txt
%doc %{_texmfdistdir}/doc/latex/splitindex/splitidx.pdf
%doc %{_mandir}/man1/splitindex.1*
%doc %{_texmfdir}/doc/man/man1/splitindex.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/splitindex/perl/splitindex.pl splitindex
popd

mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
rm -rf %{buildroot}%{_texmfdistdir}/source/
