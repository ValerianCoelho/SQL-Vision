# SQL Vision - Convert Images into SQL Queries

SQL Vision is a tool that leverages image analysis and data processing to generate SQL queries from images. It extracts key details from images, creates SQL table creation queries, and offers a user-friendly interface for data input.

## Features

- Convert images into SQL table creation queries.
- Extracts relevant data from images for table columns.
- User-friendly interface for data type and constraint input.
- Interactive table display to facilitate data manipulation.
- Generates SQL queries for table creation and data insertion.

## Installation
- Download The zip file from the link provided in the About Section of this repo
- Unzip the file and run the 'SQL Vision.exe' file

## Usage
- Follow the prompts to provide the path to the image and input table details.
- Review and modify the extracted data as needed.
- The tool will generate CREATE TABLE and INSERT INTO queries based on your input.

## Examples
<details>
  <summary>Perfect Data Extraction</summary>
  
```
Welcome to SQL Vision
Enter the Path of the Image : Test Images\Image_Test_2.png
Enter the table name : EMPLOYEE

EMPNO:-
Data Type : varchar(5)
Constraint : primary key
EMP_NAME:-
Data Type : varchar(20)
Constraint : not null
DEPT:-
Data Type : varchar(20)
Constraint :
SALARY:-
Data Type : float
Constraint :
DOJ:-
Data Type : Date
Constraint :
BRANCH:-
Data Type : varchar(20)
Constraint :

┌───────┬──────────┬────────────┬────────┬─────────────┬───────────┐
│ EMPNO │ EMP_NAME │    DEPT    │ SALARY │     DOJ     │  BRANCH   │
╞═══════╪══════════╪════════════╪════════╪═════════════╪═══════════╡
│ E101  │   Amit   │ Production │ 45000  │ 12-Mar-2000 │ Bangalore │
├───────┼──────────┼────────────┼────────┼─────────────┼───────────┤
│ E102  │   Amit   │     HR     │ 70000  │ 03-Jul-2002 │ Bangalore │
├───────┼──────────┼────────────┼────────┼─────────────┼───────────┤
│ E103  │  Sunita  │ Management │ 120000 │ 11-Jan-2001 │  Mysore   │
├───────┼──────────┼────────────┼────────┼─────────────┼───────────┤
│ E104  │  Sunita  │     IT     │ 670000 │ 01-Aug-2001 │  Mysore   │
├───────┼──────────┼────────────┼────────┼─────────────┼───────────┤
│ E105  │  Mahesh  │   Civil    │ 145000 │ 13-Sep-2003 │   Pune    │
├───────┼──────────┼────────────┼────────┼─────────────┼───────────┤
│ E106  │  Kavya   │ Management │ 110000 │ 15-Jan-2001 │   Null    │
└───────┴──────────┴────────────┴────────┴─────────────┴───────────┘
If you are satisfied with the table click 'Enter'
If not enter the cell coord you wish to alter    
Coordinates (seperated by a comma) :

CREATE TABLE QUERY:-
CREATE TABLE EMPLOYEE (EMPNO varchar(5) primary key, EMP_NAME varchar(20) not null, DEPT varchar(20) , SALARY float , DOJ Date , BRANCH varchar(20) );

FILL TABLE QUERY:-
INSERT INTO EMPLOYEE (EMPNO, EMP_NAME, DEPT, SALARY, DOJ, BRANCH) VALUES ('E101', 'Amit', 'Production', 45000, '12-Mar-2000', 'Bangalore'), ('E102', 'Amit', 'HR', 70000, '03-Jul-2002', 'Bangalore'), ('E103', 'Sunita', 'Management', 120000, '11-Jan-2001', 'Mysore'), ('E104', 'Sunita', 'IT', 670000, '01-Aug-2001', 'Mysore'), ('E105', 'Mahesh', 'Civil', 145000, '13-Sep-2003', 'Pune'), ('E106', 'Kavya', 'Management', 110000, '15-Jan-2001', Null);
```
</details>

## Contributing
Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
