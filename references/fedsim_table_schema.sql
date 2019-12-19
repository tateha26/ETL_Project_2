USE WEX_TVL_DB;

DROP TABLE IF EXISTS tpoc_info_fed;
DROP TABLE IF EXISTS traveler_info_fed;
DROP TABLE IF EXISTS fsde_employees_df;
DROP TABLE IF EXISTS employee_training;
DROP TABLE IF EXISTS pre_deployment_tasks;
DROP TABLE IF EXISTS client_info_fed;

CREATE TABLE client_info_fed (
	Record_Number INT AUTO_INCREMENT PRIMARY KEY,
    Employee_ID VARCHAR (250),
    Task_ID VARCHAR (250),
    Industry_Partner VARCHAR (250),
    Client_Id VARCHAR (250),
    Version_Date VARCHAR (250),
    Travel_No VARCHAR (250),
    Dt DATE,
    Project_Name VARCHAR (250),
    Project_ID_IA_No VARCHAR (250),
    Contract_Task_Order VARCHAR (250)
);

CREATE TABLE tpoc_info_fed (
	Record_Number INT AUTO_INCREMENT PRIMARY KEY,
	FOREIGN KEY (Record_Number) REFERENCES client_info_fed(Record_Number),
    From_Requestor VARCHAR (250),
	Through VARCHAR (250),
	Funding_Stream VARCHAR (250),
	Subject_ID VARCHAR (250),
	Cum_Amt_Billed INT (250),
	Cum_Amt_Billed_Balance INT,
    Estimate INT,
    Estimate_Balance INT,
    Employee_ID VARCHAR (250)
);

 CREATE TABLE traveler_info_fed (
	Record_Number INT AUTO_INCREMENT PRIMARY KEY,
    FOREIGN KEY (Record_Number) REFERENCES client_info_fed(Record_Number),
    Client_POC VARCHAR (250),
    ID_Project_Mgr VARCHAR (250),
    Travel_Justification VARCHAR (500),
    Employee_ID VARCHAR (250),
    Last_Name VARCHAR (250),
    First_Name VARCHAR (250),
    Company VARCHAR (250),
    Sub_Company_POC_Name VARCHAR (250),
    Sub_Company_Address VARCHAR (250),
    Sub_Company_City VARCHAR (250),
    Sub_Company_Phone VARCHAR (250),
    Sub_Company_email VARCHAR (250),
    Sub_Company_PO VARCHAR (250)
);
 
CREATE TABLE fsde_employees_df (
	Record_Number INT AUTO_INCREMENT PRIMARY KEY,
    FOREIGN KEY (Record_Number) REFERENCES client_info_fed(Record_Number),
    Employee_ID VARCHAR (250),
    Task_ID VARCHAR (250), 
	Last_Name VARCHAR (250),
	First_Name VARCHAR (250),
	Middle_Name VARCHAR (250),
	Birth_Date DATE,
	Place_Of_Birth VARCHAR (250),
	Company VARCHAR (250),
	Date_Hired DATE,
	OY2_PO_CODE VARCHAR (250),
	OY2_Org_Code VARCHAR (250),
	NOK_Date DATE,
	FSDE_Sheet_Date DATE,
	Position_Type VARCHAR (250),
	Deployment_Start_Date DATE,
	Deployment_End_Date DATE,
	Leave_Start_Date DATE, 
	Leave_End_Date DATE, 
	Mil_Leave_Start_Date DATE,
	Mil_Leave_End_Date DATE, 
	OY2_Project_String VARCHAR (250),
	PLC_Code VARCHAR (250), 
	Manager VARCHAR (250),
	DOD_ID VARCHAR (250),
	SSN VARCHAR (250),
	Primary_Phone VARCHAR (250),
	Secondary_Phone VARCHAR (250),
	Primary_Email VARCHAR (250),
	Secondary_Email VARCHAR (250),
	Passport_No VARCHAR (250), 
	Passport_Expiration DATE
);

CREATE TABLE employee_training (
	Record_Number INT AUTO_INCREMENT PRIMARY KEY,
	FOREIGN KEY (Record_Number) REFERENCES client_info_fed(Record_Number),
	Employee_ID VARCHAR (250),
	DITAC DATE,
	SIS DATE,
	FTP DATE, 
	JASA DATE, 
	DST_OSINT DATE,
	PROTON DATE,
	FMV_Academy DATE
);

CREATE TABLE pre_deployment_tasks (
	Record_Number INT AUTO_INCREMENT PRIMARY KEY,
    FOREIGN KEY (Record_Number) REFERENCES client_info_fed(Record_Number),
	Employee_ID VARCHAR (250),
	Deployment_Start_Date DATE, 
	CCM_Submit DATE,
	CI_Brief DATE,
	Visa_Submitted DATE,
	SRC_Date DATE,
	SRC_Travel_Submission DATE,
	Deployment_Travel_Submission DATE
);

SELECT * FROM client_info_fed;
SELECT * FROM tpoc_info_fed;
SELECT * FROM traveler_info_fed;
SELECT * FROM fsde_employees_df;
SELECT * FROM employee_training;
SELECT * FROM pre_deployment_tasks;