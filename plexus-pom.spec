%_javapackages_macros
Name:          plexus-pom
Version:       3.3.1
Release:       5.0%{?dist}
Summary:       Root Plexus Projects POM

License:       ASL 2.0
URL:           https://github.com/sonatype/%{name}/
Source0:       https://github.com/sonatype/plexus-pom/archive/plexus-%{version}.tar.gz
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: spice-parent

%description
The Plexus project provides a full software stack for creating and
executing software projects.  This package provides parent POM for
Plexus packages.

%prep
%setup -q -n plexus-pom-plexus-%{version}
# require: maven-site-plugin *
%pom_xpath_remove "pom:profile[pom:id='maven-3']"
# * require: org.codehaus.plexus plexus-stylus-skin 1.0
# org.apache.maven.wagon wagon-webdav-jackrabbit 1.0
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin

%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.codehaus.mojo:taglist-maven-plugin
cp -p %{SOURCE1} LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE
