## Project proposal form

Please provide the information requested in the following form. Try to provide concise and informative answers.

**1. What is your project title?**

Airbnb Recommender System using Different Matrix Factorization Models


**2. What is the problem that you want to solve?**

Optimize the airbnb recommendation and search with different matrix factorization models


**3. What distributed computing for big data methodologies and systems do you plan to use?**

In this project, we'll use Apache Hadoop for storing our collection of unstructured data containing descriptions about Airbnb listings.. We use Hadoop since it incorporates MapReduce, which allows us to clean and reorganize the text data to a trainable format. Afterward, we use Apache Spark for our distributed computation. Specifically, we utilize Spark’s Mlib, which is a scalable machine learning library that features an implementation of Latent Dirichlet Allocation (LDA), the model we are going to use for our project. Our strategy involves utilizing Spark both for training our LDA model using the textual data from Airbnb listings and for computing recommendations based on past user interactions and bookings.

The methodology of our project is designed to exploit big data and machine learning for the purpose of recommending Airbnb listings to users based on their preferences and past bookings. First, we will need to load and then clean and pre-process our data. From our initial database of Airbnb listings information, we would collect descriptions of listings. Afterward we would preprocess to collect and separate the words in the listings, removing unnecessary and invalid words from the text. Then,  we apply the LDA to the textual content of our Airbnb Listings to discover latent topics ( eg: cozy house, quiet area, city center, etc). By applying LDA, each listing is associated with a distribution over a topic, indicating the degree to which it belongs to each inferred topic. From here, we utilize the user’s history bookings to see which kind of topics the user prefers and use that to suggest listing that resembles the user’s preferred topic. For example, if users often look at cozy places, our system will learn that topic and then we can recommend new places that match those themes. Third, we will evaluate the recommendation using appropriate metrics and user feedback. 


**4. What dataset will you use? You may assess the suitability of the dataset for distributed computing for big data. Provide information about the dataset (size, features and labels, if applicable) and a URL for the dataset if available. If you intend to generate synthetic data, provide a description of what features you will use, whether your dataset is labelled or not (supervised versus unsupervised learning problem), how will it be generated (any functions, seed values etc) and the expected size. When choosing or generating data, please remember to consider any aspects related to data representativeness, quality, bias and other aspects relevant to your project**

Airbnb host data:
https://public.opendatasoft.com/explore/dataset/airbnb-listings/information/?disjunctive.host_verifications&disjunctive.amenities&disjunctive.features&location=16,40.71595,-73.95293&basemap=jawg.light

Airbnb user’s review: 
https://www.kaggle.com/code/qusaybtoush1990/airbnb-analysis-dataset/input

**5. List key references (e.g. research papers) that your project will be based on. Please cite them properly and provide URLs.**

Optimizing Airbnb Search Journey with Multi-task Learning
https://dl.acm.org/doi/pdf/10.1145/3580305.3599881

Real-time Personalization using Embeddings for Search Ranking at Airbnb
https://dl.acm.org/doi/10.1145/3219819.3219885

**Please indicate whether your project proposal is ready for review (Yes/No):**
Yes

## Feedback (to be provided by the lecturer)

[MB - 01/04/2024] The project concentrates on the combination of matrix factorisation models to optimise the Airbnb recommendation system. The problem is not new and is sufficiently addressed in the literature (see [here](https://dl.acm.org/doi/10.1145/3219819.3219885), [here](https://medium.com/@alexandra.gg150/how-to-build-a-recommender-system-for-airbnb-in-python-3a92ad500fa5) and [here](https://github.com/goelshivani321/cmpe256-airbnbproject)). The main points related to your proposal that need to be revised are:

* how does the current proposal differ from existing works or the examples used in the seminar? Do you intend to perform a comparative analysis of isolated matrix factorisation models based on some error estimation metric or are you considering a combination of models, such as an ensemble, so you can apply some voting mechanism for better outputs?
* how many features related to Airbnb listings would be necessary for a good recommendation? Are you planning to test with an increasing number of them? What about features related to users' preferences and booking history? Are you able to keep track of a few users over time, so you can infer some pattern or reliable preference? Which other "past user interaction" information would be available in these datasets?
* So, you apply LDA over a set of Airbnb listings to extract topics and related words - the same that supposedly are used to describe the listing (perhaps in the "about the space" section). Then, you feed these topics and words into another method to match user preferences and provide recommendations. Finally, as a validation step, you compare such recommendations against other (similar) recommendations for the same cluster of users. Would that be your desired application? Are you able to group users by similar preferences, for instance? Or group listing by similar characteristics (such as the keywords you mentioned)?
* you must consider two different situations and whether the datasets allow you to analyse each one: users with a history of bookings and new users (cold-start strategy). Your solution must provide consistent and reliable recommendations for both cases.
* on the big data side: why do you need Hadoop MapReduce to perform data preprocessing? Wouldn't be easier to apply standard Python libraries for that, before feeding the data into any LDA or other factorisation method? Remember to consider scalability scenarios: start with a small sample to test your solution and then increase the data size to a baseline solution, to get the intended results. If time allows, you can keep increasing the dataset size to test any technical limits of your solution - such as the number of topics and words, amount of users versus listings etc.
* There's no need to resubmit your proposal but you must extend it beyond existing works and define a few research questions/analytical scenarios to be answered by your solution. There is potential contribution if you manage to deploy a pipeline with proper data ingestion from Airbnb data (listings, customers and other relevant aspects), preprocessing, utilisation of different models - as an ensemble or in parallel, for comparison purposes, followed by consistent recommendations and subsequent validation.

**Project conditionally approved**.
* 
