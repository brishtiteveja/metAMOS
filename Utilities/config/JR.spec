[CONFIG]
input FASTQ
name jr 
output WORKSPACE/output/project_JR.final.contigs.fasta
scaffoldOutput WORKSPACE/output/project_JR.final.scaffolds.fasta 
location cpp/[MACHINE]/jr/bin
paired PE=p[LIB] [MEAN] [SD] [FIRST] [SECOND]
mated JUMP=s[LIB] [MEAN] [SD] [FIRST] [SECOND]
required PAIRED
commands bash JR_script.sh && \
	 bash run-JR.sh && \
         mv WORKSPACE [RUNDIR]
