# HW1
It's the first homework of Natural Language Processing course in Spring 2024 at Sharif University of Technology. The project focuses on preprocessing and performing various NLP tasks on different datasets.

## Project Overview
Each team member was assigned to process specific Persian or English data, either obtained through web crawling or using pre-existing datasets. Depending on the dataset's characteristics and the target processing task, we performed the necessary preprocessing steps followed by the main processing tasks.

## Directory Structure and Tasks
- `Zoomit - KeyPhrase Extraction`:  
  **Contributor**: [Ilia Hashemi Rad](https://github.com/IliaHashemiRad)

  This directory contains:
  - **Data Source**: Persian data crawled from the [Zoomit](https://www.zoomit.ir/) website.
  - **Scripts and Processing**: Includes the crawling script and subsequent key phrase extraction tasks.
 
  
- `Poem - KeyPhrase Extraction & Poem to Clear Sentence`:  
  **Contributor**: [Amir Mohammad Fakhimi](https://github.com/AmirMohammadFakhimi)

  This directory includes:
  - **Data Source**: Poems by Iranian poets Ferdowsi and Khayyam, crawled from [Ganjoor](https://ganjoor.net).
  - **Preprocessing Steps**:
    - Performed normalization, tokenization, removal of stopwords, etc.
    - Categorized Shahnameh by Ferdowsi based on its chapters.
    - Compared stopwords between chapters of Shahnameh and with Khayyam's poems.
  - **Processing Tasks**:
    - **KeyPhrase Extraction**: Extracted key phrases from Khayyam and Ferdowsi's "Shahname" using the `yake` library.
    - **Converting Poems to Clear Sentences**:
      - Used the `hazm` library POSTagger to tag each stanza.
      - Sorted the tagged stanzas based on Persian grammar to form coherent sentences, employing a somewhat greedy approach.


This README provides an overview of the project, detailing the datasets used, preprocessing steps, and specific NLP tasks performed by each contributor. For further details, please refer to the respective directories and scripts.
