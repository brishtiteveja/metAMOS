[CONFIG]
input FASTQ
name allpathslg
output project_allpathslg/data/run/ASSEMBLIES/subdir/final.contigs.fasta
scaffoldOutput project_allpathslg/data/run/ASSEMBLIES/subdir/final.assembly.fasta 
location cpp/[MACHINE]/allpathslg/bin
#threads -n
paired PE = p[LIB] [MEAN] [SD] [FIRST] [SECOND]
mated JUMP = s[LIB] [MEAN] [SD] [FIRST] [SECOND]
required PAIRED
commands rm -rf [RUNDIR]/project_allpathslg && \ 
	 bash preparegrouplib.sh [RUNDIR] project_allpathslg [INPUT] && \ 
         bash prepare.sh [RUNDIR] project_allpathslg [RUNDIR]/in_group.csv [RUNDIR]/in_lib.csv&& \
	 bash assemble.sh [RUNDIR] project_allpathslg 
	 #Example project name: project_allpathslg in run directory
