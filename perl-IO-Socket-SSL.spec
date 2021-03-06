#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-Socket-SSL
Version  : 2.071
Release  : 87
URL      : https://cpan.metacpan.org/authors/id/S/SU/SULLR/IO-Socket-SSL-2.071.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SU/SULLR/IO-Socket-SSL-2.071.tar.gz
Summary  : 'Nearly transparent SSL encapsulation for IO::Socket::INET.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-IO-Socket-SSL-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Mozilla::CA)
BuildRequires : perl(Net::SSLeay)

%description
IO::Socket::SSL is a class implementing an object oriented
interface to SSL sockets. The class is a descendent of
IO::Socket::INET.

%package dev
Summary: dev components for the perl-IO-Socket-SSL package.
Group: Development
Provides: perl-IO-Socket-SSL-devel = %{version}-%{release}
Requires: perl-IO-Socket-SSL = %{version}-%{release}

%description dev
dev components for the perl-IO-Socket-SSL package.


%package perl
Summary: perl components for the perl-IO-Socket-SSL package.
Group: Default
Requires: perl-IO-Socket-SSL = %{version}-%{release}

%description perl
perl components for the perl-IO-Socket-SSL package.


%prep
%setup -q -n IO-Socket-SSL-2.071
cd %{_builddir}/IO-Socket-SSL-2.071

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Socket::SSL.3
/usr/share/man/man3/IO::Socket::SSL::Intercept.3
/usr/share/man/man3/IO::Socket::SSL::PublicSuffix.3
/usr/share/man/man3/IO::Socket::SSL::Utils.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/IO/Socket/SSL.pm
/usr/lib/perl5/vendor_perl/5.34.0/IO/Socket/SSL.pod
/usr/lib/perl5/vendor_perl/5.34.0/IO/Socket/SSL/Intercept.pm
/usr/lib/perl5/vendor_perl/5.34.0/IO/Socket/SSL/PublicSuffix.pm
/usr/lib/perl5/vendor_perl/5.34.0/IO/Socket/SSL/Utils.pm
