USE WEX_TVL_DB;

CREATE TABLE client_info_fed (
	Employee_ID varchar (250),
    Task_ID VARCHAR (250),
    Industry_Partner VARCHAR (250),
    Client_Id VARCHAR (250),
    Version_Date VARCHAR (250),
    Travel_No VARCHAR (250),
    Dt date,
    Project_Name varchar (250),
    Project_ID_IA_No varchar (250),
    Contract_Task_Order varchar (250),
    PRIMARY KEY (Employee_ID)
);

# use WEX_TVL_DB;

DROP TABLE fsde_employee_travel;
pre_deployment_tasks;
client_info_fed;
pre_deployment_tasks
tpoc_info_fed
traveler_info_fed
fsde_employees_df
employee_training

select * from client_info_fed;

CREATE TABLE tpoc_info_fed (
	From_Requestor varchar (250),
	Through varchar (250),
	Funding_Stream varchar (250),
	Subject_ID varchar (250),
	Cum_Amt_Billed int (250),
	Cum_Amt_Billed_Balance int,
    Estimate int,
    Estimate_Balance int,
    Employee_ID varchar (250),
    primary key (Employee_ID)
);

select * from tpoc_info_fed;

drop table tpoc_info_fed;

 CREATE TABLE traveler_info_fed (
	Client_POC varchar (250),
    ID_Project_Mgr varchar (250),
    Travel_Justification varchar (500),
    Employee_ID varchar (250),
    Last_Name VARCHAR (250),
    First_Name VARCHAR (250),
    Company varchar (250),
    Sub_Company_POC_Name varchar (250),
    Sub_Company_Address varchar (250),
    Sub_Company_City varchar (250),
    Sub_Company_Phone VARCHAR (250),
    Sub_Company_email varchar (250),
    Sub_Company_PO VARCHAR (250),
    primary key (Employee_ID)
);
 
 select * from traveler_info_fed;
 
CREATE TABLE fsde_employees_df (
	Employee_ID varchar (250),
    Task_ID VARCHAR (250), 
	Last_Name varchar (250),
	First_Name varchar (250),
	Middle_Name varchar (250),
	Birth_Date date,
	Place_Of_Birth varchar (250),
	Company varchar (250),
	Date_Hired date,
	OY2_PO_CODE VARCHAR (250),
	OY2_Org_Code VARCHAR (250),
	NOK_Date date,
	FSDE_Sheet_Date date,
	Position_Type varchar (250),
	Deployment_Start_Date date,
	Deployment_End_Date date,
	Leave_Start_Date date, 
	Leave_End_Date date, 
	Mil_Leave_Start_Date date,
	Mil_Leave_End_Date date, 
	OY2_Project_String varchar (250),
	PLC_Code VARCHAR (250), 
	Manager VARCHAR (250),
	DOD_ID VARCHAR (250),
	SSN VARCHAR (250),
	Primary_Phone VARCHAR (250),
	Primary_Email varchar (250),
	Secondary_Email varchar (250),
	Passport_No VARCHAR (250), 
	Passport_Expiration date,
	PRIMARY KEY (Employee_ID)
);

select * from fsde_employees_df;

CREATE TABLE employee_training (
Employee_ID varchar (250),
DITAC date,
SIS date,
FTP date, 
JASA date, 
DST_OSINT date,
PROTON date,
FMV_Academy date,
primary key (Employee_ID)
);

select * from employee_training;

CREATE TABLE pre_deployment_tasks (
Employee_ID varchar (250),
Deployment_Start date, 
CCM_Submit date,
CI_Brief date,
Visa_Submitted date,
SRC_Date date,
SRC_Travel_Submission date,
Deployment_Travel_Submission date,
Primary Key (Employee_ID)
);

#insert '01/01/2020' into pre_deployment_tasks (SRC_Date);
select * from pre_deployment_tasks;

#SELECT CONVERT (datetime, 'MM/DD/YYYY');
    
    