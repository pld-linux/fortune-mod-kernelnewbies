Summary:	kernelnewbies fortunes
Summary(pl):	Zestaw fortunek kernelnewbies
Name:		fortune-mod-kernelnewbies
Version:	20041003
Release:	1
License:	Public Domain
Group:		Applications/Games
Requires:	fortune-mod
Source0:	http://www.kernelnewbies.org/kernelnewbies-fortunes.tar.gz
# Source0-md5:	73fbc76bfec32d3cc0da326485e7a13d
Patch0:		%{name}-remove_duplicates.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's your
program. Fun-loving system administrators can add fortune to users'
.login files, so that the users get their dose of wisdom each time
they log in.

This package provides set of fortunes collected by kernelnewbies
project.

%description -l pl
Fortune-mod zawiera wci±¿ popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochotê na odrobinê m±dro¶ci przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mog± dodaæ fortune do plików .login u¿ytkowników tak,
by ka¿dy otrzyma³ swoj± dawkê m±dro¶ci przy logowaniu.

Ten pakiet dostarcza zestaw fortunek zebranych w projekcie
kernelnewbies.

%prep
%setup -q -c
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/fortunes

install * $RPM_BUILD_ROOT%{_datadir}/games/fortunes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/fortunes/*
