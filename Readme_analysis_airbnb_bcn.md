# Readme

## Project: analysis Airbnb data from Barcelona

### Motivation

During the last years, there has been several political movements in the city of Barcelona, which could have affected tourism.

The aim of this study is to gain some insights with the help of Airbnb data. The following questions are answered in the next lines:

- QUESTION 1: Which is the current situation of Airbnb hosts in BCN? Which are the characteristics of these accomodations? Are there overcrowded neighbourhhods?
- QUESTION 2: How has this situation evolved over the last years? Have there been an increase in the mean overnight stays prices over the last years? And in the amount of rooms and appartments available?
- QUESTION 3: Who is profiting from the touristic boom in BCN? Companies or individuals?

   
### Required installation

The following packages/libraries are required the data loading, preprocessing and analysis:

- Numpy
- Pandas
- Matplotlib
- Glob
- Pathlib: Path


### File Descriptions

For this purpose, the summary information and metrics for listings in Barcelona provided by Airbnb is used. This information extract is generated Airbnb every 3 months and is downloaded for the last 2 years (from 12-17 till 03-20).

- Link to data: http://insideairbnb.com/get-the-data.html
- Files names:
    - listings 12-17.csv
    - listings 02-18.csv
    - listings 06-18.csv
    - listings 09-18.csv
    - listings 12-18.csv
    - listings 03-19.csv
    - listings 06-19.csv
    - listings 09-19.csv
    - listings 12-19.csv
    - listings 03-20.csv
- Information included:
    - Host_id
    - Host_name
    - Id
    - Last_review
    - Latitude
    - Longitude
    - Minimum_nights
    - Name
    - Neighbourhood
    - Neighbourhood_group
    - Number_of_reviews
    - Price
    - Reviews_per_month
    - Room_type
    - Availability_365

For further information, please visit the link above.

### Project description

As explained in the motivation, the aim of this project is to gain some insights in the situation of tourism in BCN. For this purpose, descriptive statistics is mainly used. The following charts are plotted to explain and visualize the data:

- Concentration of accomodations per neighbourhood (Question 1)
- Distribution of accomodation types per neighbourhood (Question 1)
- Mean price in the different neighbourhoods (Question 1)
- Average availabiliy per neighbourhood (Question 1)
- Average availabiliy per room type (Question 1)
- Evolution of the amount accomodations over time (Question 2)
- Evolution of the accomodations types over time (Question 2)
- Mean price evolution over time in the different neighbourhoods (Question 2)
- Distribution of the managed accomodations by each host (Question 3)
- Distribution of accomodation over hosts (Question 3)
- Distribution of accomodations over hosts in the different neighbourhoods (Question 3)

### Authors

Pablo Cosio, pca_92@hotmail.com

### Acknowledgements

Thanks to Airbnb and Inside Airbnb for providing the required data to perform the analysis.


```python

```
