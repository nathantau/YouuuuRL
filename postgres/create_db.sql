-- Create the database called 'url';
\c url

-- Create the table with the following fields 
CREATE TABLE url(
    id SERIAL, 
    url VARCHAR(255) NOT NULL
);
