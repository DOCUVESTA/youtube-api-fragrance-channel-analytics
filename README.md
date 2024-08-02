<h1 align="center">
	Engagement Metrics Analysis of a Perfume Youtube Channel Using YouTube API
</h1>

<h3 align="center">
	<img src="https://github.com/DOCUVESTA/youtube-api-fragrance-channel-analytics/blob/ce6f2c922f0725779302141716324ead5ff6515c/assets/header_perfume.png"/>
</h3>

## Overview
What better way to discover new products than through a recommendation? It's pre-vetted and, if we're lucky, it includes a detailed breakdown of the product's pros and cons. Nowadays, if we're considering buying a new sunscreen, lotion, or perfume, it's likely because we've seen it highlighted by an influencer on social media. For this project, I analyze Monika Cioch's YouTube channel, which is largely dedicated on reviewing, discovering, and recommending perfumes. This analysis aims to understand her viewers' preferences by examining engagement metrics such as views, likes, and comment counts to determine which of her videos performs the best.

<br>

## Data Context
#### For the analysis, each video was categorized into a specific group
<table style="width:100%">
    <tr>
        <th>Category Name</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>recommendation</td>
        <td>in-depth description about a perfume</td>
    </tr>
    <tr>
        <td>review</td>
        <td>first impression of a perfume or perfume comparison</td>
    </tr>
    <tr>
        <td>informative</td>
        <td>in-depth breakdown of a specific perfume or videos on how to choose a perfume</td>
    </tr>
    <tr>
        <td>fun</td>
        <td>non-perfume related videos for entertainment</td>
    </tr>
    <tr>
        <td>fashion</td>
        <td>non-perfume related videos about fashion</td>
    </tr>
    <tr>
        <td>shorts</td>
        <td>Youtube shorts</td>
    </tr>
</table>



## Analytics
<h3 align="center">
	<img src="https://github.com/DOCUVESTA/youtube-api-fragrance-channel-analytics/blob/5b77903a1e795d91e10ed033bb06069d3ce57ec6/assets/information_bar.png"/>
</h3>


	
<img src="https://github.com/DOCUVESTA/youtube-api-fragrance-channel-analytics/blob/44ee6ea1b625fbf28f42c16bdacd1afc60c03e03/assets/categories_and_metrics.png"/>
<img src="https://github.com/DOCUVESTA/youtube-api-fragrance-channel-analytics/blob/44ee6ea1b625fbf28f42c16bdacd1afc60c03e03/assets/all_violin_plots.png"/>

<img src="https://github.com/DOCUVESTA/youtube-api-fragrance-channel-analytics/blob/8eb523ddaa84cd1d97a6741374f507814e5b8a92/assets/top_performing_videos.png"/>

<br>


## Key Insights




<br>

## Future Work




<br>

## Repository Contents
### Folder: data
##### All data used to complete project
<table style="width:100%">
    <tr>
        <th>File Name</th>
        <th>Data Description</th>
    </tr>
    <tr>
        <td>video_info.csv</td>
        <td>raw data from Youtube API</td>
    </tr>
    <tr>
        <td>video_info_with_categories.csv</td>
        <td>added new column named 'category' to classify videos</td>
    </tr>
    <tr>
        <td>video_info_cleaned.csv</td>
        <td>final cleaned data</td>
    </tr>
</table>
<br>

### Python File: youtube_api_data_collection.py
- Extracts engagement metrics from a perfume YouTube channel
- Utilizes the YouTube API for data retrieval
- Saves the data in csv format

<br>

### Jupyter Notebook: data_transformation_fragrance_youtube.ipynb
- Jupyter notebook with annotations detailing each stage of preprocessing data from Youtube's API
- Data exploration process
- Plotly visualizations

<br>

### Folder: assets
##### All assets used to complete project
- pictures
- graphs
- tables






