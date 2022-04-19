<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D

*** Jon Chun 24 Mar 2022 Update

*** REFERENCE: https://github.com/othneildrew/Best-README-Template/blob/master/README.md
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!---
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
--->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/jon-chun/sentiment_arcs">
    <img src="images/sentiment_arcs_logo.jpg" alt="Sentiment Arcs Logo" width="256" height="256">
  </a>

  <h3 align="center">Sentiment Arcs - Emotion in Texts</h3>

  <p align="center">
    An end-to-end pipeline to detect, extract, process and anlayze sentiment analysis time series in long text(s).
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">Quick Video Overview</a>
    ·
    <a href="https://www.cambridge.org/core/what-we-publish/elements/cambridge-elements-series">University of Cambridge Press Elements Textbook by Katherine Elkins</a>
    ·
    <a href="https://github.com/jon-chun/sentiment_arcs/issues">Report a Bug or Request a Feature</a>
    ·
    More Research by <a href="https://arxiv.org/abs/2110.09454">Jon Chun</a> and <a href="https://kenyon.academia.edu/KatherineElkins">Katherine Elkins</a>
    ·
    <a href="https://github.com/jon-chun/sentiment_arcs/affectiveai_links">References on Sentiment Analysis, AffectiveAI and Related Topics</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

<!---
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)
--->

<div align="center">
  <a href="https://github.com/jon-chun/sentiment_arcs">
    <img src="images/graph_sentiment_arcs_ensemble_vwoolf_ttl.png" alt="Sentiment Arcs Ensemble of To The Lighthouse by Virginia Woolf"> 
    <!--- width="2048" height="1018"> --->
  </a>
  <br>
  <a href="https://github.com/jon-chun/sentiment_arcs">
    <img src="images/graph_sentiment_arcs_smoothed_vwoolf_ttl.png" alt="Sentiment Arcs SMA Smoothed Peaks To The Lighthouse by Virginia Woolf"> 
    <!---  width="2048" height="1018"> --->
  </a>
  <br>
  <a href="https://github.com/jon-chun/sentiment_arcs">
    <img src="images/graph_sentiment_arc_lowess_mproust_guermantesway.png" alt="Sentiment Arcs LOWESS Smoothed Peaks Guermantes Way by Marcel Proust"> 
    <!---  width="2048" height="1018"> --->
  </a>
  <br>
</div> 

## Welcome!

SentimentArcs is a novel methodology and software framework for analyzing emotion in long texts or sequenced collections of shorter texts using Diachronic Sentiment Analysis. It segments any corpus of long text into semantic units (e.g. sentences, tweets, financial posts), applying an ensemble of over three dozen NLP sentiment analysis models from simple lexical models to state-of-the-art Transformer models. The resulting sentiment time series can be smoothed so key features like peaks and valleys can be detected and the surrounding text around these key crux points can be extracted for analysis by domain experts.

For literary experts features like peaks and valleys often correspond to key crux point in narrative. For financial analyst these could represent regime changes or arbitrage opportunities. For social media analysts these swings in could represent shifting public opinion on key topics, public figures or even terrorist cell activities. SentimentArcs is build around a a large ensemble of sentiment analysis models that surface interesting emotional arcs that domain experts can use to efficiently detect subtle and complex ground truths hidden within any sequenced body of text. 

## BACKGROUND

SentimentArcs is the result of many years of our experiences researching a wide variety of AI and machine learning technique to assist human experts in the extremely challenging task of analyzing and generating natural language texts. This includes a focus on AffectiveAI approaches to analyzing diverse textual corpora including literature, social media, news, scripts, lyrics, speeches, poems, financial reports, legal documents, etc. Virtually all sequential longform text have detectable and measurable sentiment changes over time that reveals cohesive narrative elements. SentimentArcs helps domain experts to efficiently arbitrate between competing machine learning and AI NLP models to quickly and efficiently identify, analyze and discover latent narratives elements and emotional arcs in text. 

SentimentArcs is the novel software framework underlying  <a href="https://www.cambridge.org/core/what-we-publish/elements/cambridge-elements-series">Katherine Elkins upcoming University of Cambridge Elements text </a>. This text speaks to the domain expert in Narrative Studies, Comparative Literature and English who want to learn how to use NLP sentiment analysis in general, and Sentiment Arcs in particular, for analyzing literature. The approach in this Cambridge Elements text is entirely generalizable to other fields. A more technical introduction to the core framework of SentimentArcs can be found in the <a href="https://arxiv.org/abs/2110.09454">October 2021 ArXiv paper by Jon Chun</a>. The Abstract of this paper outlines the technical focus and practical goals of Sentiment Arcs:

<blockquote>
SOTA Transformer and DNN short text sentiment classifiers report over 97% accuracy on narrow domains like IMDB movie reviews. Real-world performance is significantly lower because traditional models overfit benchmarks and generalize poorly to different or more open domain texts. This paper introduces SentimentArcs, a new self-supervised time series sentiment analysis methodology that addresses the two main limitations of traditional supervised sentiment analysis: limited labeled training datasets and poor generalization. A large ensemble of diverse models provides a synthetic ground truth for self-supervised learning. Novel metrics jointly optimize an exhaustive search across every possible corpus:model combination. The joint optimization over both the corpus and model solves the generalization problem. Simple visualizations exploit the temporal structure in narratives so domain experts can quickly spot trends, identify key features, and note anomalies over hundreds of arcs and millions of data points. To our knowledge, this is the first self-supervised method for time series sentiment analysis and the largest survey directly comparing real-world model performance on long-form narratives.
</blockquote>

## REFERENCE CORPORA

SentimentArcs can be viewed as an end-to-end pipeline to detect, extract, preprocess and analyze sentiment in any corpus of long-form texts. This includes both individual long-form texts as well as corpora compiled from individually time sequenced smaller texts like compilations of specific authors, genres, or periods as well as tweets, financial reports, topical news articles, speeches, etc. Initally, SentimentArcs is focused on offering users both carefully curated reference corpora to provide a ground truth and baseline reference for specific genres of text including novels, financial texts and social media. SentimentArcs also enables users to create new corpora of customized texts for specialized sentiment analysis tasks and analysis. Currently, SentimentArcs provides reference corpora for these types of texts (with more to be added in the future):

* Novels
* Financial Texts
* Social Media

For exmample, the reference corpus for novels consists of 25 narratives selected to create a diverse set of well recognized novels that can serve as a benchmark for sentiment analysis of other texts. The novel corpora spans approximately 2300 years from Homer’s Odyssey to the 2019 Machines like Me by award-winning author, Ian McEwan. Early 20th century modernists are emphasized with authors like Marcel Proust and Virginia Woolf. In sum, the corpora includes (1) the two most popular novels on Gutenberg.org (Project Gutenberg, 2021b), (2) eight of the fifteen most assigned novels at top US universities (EAB, 2021), and (3) three works that have sold over 20 million
copies (Books, 2021). There are eight works by women, two by African-Americans and five works by two LGBTQ authors. Britain leads with 15 authors followed by 6 Americans and one each from France, Russia, North Africa and Ancient Greece.

## SENTIMENT ANALYSIS MODELS

Concretely, Sentiment Arcs consists of a series of software modules embodied as Jupyter notebooks and supporting libraries designed to work on Google's free Colab service. Notebooks are executed in sequence reflecting different steps in the pipeline from text cleaning to sentiment time series analysis. Despite some shortcomings, Google Colab offers the lowest technical barrier for the widest range of non-technical Domain Experts as well as powerful-GPU backed Jupyter notebooks required for the most powerful state-of-the-art models in our ensemble. SentimentArc models/notebooks include:

* Text preprocessing (cleaning, advanced sentence segmentation, custom stopword sets, etc)
* An ensemble of over 3 dozen Sentiment Analysis Model including a diverse representation of major families (including the most popular sentiment analysis libraries and models from both R and Python as well as some AutoML techniques):

<blockquote>
<ul>
<li> Lexical
<li> Heuristics
<li> GOFAI Machine Learning
<li> Deep Neural Networks
<li> State of the Art Transformer Models
</ul>
</blockquote>

## FEATURES

* Novel Time Series Synthesis and Data Augmentation for NLP Sentiment Analysis Time Series
* Novel Peak Detection Algorithms customized for NLP Sentiment Analysis Time Series
* Efficient and Flexible Human-in-the-Loop to customize and tune the entire end-to-end process
* Flexible statistical, visualzation and text cutomizations so Domain Experts can quickly identify, extract and analyze key features of time series.


<p align="right">(<a href="#top">back to top</a>)</p>


<!---
### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Next.js](https://nextjs.org/)
* [React.js](https://reactjs.org/)
* [Vue.js](https://vuejs.org/)
* [Angular](https://angular.io/)
* [Svelte](https://svelte.dev/)
* [Laravel](https://laravel.com)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)

<p align="right">(<a href="#top">back to top</a>)</p>
--->


<!-- GETTING STARTED -->
## NOTEBOOKS

SentimentArcs is a pipeline of Google Colab Jupyter Notebooks run in sequence as follows:

<ol>
<li>Notebook 0: Copy SentimentArcs Github repo to your Google GDrive (run once at setup or to reset)
<li>Notebook 1: Preprocessing Text
<li>Notebook 2: Sentiment Analysis Models: R Lexicon and Heuristic using SyuzhetR(4) and SentimentR(8)
<li>Notebook 3: Sentiment Analysis Models: Python Lexicon, Heuristic and ML 
<li>Notebook 4: Sentiment Analysis Models: DNN and AutoML
<li>Notebook 5: Sentiment Analysis Models: Transformers(11)
<li>Notebook 6: Analysis, Visualizations, Smoothing and Crux Extraction
</ol>

<b>(INSERT NOTEBOOK PIPELINE FIGURE HERE)</b>

Data flows through the project subdirectory structure in a corresponding manner:

<ol>
<li>text_raw: minimally prepared textfiles for the corpus
<li>text_clean: text further cleaned by Sentiment Arcs
<li>sentiment_raw: raw sentiment values for all texts in the corpus
<li>sentiment_clean: processed sentiment time series 
<li>graphs_cruxes: extracted key features/crux points with surrounding text
<ol>

<b>(INSERT DATAFLOW PIPELINE FIGURE HERE)</b>

### Prerequisites

Sentiment Arcs relies upon Goolge to provide easy to use, ubiquitious and free access to powerful GPU-backed Jupyter Notebooks. Here are the free resources you should sign-up to use Sentiment Arcs:

* Google GMail Account (to have access to GDrive)
* Activate <a href="https://workspace.google.com/u/0/marketplace/app/colaboratory/1014160490159">Colab Jupyter Notebooks</a> to your GDrive from the Goolge Workspace Market
* Github account (if you which to report issues or comment)

### Installation

Colab Jupyter Notebooks offer a number of advantages, but can be a bit unorthodox to setup. Please follow the instructions below carefully as each step depends upon the previous steps.

1. Login to Google, goto your GDrive and create a subfolder to hold your copy of the SentimentArc project (e.g. /MyDrive/sentimentarcs/)

2. Be sure you have connected the Colab Notebooks app from the Google Workplace Market.

3. Navigate to your SentimentArcs project subdirectory and create/open a new Colab Notebook.

4. On the new blank Colab Notebook, to to the top left corner and select [File]->[Open Notebook]. When a pop-up window appears, select the [Github] from the right side of the top horizontal menu. Enter 'https://github.com/jon-chun/sentimentarcs_notebooks' on the top line after the prompt [Enter a GitHub URL or search by organization or user], click the search icon, and select 'sentiment_arcs_part1_text_preprocessing.ipynb' from the list below.

5. Run the first code cell to 'Connect Google GDrive' and grant permission for this notebook to connect to your GDrive.

6. Edit the input on the second code cell to point to the Sentiemnt Arcs project directory you defined in Step 1 and other information asked. Be sure to execute this code cell after entering this information.

7. Executing the next cell should copy over the current Sentiment Arcs code from Github if it does not already exist in your GDrive.

(Note: the private development repos do not work with simple passwords as of late 2021 and now <a href="https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/">require Github Token Authentication</a>)

