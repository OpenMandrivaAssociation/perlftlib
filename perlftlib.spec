Summary:	Libraries to use the FreeType library with Perl
Name:		perlftlib
Version:	1.2
Release:	21mdk
License:	GPL
Group:		Development/Perl
BuildRequires:	freetype-devel perl-devel

Source:		%{name}-%{version}.tar.bz2
Patch:		%{name}-%{version}-mdkconf.patch.bz2
Patch2:		%{name}-%{version}-mdkconf2.patch.bz2
Patch3:		%{name}-%{version}-nojcode.patch.bz2
Patch4:		perlftlib-1.2-perl_pollute.patch.bz2
Patch5:         perlftlib-1.2-handle-DESTDIR.patch.bz2

Requires:	perl
BuildRoot:	%_tmppath/%name-%version-%release-root

%description
This is a package of libraries to use the FreeType library from the perl
language. It contains FreeType.xs and FreeTypeWrapper.pm,
so you don't need install each of them. It also contains ftinfo.pl and
mkttfdir.pl.

%prep

%setup -q
%patch -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
(cd FreeType ; %{__perl} Makefile.PL INSTALLDIRS=vendor)
%make PREFIX=%{_prefix} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/X11R6/man/man1
%makeinstall_std

cp FreeTypeWrapper.pm $RPM_BUILD_ROOT%{perl_vendorarch}
(
cd $RPM_BUILD_ROOT%{_prefix}/X11R6/man/man1/
ln -sf ../../bin/ftinfo ftinfo.1
ln -sf ../../bin/mkttfdir mkttfdir.1
)

#(peroyvind) remove unpackaged files
rm -f $RPM_BUILD_ROOT/usr/lib/perl5/site_perl

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%{_prefix}/X11R6/bin/*
%{_prefix}/X11R6/man/*/*
%{_mandir}/man3/*
%{perl_vendorarch}/FreeType*
%{perl_vendorarch}/auto/FreeType/*

