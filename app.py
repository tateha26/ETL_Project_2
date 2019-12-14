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
        
        client_dict = {
            'Employee_ID':employee_id,
            'Task_ID':task_id,
            'Industry_Partner':industry_partner,
            'Client_Id':client_id,
            'Version_Date':version_date,
            'Travel_No':travel_no,
            'Dt':dt,
            'Project_Name':project_name,
            'Project_ID_IA_No':project_id,
            'Contract_Task_Order':contract_task_order
            }
        
        tpoc_dict = {
            'From_Requestor':from_requestor,
            'Through':through,
            'Funding_Stream':funding_stream,
            'Subject_ID':subject_id,
            'Cum_Amt_Billed':cum_amt_billed,
            'Cum_Amt_Billed_Balance':cum_amt_billed_balance,
            'Estimate':estimate,
            'Estimate_Balance':estimate_balance,
            'Employee_ID':employee_id
        }

        traveler_dict = {
            'Employee_ID':employee_id,
            'Client_POC':client_poc,
            'ID_Project_Mgr':id_project_mgr,
            'Travel_Justification':travel_justification,
            'Last_Name':last_name,
            'First_Name':first_name,
            'Company':company,
            'Sub_Company_POC_Name':sub_company_poc_name,
            'Sub_Company_Address':sub_company_address,
            'Sub_Company_City':sub_company_city,
            'Sub_Company_Phone':sub_company_phone,
            'Sub_Company_email':sub_company_email,
            'Sub_Company_PO':sub_company_po,
        }

        employee_dict = {
            'Employee_ID':employee_id,
            'Task_ID':task_id,
            'Last_Name':last_name,      
            'First_Name':first_name,
            'Middle_Name':middle_name,    
            'Birth_Date':birth_date,
            'Place_Of_Birth':place_of_birth,
            'Company':company,
            'Date_Hired':date_hired,
            'OY2_PO_CODE':oy2_po_code,
            'OY2_Org_Code':oy2_org_code,
            'NOK_Date':nok_date,
            'FSDE_Sheet_Date':fsde_sheet_date,
            'Position_Type':position_type,
            'Deployment_Start_Date':deployment_start_date,
            'Deployment_End_Date':deployment_end_date,
            'Leave_Start_Date':leave_start_date,
            'Leave_End_Date':leave_end_date,
            'Mil_Leave_Start_Date':mil_leave_start_date,
            'Mil_Leave_End_State':mil_leave_end_date,
            'OY2_Project_String':oy2_project_string,
            'PLC_Code':plc_code,
            'Manager':manager,
            'DOD_ID':dod_id,
            'SSN':ssn,
            'Primary_Phone':primary_phone,
            'Secondary_Phone':primary_phone,
            'Primary_Email':primary_email,
            'Secondary_Email':secondary_email,
            'Passport_No':passport_no,
            'Passport_Expiration':passport_expiration
        }

        training_dict = {
            'Employee_ID':employee_id,
            'DITAC':ditac,
            'SIS':sis,
            'FTP':ftp,
            'JASA':jasa,
            'DST_OSINT':dst_osint,
            'PROTON':proton,
            'FMV_Academy':fmv_academy
        }

        task_dict = {
            'Employee_ID':employee_id,
            'Deployment_Start_Date':deployment_start_date,
            'CCM_Submit':ccmsubmit,
            'CI_Brief':ci_brief,
            'Visa_Submitted':visa_submitted,
            'SRC_Date':src_date,
            'SRC_Travel_Submission':src_travel_submission,
            'Deployment_Travel_Submission':deployment_travel_submission
        }

        tables = [
            client_dict,
            tpoc_dict,
            traveler_dict,
            employee_dict,
            training_dict,
            task_dict
        ]

        # data_df = pd.DataFrame([data_dict])
        # data_df.to_csv('input.csv')
        return jsonify(tables)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)