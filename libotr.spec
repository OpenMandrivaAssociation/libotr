%define major 2
%define libname %mklibname otr %{major}
%define libnamedev %mklibname -d otr

Summary:	Off-The-Record Messaging library and toolkit
Name:		libotr
Version:	3.2.1
Release:	2
License:	LGPL/GPL
Group:		Networking/Instant messaging
URL:		http://www.cypherpunks.ca/otr/
Source0:	http://www.cypherpunks.ca/otr/%{name}-%{version}.tar.gz
Source1:	http://www.cypherpunks.ca/otr/%{name}-%{version}.tar.gz.asc
BuildRequires:	libgcrypt-devel >= 1.2.0

%description
%{name} is a library and toolkit which implements Off-the-Record (OTR)
Messaging.

OTR allows you to have private conversations over IM by providing:
 - Encryption
   - No one else can read your instant messages.
 - Authentication
   - You are assured the correspondent is who you think it is.
 - Deniability
   - The messages you send do _not_ have digital signatures that are
     checkable by a third party.  Anyone can forge messages after a
     conversation to make them look like they came from you.  However,
     _during_ a conversation, your correspondent is assured the messages
     he sees are authentic and unmodified.
 - Perfect forward secrecy
   - If you lose control of your private keys, no previous conversation
     is compromised.

%package	-n %{libname}
Summary:	Off-The-Record Messaging library and toolkit
Group:		Networking/Instant messaging
License:	LGPL
Provides:	%{name} = %{version}-%{release}

%description	-n %{libname}
%{name} is a library and toolkit which implements Off-the-Record (OTR)
Messaging.

OTR allows you to have private conversations over IM by providing:
 - Encryption
   - No one else can read your instant messages.
 - Authentication
   - You are assured the correspondent is who you think it is.
 - Deniability
   - The messages you send do _not_ have digital signatures that are
     checkable by a third party.  Anyone can forge messages after a
     conversation to make them look like they came from you.  However,
     _during_ a conversation, your correspondent is assured the messages
     he sees are authentic and unmodified.
 - Perfect forward secrecy
   - If you lose control of your private keys, no previous conversation
     is compromised.

%package	-n %{libnamedev}
Summary:	Development related files of %{name}
Group:		Networking/Instant messaging
License:	LGPL
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname -d otr 2} < 3.2.1

%description	-n %{libnamedev}
%{name} is a library and toolkit which implements Off-the-Record (OTR)
Messaging. This package contains development related files of %{name}.

%package	utils
Summary:	Helper utilities of %{name}
Group:		Networking/Instant messaging
License:	GPL
Requires:	%{libname} = %{version}

%description	utils
%{name} is a library and toolkit which implements Off-the-Record (OTR)
Messaging. This package contains various helper utilities from %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--with-pic \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS
%{_libdir}/lib*.so.%{major}*

%files -n %{libnamedev}
%doc ChangeLog INSTALL Protocol-v2.html NEWS README
%{_datadir}/aclocal/*.m4
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%files utils
%doc AUTHORS
%{_bindir}/*
%{_mandir}/man?/*


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 3.2.0-5mdv2011.0
+ Revision: 661513
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2.0-4mdv2011.0
+ Revision: 602594
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2.0-3mdv2010.1
+ Revision: 520896
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.2.0-2mdv2010.0
+ Revision: 425685
- rebuild

* Sat Jun 21 2008 Funda Wang <fwang@mandriva.org> 3.2.0-1mdv2009.0
+ Revision: 227777
- New version 3.2.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 3.1.0-1mdv2008.1
+ Revision: 136557
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 06 2007 Götz Waschk <waschk@mandriva.org> 3.1.0-1mdv2008.0
+ Revision: 59267
- new version
- new devel name
- Import libotr



* Wed Jul 05 2006 Thierry Vignaud <tvignaud@mandriva.com> 3.0.0-2mdv2007.0
- fix group

* Fri Nov 18 2005 Abel Cheung <deaddog@mandriva.org> 3.0.0-1mdk
- New release

* Wed Jun 29 2005 Abel Cheung <deaddog@mandriva.org> 2.0.2-1mdk
- First Mandriva package, based on packaging from master site
