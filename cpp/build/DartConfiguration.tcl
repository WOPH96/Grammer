# This file is configured by CMake automatically as DartConfiguration.tcl
# If you choose not to use CMake, this file may be hand configured, by
# filling in the required variables.


# Configuration directories and files
<<<<<<< HEAD
SourceDirectory: /mnt/c/Users/ywonp/Documents/study/grammer/cpp
BuildDirectory: /mnt/c/Users/ywonp/Documents/study/grammer/cpp/build
=======
SourceDirectory: /Users/yang-wonphil/Desktop/study/Grammer/cpp
BuildDirectory: /Users/yang-wonphil/Desktop/study/Grammer/cpp/build
>>>>>>> 2e240878808e7e91ef91553eeab27445953b4766

# Where to place the cost data store
CostDataFile: 

# Site is something like machine.domain, i.e. pragmatic.crd
Site: DESKTOP-JF08IT6

# Build name is osname-revision-compiler, i.e. Linux-2.4.2-2smp-c++
BuildName: Linux-x86_64-linux-gnu-g++-7

# Subprojects
LabelsForSubprojects: 

# Submission information
IsCDash: 
CDashVersion: 
QueryCDashVersion: 
DropSite: 
DropLocation: 
DropSiteUser: 
DropSitePassword: 
DropSiteMode: 
DropMethod: http
TriggerSite: 
ScpCommand: /usr/bin/scp

# Dashboard start time
NightlyStartTime: 00:00:00 EDT

# Commands for the build/test/submit cycle
<<<<<<< HEAD
ConfigureCommand: "/usr/bin/cmake" "/mnt/c/Users/ywonp/Documents/study/grammer/cpp"
MakeCommand: /usr/bin/cmake --build . --config "${CTEST_CONFIGURATION_TYPE}" -- -i
=======
ConfigureCommand: "/opt/homebrew/Cellar/cmake/3.22.2/bin/cmake" "/Users/yang-wonphil/Desktop/study/Grammer/cpp"
MakeCommand: /opt/homebrew/Cellar/cmake/3.22.2/bin/cmake --build . --config "${CTEST_CONFIGURATION_TYPE}" -- -i
>>>>>>> 2e240878808e7e91ef91553eeab27445953b4766
DefaultCTestConfigurationType: Release

# version control
UpdateVersionOnly: 

# CVS options
# Default is "-d -P -A"
CVSCommand: CVSCOMMAND-NOTFOUND
CVSUpdateOptions: -d -A -P

# Subversion options
SVNCommand: SVNCOMMAND-NOTFOUND
SVNOptions: 
SVNUpdateOptions: 

# Git options
GITCommand: /usr/bin/git
GITInitSubmodules: 
GITUpdateOptions: 
GITUpdateCustom: 

# Perforce options
P4Command: P4COMMAND-NOTFOUND
P4Client: 
P4Options: 
P4UpdateOptions: 
P4UpdateCustom: 

# Generic update command
UpdateCommand: 
UpdateOptions: 
UpdateType: 

# Compiler info
<<<<<<< HEAD
Compiler: /usr/bin/x86_64-linux-gnu-g++-7
CompilerVersion: 7.5.0
=======
Compiler: /usr/bin/clang++
CompilerVersion: 13.1.6.13160021
>>>>>>> 2e240878808e7e91ef91553eeab27445953b4766

# Dynamic analysis (MemCheck)
PurifyCommand: 
ValgrindCommand: 
ValgrindCommandOptions: 
MemoryCheckType: 
MemoryCheckSanitizerOptions: 
MemoryCheckCommand: MEMORYCHECK_COMMAND-NOTFOUND
MemoryCheckCommandOptions: 
MemoryCheckSuppressionFile: 

# Coverage
CoverageCommand: /usr/bin/gcov
CoverageExtraFlags: -l

# Cluster commands
SlurmBatchCommand: SLURM_SBATCH_COMMAND-NOTFOUND
SlurmRunCommand: SLURM_SRUN_COMMAND-NOTFOUND

# Testing options
# TimeOut is the amount of time in seconds to wait for processes
# to complete during testing.  After TimeOut seconds, the
# process will be summarily terminated.
# Currently set to 25 minutes
TimeOut: 1500

# During parallel testing CTest will not start a new test if doing
# so would cause the system load to exceed this value.
TestLoad: 

UseLaunchers: 
CurlOptions: 
# warning, if you add new options here that have to do with submit,
# you have to update cmCTestSubmitCommand.cxx

# For CTest submissions that timeout, these options
# specify behavior for retrying the submission
CTestSubmitRetryDelay: 5
CTestSubmitRetryCount: 3
