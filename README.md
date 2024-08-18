![header](headerNew.png)

# Optimizing Ride Fares: A Dynamic Pricing Model for Ride-Sharing Services

## About
A ride-sharing company uses a time-based strategy for determining fares of the services. Since this strategy only considers one factor, the company is now exploring an ML-based dynamic pricing strategy to manage demands in their services. My objective is to build a dynamic pricing model that takes into account various factors influencing fares, such as time of booking, loyalty status, and expected ride duration. By dynamically adjusting prices based on real-time conditions, this model aims to better manage supply and demand and enhance customer satisfaction through more personalized pricing. Ultimately, this approach is expected to optimize the company's profitability in fluctuating demand scenarios. Involving 12 algorithms and 3 experimental setups, the final model achieved high R-squared of 0.84 with minimum mispredictions (RMSE: USD 68 and MAE: USD 53) in testing data. In a simulation using a limited test size (*N* = 100), the model is projected to generate a net profit of USD 2.4K.

>[!important]
> The report of this project is in the form of Jupyter notebook which can be accessed [here](https://github.com/LingAdeu/dynamic-pricing-model/blob/main/notebook/notebook.ipynb). However, since some parts of the report cannot be seen directly on GitHub, e.g., pipeline and SHAP plot for demonstrating how the Lasso Regression model works, consider reading the report on [NBViewer](https://nbviewer.org/github/LingAdeu/dynamic-pricing-model/blob/main/notebook/notebook.ipynb).

## Content
    .
    ├── README.md               <- The top-level README for using this project
    ├── data
    │   └── dynamic_pricing.csv <- The dataset used to train and test the models
    ├── model
    │   └── final_model.pkl     <- The final model (Lasso Regression)
    ├── notebook
    │   └── notebook.ipynb      <- The Jupyter notebook to build the model
    └── requirements.txt        <- The requirements file for reproducing the environment

## Feedback
If there are any questions or suggestions for improvements, feel free to contact me here:

<a href="https://www.linkedin.com/in/adelia-januarto/" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/linkedin/default.svg" width="52" height="40" alt="linkedin logo"/>
  </a>
<a href="mailto:januartoadelia@gmail.com" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/gmail/default.svg"  width="52" height="40" alt="gmail logo"/>
  </a>