Name:          plexus-pom
Version:       27
Release:       1
Summary:       Root Plexus Projects POM

License:       ASL 2.0
URL:           https://github.com/codehaus-plexus/plexus-pom
Source0:       https://github.com/codehaus-plexus/plexus-pom/archive/refs/tags/plexus-%{version}.tar.gz
Source1:       https://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:     noarch
BuildSystem:	maven
BuildOption:	validate

%description
The Plexus project provides a full software stack for creating and
executing software projects.  This package provides parent POM for
Plexus packages.

%prep
%setup -q -n plexus-pom-plexus-%{version}
cp -p %{SOURCE1} LICENSE

%files -f .mfiles
%doc LICENSE README.md
