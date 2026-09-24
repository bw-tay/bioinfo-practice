# Current Learning Roadmap & Working Context

## 1. Learner Profile
- **Academic Background**: Marine Biotechnology & Resources (Wet lab molecular biology experience: PCR, plasmid transfection, E. coli transformation, RNA extraction, enzyme/carbohydrate research).
- **Publication**: 2nd author in *Carbohydrate Polymers*.
- **Target Transition**: Bioinformatics, Computational Biology, Biostatistics, Biomedical Data Science, Healthcare AI.
- **Language**: Prefers Traditional Chinese (繁體中文) for explanations and interaction.

## 2. AI Role Architecture
- **AI Studio (Web Mentor)**: Long-term mentor, learning strategist, curriculum director, conceptual educator, and scientific judge.
- **Claude Code (CLI Partner)**: Local implementation assistant, terminal command executor, code debugger, project file manager, and progressive coding tutor.
- **Learner (User)**: Decision-maker, scientific reasoning owner, and active learner. Avoid passive copy-pasting.

## 3. Overall One-Year Progression
1. **Phase 0 — Environment & Basic Workflow** (COMPLETED)
   - WSL2 / Ubuntu setup, terminal navigation, basic file operations.
   - VS Code integration, Git local repository, GitHub remote repository.
2. **Phase 1 — Python & Computational Thinking** (CURRENT PHASE)
   - Data structures (Strings, Lists, Dictionaries) connected to biological sequences.
   - Flow control (Loops, Conditionals), File I/O (FASTA/FASTQ handling).
   - Functions (`def`), modular code, and introductory Rosalind challenges.
3. **Phase 2 — Data Analysis, Statistics & R** (UPCOMING)
   - NumPy, pandas, matplotlib; Hypothesis testing, p-values, distributions; R & ggplot2/Bioconductor.
4. **Phase 3 — NGS & Bioinformatics Foundations**
   - FASTQ, quality control, read alignment (BAM/SAM), count matrices, DESeq2.
5. **Phase 4 — End-to-End Real Bioinformatics Pipelines**
6. **Phase 5 — SQL, Workflow Managers & Reproducibility**
7. **Phase 6 & 7 — Independent Bioinformatics Project & Machine Learning (KNN, scikit-learn)**

---

## 4. Current Milestone: Phase 1 (Week 1–2 Focus)
- **Current Topic**: Fundamental data structures for biological data.
- **Accomplished So Far**:
  - Reading single-line and multi-line FASTA files using Python file streaming (`for line in file:`).
  - Calculating DNA sequence length and GC Content percentage.
  - Basic dictionary (`dict`) lookup for complement base pairing (`complement_dict`).
  - Understanding safe dictionary lookup using `.get(query, default)`.
- **Immediate Next Tasks**:
  1. Generate the full complementary strand of a DNA sequence using loops and dictionaries.
  2. Implement transcription (DNA -> mRNA).
  3. Reverse complement generation (handling 5' to 3' biological orientation).
  4. Building and parsing complete Codon translation tables.
  5. Refactoring scripts into reusable Python functions (`def`).