Title: NFT Post 2
Date: 2019-09-03
Modified: 2019-09-03
Category: Python
Tags: pelican, publishing
Slug: post-two
Authors: Tobias Reaper
Summary: Here's a short summary

# Here's a Headline

Here is the body content.

## A Smaller Headline

And an image...one that is styled.

<img class="size-auto" alt="Laptop" src="/images/laptop.jpg">

Here is a highlighted code snippet.

    :::python
    # 1. Import estimator class
    from sklearn.linear_model import LinearRegression

    # 2. Instantiate this class
    linear_reg = LinearRegression()

    # 3. Arrange X feature matrices (already did y target vectors)
    features = ['Pclass', 'Age', 'Fare']
    X_train = my_train[features]
    X_val = my_val[features]

    # Impute missing values
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer()
    X_train_imputed = imputer.fit_transform(X_train)
    X_val_imputed = imputer.transform(X_val)

    # 4. Fit the model
    linear_reg.fit(X_train_imputed, y_train)

    # 5. Apply the model to new data.
    # The predictions look like this ...
    linear_reg.predict(X_val_imputed)

And that's all, folks!
