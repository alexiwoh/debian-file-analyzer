# debian-file-analyzer
A python command line tool that takes the architecture (amd64, arm64, mips etc.) as an argument and downloads the compressed Contents file associated with it from a Debian mirror. The program parses the file and output the statistics of the top 10 packages that have the most files associated with them.
