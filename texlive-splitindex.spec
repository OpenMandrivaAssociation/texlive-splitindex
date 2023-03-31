Name:		texlive-splitindex
Version:	39766
Release:	2
Summary:	Unlimited number of indexes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/splitindex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/splitindex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/splitindex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/splitindex.source.r%{version}.tar.xz
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
%{_texmfdistdir}/scripts/splitindex
%{_texmfdistdir}/tex/generic/splitindex
%{_texmfdistdir}/tex/latex/splitindex
%doc %{_texmfdistdir}/doc/latex/splitindex
%doc %{_mandir}/man1/splitindex.1*
%doc %{_texmfdistdir}/doc/man/man1/splitindex.man1.pdf
#- source
%doc %{_texmfdistdir}/source/latex/splitindex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/splitindex/splitindex.pl splitindex
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
