#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-Socket-SSL
Version  : 2.027
Release  : 29
URL      : http://search.cpan.org/CPAN/authors/id/S/SU/SULLR/IO-Socket-SSL-2.027.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/S/SU/SULLR/IO-Socket-SSL-2.027.tar.gz
Summary  : 'Nearly transparent SSL encapsulation for IO::Socket::INET.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-IO-Socket-SSL-doc
BuildRequires : perl(Mozilla::CA)
BuildRequires : perl(Net::SSLeay)

%description
IO::Socket::SSL is a class implementing an object oriented
interface to SSL sockets. The class is a descendent of
IO::Socket::INET.

%package doc
Summary: doc components for the perl-IO-Socket-SSL package.
Group: Documentation

%description doc
doc components for the perl-IO-Socket-SSL package.


%prep
%setup -q -n IO-Socket-SSL-2.027

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.24.0/IO/Socket/SSL.pm
/usr/lib/perl5/site_perl/5.24.0/IO/Socket/SSL.pod
/usr/lib/perl5/site_perl/5.24.0/IO/Socket/SSL/Intercept.pm
/usr/lib/perl5/site_perl/5.24.0/IO/Socket/SSL/PublicSuffix.pm
/usr/lib/perl5/site_perl/5.24.0/IO/Socket/SSL/Utils.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
