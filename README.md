# sc-multi-omics

_memo for single cell multi-omics data and methods; this is a work in progress focusing on single-cell in single omics across different omics layers as well as multi-omics methods and applications, starting at laymen terms in the hopes of building up towards complex notions in the field_

> ✨ "fine.. I'll do it myself" - Thanos 
<!-- 🔷🔴🟨🟢🟪🔶 -->

## Table of Contents

- [Context: sc-omics](#context-sc-omics)
- [Trajectory Inference](#trajectory-inference)
- [Multi-Omics Methodologies](#multi-omics-methodologies)


## Context: sc-omics

**Readings**:
- [x] [Single-cell sequencing techniques from individual to multiomics analyses](https://www.nature.com/articles/s12276-020-00499-2)
- [ ] [The technological landscape and applications of single-cell multi-omics](https://www.nature.com/articles/s41580-023-00615-w)
- [ ] [Considerations for building and using integrated single-cell atlases](https://www.nature.com/articles/s41592-024-02532-y)

### super brief history of single cell

$$DNA \rightarrow RNA \rightarrow Protein$$

The calssical dogma of molecular biology.  
An organism is defined by its genome (DNA), that is present in all the cells that made up tissues, organs, system, and the whole body.  
What makes cells different is the way they use their genome, that is, the way they express their genes through mRNA. RNA is the main molecule that quantifies the expression of a gene and is a necessary intermediary to reach the functional product of the cell, the protein, that will be manifested in the parrticular phenotype of the cell through its function (enzymatic, structural, signaling, etc).

Once upon a time there was bulk sequencing, technology giving birth to high throughput sequncing in transcriptomics - with respect to the CGH micro-array *not-too-convenient* counterpart.
Bulk RNA-seq represents the _average_ quantity of RNA molecules in a sample where the word "bulk" refers to the fact that the sample (most of the times, a patient) is made of many cells, and the sequencing is performed on the whole sample. Thus the quantification is really an avergae expression of genes accross all the cells. 
This has been an outstanding technology leveraging the world of transcriptomics and was mainly used in differential analysis of expression between conditions (e.g., healthy vs disease). But it also has some limitations, most importantly it's low resolution in depicting the heterogeneity of the sample, that is, expression differences between cells.

That was until 2009, when single-cell RNA-seq saw the light, enabling gene expression quantification at single cell resolution. scRNA-seq was named method of the year by Nature Methods in 2013, and since then a plethora of single cell technologies have been developed, namely in epigenomics, proteomics amongs others.

### scRNA-seq

Regardless of the ever increasing number of datasets and applications done so far in scRNA-seq, the technology did not drop out of the sky. It's the outcome of a long series of developments to reach the current state that is less error prone, more scalable and affordable.

In comparison to bulk RNA-seq, sc has a necessary step called "cell dissociation" or cell isolation. Consisting of seperating cells from the tissue, it allows to subsequently capture and sequenece the cellular RNA. 
To measure the transcriptome, similarly to bulk this step consists of reverse transcribing the RNA into cDNA and amplifying it before sequencing.

Several families of methods are availble, oen of which is `Smart-seq` (+ extensions methods) that is a whole-transccriptome amplification (WTA) method. As the name suggests it allows for full length cDNA amplification and hence whole transcriptomce sequencing. However, it is challenging in a sense it's hard to accomodate for a large number of cells and is naturally more expensive for having to sequence the whole transcriptome. 

On the other hand, more scalable methods are "droplet-based" for their reliance on microfluidic droplets to capture and sequence the RNA of a large number of cells. Unlike WTA approaches, they rely on 3'end sequencing (only sequence the 3' end of the transcript). Why? It's mainly because of the polyA tail:  
As the mature mRNA is polyadenulated (ends with AAAAAAAAAA- at the 3' end of the sequence), first there's capture of mRNA molecule through an oligo-dT primer (a TTTTT- primer), then reverse transcription starting there allowing for the capture of the 3' end. The other end however is not captured - and hence the name 3' end sequencing and hence the reason why it's not a WTA method.  It is much more convenient to sequence a large number of cells, cost effective. Not without limitations, it usually present a higher dropout rate, lower RT efficiency and higher amplification bias.

### scATAC-seq

Epigenomics is "above" genomics, as in, it a regulation layer controling expression, without changing the genome itself. Quickly citing main mechanisms of epigenetic regulation: DNA methylation, histone modification, protein-DNA interactions and chromatin accessibility.

With the advent of sequencing there have been techniques to measure each of these mechanisms through a nucleotide-level look at the genome. Of which there is bisulfite sequencing for methylation, ChIP-seq for histone modification and protein-DNA interactions, and ATAC-seq for chromatin accessibility.

Chromatin accessibility describe the state of the chromatin. We have 2 main states: Heterochromatin (closed) and Euchromatin (open). The former is more compacted and less accessible to transcription factors, while the latter is more open and accessible. Studying its status allows the inference of gene activity at a particular locus.  
ATAC-seq (Assay for Transposase-Accessible Chromatin using sequencing) uses a transposase enzyme to cut the DNA at accessible regions and insert sequencing adapters, allowing for the identification of open chromatin regions. scATAC-seq is the single cell version of this technique, allowing for the study of chromatin accessibility at single cell resolution.


### Cell Atlases

*What the hell is an atlas?*  
backstory: there is a multitude of single cell datasets, and they are all different in terms of the tissue, the condition, the technology, the species, etc. Super heterogeneous data, and often times the number of patients per study is super low (study reported median ~14).  
Enters the atlas: integration of various single cell datasets creating a standardized reference.  
Global intiative are underway to create comprehensive atlases of human cells, examples are the Human Cell Atlas (HCA, for all human cell types), Allen Brain Atlas (brain cells in humans and mice), Cancer Cell Atlas (cancer cells), etc.
The idea is to create a reference that can be used for various applications.

To build an atlas:  
The atlas data should abide by severe rules of quality and standardization. First there should be a cler goal for the atlas field of application that will guide the design decisions. Following that datasets should be cherry-picked carefully for inclusion. The more specialized the atlas is, the easier it is to integrate the data and create a high quality atlas. For example, an atlas of a specific tissue (e.g., brain) is easier to build than an atlas of all human cells.  
Afterwards comes rigorous stages of harmonization and preprocessing to unify metadata and account for batch effects.
Preprocessing might actually be dataset-specific. Gene selection is crucial to improve the integration process, with the latter being the most important and challenging step.

## Trajectory Inference

**Readings**:
- [ ] [Computational methods for trajectory inference from single-cell transcriptomics
](https://onlinelibrary.wiley.com/doi/full/10.1002/eji.201646347)

## Multi-Omics Methodologies

**Readings**:
- [ ] [Biological Multi-Layer and Single Cell Network-Based Multiomics Models-a Review](https://arxiv.org/abs/2503.09568)