from flask import Flask, render_template, jsonify, request
import pandas as pd
# from flask_mysqldb import MySQL

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'MySqL_JNJ13!'
# app.config['MYSQL_DB'] = 'DataBootCamp'

# mysql = MySQL(app)

# @app.route('/', methods=['POST'])
# def index():
#     if request.method == 'POST':
#         detail = request.form
#         first_name = detail['first_name']
#         last_name = detail['last_name']
#         cur = mysql.connection.cursor()
#         cur.execute ("INSERT INTO MyUsers(first_name, last_name) VALUES (%s, %s)")
#         mysql.connection.commit()
#         cur.close()
#         return 'success'

# @app.route('/')
# def index():
#     return 'Hello'

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        
        req = request.form

        Industry_Partner = req['industry_partner']
        Client_Id = req['client_id']
        Version_Date = req['version_date']
        Travel_No = req['travel_no']
        Dt = req['dt']
        Project_Name = req['project_name']
        Project_ID_IA_No = req['project_id']
        Contract_Task_Order = req['contract_task_order']
        
        From_Requestor = req['from_requestor']
        Through = req['client_id']
        Funding_Stream = req.get('funding_stream')
        Subject_ID = req['subject_id']
        Cum_Amt_Billed = req['cum_amt_billed']
        Cum_Amt_Billed_Balance = req['cum_amt_billed_balance']
        Estimate = req['estimate']
        Estimate_Balance = req['estimate_balance']

        Client_POC = req['client_poc']
        ID_Project_Mgr = req['id_project_mgr']
        Travel_Justification = req['travel_justification']
        First_Name = req['first_name']
        Middle_Name = req['middle_name']
        Last_Name = req['last_name']
        Company = req['company']
        Sub_Company_POC_Name = req['sub_company_poc_name']
        Sub_Company_Address = req['sub_company_address']
        Sub_Company_City = req['sub_company_city']
        Sub_Company_Phone = req['sub_company_phone']
        Sub_Company_email = req['sub_company_email']
        Sub_Company_PO = req['sub_company_po']
        
        Birth_Date = req['birth_date']
        Place_Of_Birth = req['place_of_birth']
        SSN = req['ssn']
        DOD_ID = req['dod_id']
        Passport_No = req['passport_no']
        Passport_Expiration = req['passport_expiration']
        Employee_ID = req['employee_id']
        Date_Hired = req['date_hired']
        Position_Type = req['position_type']
        Primary_Phone = req['primary_phone']
        Secondary_Phone = req['primary_phone']
        Primary_Email = req['primary_email']
        Secondary_Email = req['secondary_email']
        Task_ID = req['task_id']
        Manager = req['manager']
        OY2_PO_CODE = req['oy2_po_code']
        OY2_Org_Code = req['oy2_org_code']
        OY2_Project_String = req['oy2_project_string']
        PLC_Code = req['plc_code']
        NOK_Date = req['nok_date']
        FSDE_Sheet_Date = req['fsde_sheet_date']
        Deployment_Start_Date = req['deployment_start_date']
        Deployment_End_Date = req['deployment_end_date']
        Leave_Start_Date = req['leave_start_date']
        Leave_End_Date = req['leave_end_date']
        Mil_Leave_Start_Date = req['mil_leave_start_date']
        Mil_Leave_End_State = req['mil_leave_end_date']
        
        DITAC = req['ditac']
        SIS = req['sis']
        FTP = req['ftp']
        JASA = req['jasa']
        DST_OSINT = req['dst_osint']
        PROTON = req['proton']
        FMV_Academy = req['fmv_academy']
        
        CCM_Submit = req['ccmsubmit']
        CI_Brief = req['ci_brief']
        Visa_Submitted = req['visa_submitted']
        SRC_Date = req['src_date']
        SRC_Travel_Submission = req['src_travel_submission']
        Deployment_Travel_Submission = req['deployment_travel_submission']

        # cur = mysql.connection.cursor()
        # cur.execute ("INSERT INTO MyUsers(first_name, last_name) VALUES (%s, %s)")
        # mysql.connection.commit()
        # cur.close()
        
        client_info_fed = {
            'Employee_ID':Employee_ID,
            'Task_ID':Task_ID,
            'Industry_Partner':Industry_Partner,
            'Client_Id':Client_Id,
            'Version_Date':Version_Date,
            'Travel_No':Travel_No,
            'Dt':Dt,
            'Project_Name':Project_Name,
            'Project_ID_IA_No':Project_ID_IA_No,
            'Contract_Task_Order':Contract_Task_Order
            }
        
        tpoc_info_fed = {
            'From_Requestor':From_Requestor,
            'Through':Through,
            'Funding_Stream':Funding_Stream,
            'Subject_ID':Subject_ID,
            'Cum_Amt_Billed':Cum_Amt_Billed,
            'Cum_Amt_Billed_Balance':Cum_Amt_Billed_Balance,
            'Estimate':Estimate,
            'Estimate_Balance':Estimate_Balance,
            'Employee_ID':Employee_ID
        }

        traveler_info_fed = {
            'Employee_ID':Employee_ID,
            'Client_POC':Client_POC,
            'ID_Project_Mgr':ID_Project_Mgr,
            'Travel_Justification':Travel_Justification,
            'Last_Name':Last_Name,
            'First_Name':First_Name,
            'Company':Company,
            'Sub_Company_POC_Name':Sub_Company_POC_Name,
            'Sub_Company_Address':Sub_Company_Address,
            'Sub_Company_City':Sub_Company_City,
            'Sub_Company_Phone':Sub_Company_Phone,
            'Sub_Company_email':Sub_Company_email,
            'Sub_Company_PO':Sub_Company_PO,
        }

        fsde_employees_df = {
            'Employee_ID':Employee_ID,
            'Task_ID':Task_ID,
            'Last_Name':Last_Name,      
            'First_Name':First_Name,
            'Middle_Name':Middle_Name,    
            'Birth_Date':Birth_Date,
            'Place_Of_Birth':Place_Of_Birth,
            'Company':Company,
            'Date_Hired':Date_Hired,
            'OY2_PO_CODE':OY2_PO_CODE,
            'OY2_Org_Code':OY2_Org_Code,
            'NOK_Date':NOK_Date,
            'FSDE_Sheet_Date':FSDE_Sheet_Date,
            'Position_Type':Position_Type,
            'Deployment_Start_Date':Deployment_Start_Date,
            'Deployment_End_Date':Deployment_End_Date,
            'Leave_Start_Date':Leave_Start_Date,
            'Leave_End_Date':Leave_End_Date,
            'Mil_Leave_Start_Date':Mil_Leave_Start_Date,
            'Mil_Leave_End_State':Mil_Leave_End_State,
            'OY2_Project_String':OY2_Project_String,
            'PLC_Code':PLC_Code,
            'Manager':Manager,
            'DOD_ID':DOD_ID,
            'SSN':SSN,
            'Primary_Phone':Primary_Phone,
            'Secondary_Phone':Secondary_Phone,
            'Primary_Email':Primary_Email,
            'Secondary_Email':Secondary_Email,
            'Passport_No':Passport_No,
            'Passport_Expiration':Passport_Expiration
        }

        employee_training = {
            'Employee_ID':Employee_ID,
            'DITAC':DITAC,
            'SIS':SIS,
            'FTP':FTP,
            'JASA':JASA,
            'DST_OSINT':DST_OSINT,
            'PROTON':PROTON,
            'FMV_Academy':FMV_Academy
        }

        pre_deployment_tasks = {
            'Employee_ID':Employee_ID,
            'Deployment_Start_Date':Deployment_Start_Date,
            'CCM_Submit':CCM_Submit,
            'CI_Brief':CI_Brief,
            'Visa_Submitted':Visa_Submitted,
            'SRC_Date':SRC_Date,
            'SRC_Travel_Submission':SRC_Travel_Submission,
            'Deployment_Travel_Submission':Deployment_Travel_Submission
        }

        tables = [
            client_info_fed,
            tpoc_info_fed,
            traveler_info_fed,
            fsde_employees_df,
            employee_training,
            pre_deployment_tasks
        ]

        # data_df = pd.DataFrame([data_dict])
        # data_df.to_csv('input.csv')
        return jsonify(tables)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)