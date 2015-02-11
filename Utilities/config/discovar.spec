[CONFIG]
input FASTQ
name discovar 
location cpp/[MACHINE]/discovar/bin
output project_discovar/a.fin/a.fasta
scaffoldOutput project_discovar/a.final/a.fasta
paired PE=p[LIB] [MEAN] [SD] [FIRST] [SECOND]
required PAIRED
commands rm -rf [RUNDIR]/project_discovar && \
         bash fastq_convert_to_bam.sh [RUNDIR] project_discovar [INPUT] && \ 
	 bash run-discovarexp-assembly.sh [RUNDIR]/project_discovar [RUNDIR]/reads.bam
