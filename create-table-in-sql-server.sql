USE IrisDB;
GO

CREATE TABLE dbo.iris_data (
    sepal_length FLOAT NOT NULL,
    sepal_width FLOAT NOT NULL,
    petal_length FLOAT NOT NULL,
    petal_width FLOAT NOT NULL,
    species NVARCHAR(50) NOT NULL
);
