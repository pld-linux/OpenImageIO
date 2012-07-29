# to bootstrap: build OpenColorIO --without oiio, build OpenImageIO, rebuild OpenColorIO
#
# Conditional build:
%bcond_without	ocio		# OpenColorIO support in library
%bcond_without	static_libs	# don't build static libraries
%bcond_without	tbb		# Threading Building Blocks
#
Summary:	Library for reading and writing images
Summary(pl.UTF-8):	Biblioteka do odczytu i zapisu obrazów
Name:		OpenImageIO
Version:	1.0.7
Release:	3
License:	BSD
Group:		Libraries
Source0:	https://github.com/OpenImageIO/oiio/tarball/Release-%{version}#/%{name}-%{version}.tar.gz
# Source0-md5:	e939f97db2b0cac813c9e166f2353fe6
Patch0:		%{name}-link.patch
Patch2:		%{name}-hdf.patch
Patch3:		%{name}-system-squish.patch
Patch4:		%{name}-system-ptex.patch
Patch5:		%{name}-system-dpx.patch
Patch6:		%{name}-system-libcineon.patch
Patch7:		no-gcc-atomics.patch
URL:		https://sites.google.com/site/openimageio/home
BuildRequires:	Field3D-devel
%{?with_ocio:BuildRequires:	OpenColorIO-devel}
BuildRequires:	OpenEXR-devel >= 1.6.1
BuildRequires:	OpenGL-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtOpenGL-devel
# filesystem, regex, system, thread
BuildRequires:	boost-devel >= 1.35
BuildRequires:	boost-python-devel >= 1.35
BuildRequires:	cmake >= 2.6
BuildRequires:	dpx-devel
BuildRequires:	glew-devel >= 1.5.1
BuildRequires:	hdf5-devel
BuildRequires:	ilmbase-devel >= 1.0.1
BuildRequires:	libstdc++-devel
BuildRequires:	jasper-devel
BuildRequires:	libcineon-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libwebp-devel
BuildRequires:	pugixml-devel
BuildRequires:	ptex-devel >= 2
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	squish-devel >= 1.10
%{?with_tbb:BuildRequires:	tbb-devel}
BuildRequires:	txt2man
BuildRequires:	zlib-devel
Requires:	ilmbase >= 1.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenImageIO is a library for reading and writing images, and a bunch
of related classes, utilities, and applications. It has extremely
simple but powerful ImageInput and ImageOutput APIs for reading and
writing 2D images that is format agnostic; specific formats are
implemented by DLL/DSO plugins.

Currently there are format plugins for: TIFF, JPEG/JFIF, OpenEXR, PNG,
HDR/RGBE, Targa, JPEG-2000, DPX, Cineon, FITS, BMP, ICO, RMan Zfile,
Softimage PIC, DDS, SGI, PNM/PPM/PGM/PBM, Field3d, WebP.

%description -l pl.UTF-8
OpenImageIO to biblioteka do odczytu i zapisu obrazów oraz wiele
powiązanych klas, narzędzi i aplikacji. Ma bardzo proste, ale mające
wiele możliwości API ImageInput i ImageOutput służące do odczytu i
zapisu obrazów 2D, które jest niezależne od formatu; konkretne formaty
są implementowane przez wtyczki DLL/DSO.

Obecnie istnieją wtyczki obsługujące formaty: TIFF, JPEG/JFIF,
OpenEXR, PNG, HDR/RGBE, Targa, JPEG-2000, DPX, Cineon, FITS, BMP, ICO,
RMan Zfile, Softimage PIC, DDS, SGI, PNM/PPM/PGM/PBM, Field3d, WebP.

%package devel
Summary:	Header files for OpenImageIO library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OpenImageIO
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for OpenImageIO library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OpenImageIO.

%package plugin-cineon
Summary:	Cineon plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka Cineon dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-cineon
OpenImageIO plugin to read Cineon files.

%description plugin-cineon -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca pliki Cineon.

%package plugin-dds
Summary:	DDS plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka DDS dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	squish >= 1.10

%description plugin-dds
OpenImageIO plugin to read DDS files.

%description plugin-dds -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca pliki DDS.

%package plugin-dpx
Summary:	DPX plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka DPX dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-dpx
OpenImageIO plugin to read and write DPX files.

%description plugin-dpx -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki DPX.

%package plugin-field3d
Summary:	Field3D plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka Field3D dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-field3d
OpenImageIO plugin to read Field3D files.

%description plugin-field3d -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca pliki Field3D.

%package plugin-ico
Summary:	ICO plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka ICO dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-ico
OpenImageIO plugin to read and write ICO files.

%description plugin-ico -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki ICO.

%package plugin-jpeg
Summary:	JPEG plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka JPEG dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-jpeg
OpenImageIO plugin to read and write JPEG files (with TIFF/EXIF
information).

%description plugin-jpeg -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki JPEG
(wraz z informacjami TIFF/EXIF).

%package plugin-jpeg2000
Summary:	JPEG2000 plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka JPEG2000 dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-jpeg2000
OpenImageIO plugin to read and write JPEG2000 files.

%description plugin-jpeg2000 -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki JPEG2000.

%package plugin-openexr
Summary:	OpenEXR plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka OpenEXR dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenEXR >= 1.6.1

%description plugin-openexr
OpenImageIO plugin to read and write OpenEXR files.

%description plugin-openexr -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki OpenEXR.

%package plugin-png
Summary:	PNG plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka PNG dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-png
OpenImageIO plugin to read and write PNG files.

%description plugin-png -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki PNG.

%package plugin-psd
Summary:	PSD plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka PSD dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-psd
OpenImageIO plugin to read and write PSD files.

%description plugin-psd -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki PSD.

%package plugin-ptex
Summary:	Ptex plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka Ptex dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ptex >= 2

%description plugin-ptex
OpenImageIO plugin to read Ptex files.

%description plugin-ptex -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca pliki Ptex.

%package plugin-webp
Summary:	WebP plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka WebP dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-webp
OpenImageIO plugin to read and write WebP files.

%description plugin-webp -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki WebP.

%package plugin-tiff
Summary:	TIFF plugin for OpenImageIO library
Summary(pl.UTF-8):	Wtyczka TIFF dla biblioteki OpenImageIO
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-tiff
OpenImageIO plugin to read and write TIFF files.

%description plugin-tiff -l pl.UTF-8
Wtyczka biblioteki OpenImageIO czytająca i zapisująca pliki TIFF.

%package apidocs
Summary:	Programmer documentation for OpenImageIO library
Summary(pl.UTF-8):	Dokumentacja programisty do biblioteki OpenImageIO
Group:		Documentation

%description apidocs
Programmer documentation for OpenImageIO library.

%description apidocs -l pl.UTF-8
Dokumentacja programisty do biblioteki OpenImageIO.

%package iv
Summary:	Qt/OpenImageIO-based Image Viewer
Summary(pl.UTF-8):	Przeglądarka obrazków (IV) oparta o Qt i OpenImageIO
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Requires:	glew >= 1.5.1

%description iv
IV is an image viewer based on ImageIO plugins; therefore it can read
images of any format for which an appropriate plugin may be found.

%description iv -l pl.UTF-8
IV to przeglądarka obrazków oparta na wtyczkach ImageIO; dzięki temu
jest w stanie odczytać obrazy w dowolnym formacie, dla którego
istnieje właściwa wtyczka.

%package -n python-OpenImageIO
Summary:	Python binding for OpenImageIO library
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki OpenImageIO
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-OpenImageIO
Python binding for OpenImageIO library.

%description -n python-OpenImageIO -l pl.UTF-8
Wiązanie Pythona do biblioteki OpenImageIO.

%prep
%setup -q -n OpenImageIO-oiio-e9fa4c7
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%ifarch i486
%patch7 -p1
%endif

%{__rm} -r src/dds.imageio/squish src/ptex.imageio/ptex
# when using system pugixml, don't use hacked headers
%{__rm} src/include/pugi*.hpp

%build
install -d build
cd build
%cmake ../src \
	-DEMBEDPLUGINS=OFF \
	-DINCLUDE_INSTALL_DIR=%{_includedir}/%{name} \
	-DPYLIB_INSTALL_DIR=%{py_sitedir} \
	-DPYTHON_VERSION=%{py_ver} \
	-DUSE_EXTERNAL_PUGIXML=ON \
	%{!?with_ocio:-DUSE_OCIO=OFF} \
	%{!?with_tbb:-DUSE_TBB=OFF}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# name clash with iv
%{__mv} -f $RPM_BUILD_ROOT%{_bindir}/{iv,oiiv}
%{__mv} -f $RPM_BUILD_ROOT%{_mandir}/man1/{iv,oiiv}.1

# installed as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc/openimageio

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS LICENSE README
%attr(755,root,root) %{_bindir}/iconvert
%attr(755,root,root) %{_bindir}/idiff
%attr(755,root,root) %{_bindir}/igrep
%attr(755,root,root) %{_bindir}/iinfo
%attr(755,root,root) %{_bindir}/iprocess
%attr(755,root,root) %{_bindir}/maketx
%attr(755,root,root) %{_bindir}/oiiotool
%attr(755,root,root) %{_libdir}/libOpenImageIO.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOpenImageIO.so.1.0
%attr(755,root,root) %{_libdir}/bmp.imageio.so
%attr(755,root,root) %{_libdir}/fits.imageio.so
%attr(755,root,root) %{_libdir}/hdr.imageio.so
%attr(755,root,root) %{_libdir}/iff.imageio.so
%attr(755,root,root) %{_libdir}/pnm.imageio.so
%attr(755,root,root) %{_libdir}/rla.imageio.so
%attr(755,root,root) %{_libdir}/sgi.imageio.so
%attr(755,root,root) %{_libdir}/socket.imageio.so
%attr(755,root,root) %{_libdir}/softimage.imageio.so
%attr(755,root,root) %{_libdir}/targa.imageio.so
%attr(755,root,root) %{_libdir}/zfile.imageio.so
%{_mandir}/man1/iconvert.1*
%{_mandir}/man1/idiff.1*
%{_mandir}/man1/igrep.1*
%{_mandir}/man1/iinfo.1*
%{_mandir}/man1/iprocess.1*
%{_mandir}/man1/maketx.1*
%{_mandir}/man1/oiiotool.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libOpenImageIO.so
%{_includedir}/OpenImageIO

%files plugin-cineon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cineon.imageio.so

%files plugin-dds
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/dds.imageio.so

%files plugin-dpx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/dpx.imageio.so

%files plugin-field3d
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/field3d.imageio.so

%files plugin-ico
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ico.imageio.so

%files plugin-jpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/jpeg.imageio.so

%files plugin-jpeg2000
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/jpeg2000.imageio.so

%files plugin-openexr
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openexr.imageio.so

%files plugin-png
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/png.imageio.so

%files plugin-psd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/psd.imageio.so

%files plugin-ptex
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ptex.imageio.so

%files plugin-tiff
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/tiff.imageio.so

%files plugin-webp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/webp.imageio.so

%files apidocs
%defattr(644,root,root,755)
%doc src/doc/openimageio.pdf

%files iv
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oiiv
%{_mandir}/man1/oiiv.1*

%files -n python-OpenImageIO
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/OpenImageIO.so
