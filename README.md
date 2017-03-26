# Big-Data-Anayltics
Hands on Hadoop and Spark using the Hadoop streaming and PySpark.
# About the Data:
The data used for this project is a subset of the NYC parking violation data which can be found at: [ViolationData](https://vgc.poly.edu/~juliana/courses/BigData2017/Data/parking-violations.tar.gz).

There are 2 csv files in the violation data:
- **Parking Violations**
    This data has records of all the violations that are made in the NYC.
- **Open Violations**
    This data has records of all the violations that are still open i.e. they are not paid.
# What this Project covers?
There are 7 tasks performed on the March 2016 subset of the NYC violation data.   
  -  **Task 1**
    We found out all the parking violations that were paid, i.e., that did not occur in open-violations.csv.
- **Task 2**
    We found the distribution of the violation types, i.e., for each violation code, the number of violations that had this code.
 - **Task 3**
     We computed the total and average amount due in open violations for each license type.
- **Task 4**	
    We computed the total number of violations for vehicles registered in the state of NY and all other vehicles.
- **Task 5**
    We found the vehicle that had the greatest number of violations (assuming that plate_id and registration_state uniquely identify a vehicle).
- **Task 6**
    We found the top-20 vehicles in terms of total violations (assuming that plate id and registration state uniquely identify a vehicle).
- **Task 7**
    We computed the average number of violations with each code issued per day on weekdays and weekend days.



